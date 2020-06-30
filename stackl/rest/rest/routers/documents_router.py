import logging
from collections.abc import Collection

from fastapi import APIRouter, HTTPException, Request, status
from stackl.models.configs.document_model import CollectionDocument, BaseDocument

from stackl.tasks.document_task import DocumentTask
from stackl.task_broker.task_broker_factory import TaskBrokerFactory

logger = logging.getLogger("STACKL_LOGGER")
router = APIRouter()

task_broker = TaskBrokerFactory().get_task_broker()


@router.get('/{type_name}', response_model=CollectionDocument)
def collect_documents_by_type(type_name: str):
    """Returns a collection of all the documents with the specific type and optionally containing the given name"""
    logger.info(
        f"[CollectionDocumentByType GET] API COLLECT request with type_name '{type_name}'"
    )
    task = DocumentTask.parse_obj({
        'channel': 'worker',
        'args': type_name,
        'subtype': "COLLECT_DOCUMENT"
    })

    task_broker.give_task(task)
    result = task_broker.get_task_result(task.id)
    document: CollectionDocument = {
        "name": "CollectionDocumentByType_" + type_name,
        "description":
        "Document that contains all the documents by type " + type_name,
        "type": type_name,
        "documents": result
    }
    if not isinstance(result, Collection):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="NOT OK!")
    return document


@router.get('/{type_name}/{name}')
def get_document_by_type_and_name(type_name: str, name: str):
    """Returns a specific document with a type and name"""
    logger.info(
        f"[DocumentByTypeAndName GET] API GET request for type '{type_name}' and document '{name}'"
    )
    task = DocumentTask.parse_obj({
        'channel': 'worker',
        'args': (type_name, name),
        'subtype': "GET_DOCUMENT"
    })
    task_broker.give_task(task)
    result = task_broker.get_task_result(task.id)

    if not isinstance(result, Collection):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="NOT OK!")
    return result


@router.post('')
def post_document(document: BaseDocument):
    """Create the document with a specific type and an optional name given in the payload"""
    logger.info(f"[PostDocument] Receiver POST request with data: {document}")

    task = DocumentTask.parse_obj({
        'channel': 'worker',
        'document': document.dict(),
        'subtype': "POST_DOCUMENT"
    })

    task_broker.give_task(task)
    result = task_broker.get_task_result(task.id)

    if not StatusCode.is_successful(result):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="NOT OK!")
    return result


@router.put('')
def put_document(document: BaseDocument, request: Request):
    """Update (or create) the document with a specific type and an optional name given in the payload"""
    logger.info(f"[PutDocument] API PUT request with data: {document}")
    json_body = request.json()
    logger.info(f"[PutDocument] API PUT request with request: {json_body}")
    task = DocumentTask.parse_obj({
        'channel': 'worker',
        'document': json_body,
        'subtype': "PUT_DOCUMENT"
    })

    task_broker.give_task(task)
    result = task_broker.get_task_result(task.id)
    logger.info(f"[PutDocument] API PUT request with result: '{result}'")

    if not StatusCode.is_successful(result):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="NOT OK!")

    return result


@router.delete('/{type_name}/{name}')
def delete_document(type_name: str, name: str):
    """Delete a specific document with a type and name"""
    logger.info(
        f"[DeleteDocument] API Delete request for type '{type_name}' and document '{name}'"
    )
    task = DocumentTask.parse_obj({
        'channel': 'worker',
        'args': (type_name, name),
        'subtype': "DELETE_DOCUMENT"
    })

    task_broker.give_task(task)
    result = task_broker.get_task_result(task.id)

    if not StatusCode.is_successful(result):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="NOT OK!")
    return result