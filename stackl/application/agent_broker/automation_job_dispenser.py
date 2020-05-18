import json
import logging

from redis import StrictRedis

import model
from manager.document_manager import DocumentManager
from model.items.functional_requirement_status_model import FunctionalRequirementStatus
from protos.agent_pb2 import AgentMetadata, Invocation, ConnectionResult, AutomationResult, Status
from protos.agent_pb2_grpc import StacklAgentServicer

logger = logging.getLogger("STACKL_LOGGER")


class AutomationJobDispenser(StacklAgentServicer):
    def __init__(self, redis: StrictRedis, document_manager: DocumentManager):
        self.redis = redis
        self.document_manager = document_manager

    def RegisterAgent(self, agent_metadata: AgentMetadata, context):
        self.redis.set(f'agents/{agent_metadata.name}',
                       agent_metadata.selector)
        connection_result = ConnectionResult()
        connection_result.success = True
        return connection_result

    def GetJob(self, agent_metadata: AgentMetadata, context):
        logger.debug(f"Request for job received")
        agent_p = self.redis.pubsub()
        agent_p.subscribe(agent_metadata.name)
        for message in agent_p.listen():
            logger.debug(f"Recieved message: {message}")
            invocation = Invocation()
            try:
                invoc_message = json.loads(message["data"])
            except TypeError:
                continue
            invocation.image = invoc_message["image"]
            invocation.infrastructure_target = invoc_message[
                "infrastructure_target"]
            invocation.stack_instance = invoc_message["stack_instance"]
            invocation.service = invoc_message["service"]
            invocation.functional_requirement = invoc_message[
                "functional_requirement"]
            invocation.tool = invoc_message["tool"]
            invocation.action = invoc_message["action"]
            logger.debug(f"invocation {invocation}")
            yield invocation
        # TODO Lets check if listen fails if the connection drops, then this place would be perfect to deregister the agent

    def ReportResult(self, automation_result: AutomationResult, context):
        logger.info(
            f"[AutomationJobDispenser] processing result {automation_result}")
        stack_instance = self.document_manager.get_stack_instance(
            automation_result.stack_instance)
        stack_instance.services[automation_result.service].status = []

        if hasattr(automation_result, 'error_message'):
            error_message = automation_result.error_message
        else:
            error_message = ""

        if hasattr(automation_result, 'status'):
            status = model.items.functional_requirement_status_model.Status(
                automation_result.status)
        else:
            status = model.items.functional_requirement_status_model.Status.READY

        fr_status = FunctionalRequirementStatus(
            functional_requirement=automation_result.functional_requirement,
            status=status,
            error_message=error_message)
        stack_instance.services[automation_result.service].status.append(
            fr_status)
        logger.info(f"[AutomationJobDispenser] done processing")
        self.document_manager.write_stack_instance(stack_instance)
        connection_result = ConnectionResult()
        connection_result.success = True
        return connection_result
