import logging

from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults

log = logging.getLogger(__name__)

class MyFirstOperator(BaseOperator):
    @apply_defaults
    def __init__(self, my_operator_params, *args, **kwargs):
        self.operator_param = my_operator_params
        super(MyFirstOperator, self).__init__(*args, **kwargs)

    def excute(self, context):
        log.info("Hello World")
        log.info("operator_param: %s", self.operator_param)


class MyFirstPlugin(AirflowPlugin):
    name = 'my_first_plugin'
    operators = [MyFirstOperator]