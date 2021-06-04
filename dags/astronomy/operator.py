from typing import Any

from airflow.models.baseoperator import BaseOperator

from .hook import WeatherApiHook


class WeatherApiOperator(BaseOperator):
    def __init__(
            self,
            metar_code: str,
            conn_id: str = 'weather_api_conn_id',
            **kwargs) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.metar_code = metar_code

    def execute(self, context: Any):
        api = WeatherApiHook(self.conn_id)
        return api.get_astronomy(context['execution_date'].date(), self.metar_code)
