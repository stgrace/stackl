import sys


from logger import Logger
from utils.stackl_singleton import Singleton
from utils.general_utils import get_config_key

class TaskBrokerFactory(metaclass=Singleton):
    
    def __init__(self):
        self.task_broker_type = get_config_key("TASK_BROKER")
        self.logger = Logger("TaskBrokerFactory")
        self.logger.info("[TaskBrokerFactory] Creating Task Broker with type: {}".format(self.task_broker_type))
        self.task_broker = None

        if self.task_broker is not None:
            pass
        elif self.task_broker_type == "Celery":
            pass
        elif self.task_broker_type == "Custom":
            from task_broker.custom_task_broker import CustomTaskBroker
            self.task_broker = CustomTaskBroker()
        else: #assume local custom redis broker
            from task_broker.custom_task_broker import CustomTaskBroker
            self.task_broker = CustomTaskBroker()

    def get_task_broker(self):
        return self.task_broker