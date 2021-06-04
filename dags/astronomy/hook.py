from typing import Dict

import requests
from airflow.exceptions import AirflowException
from airflow.hooks.base import BaseHook
from pendulum import Date


class WeatherApiHook(BaseHook):
    def __init__(self, weather_api_conn_id: str) -> None:
        super().__init__()
        self.api_key = self._get_api_key(weather_api_conn_id)

    def get_astronomy(self, date: Date, metar_code: str) -> Dict[str, str]:
        url = 'https://api.weatherapi.com/v1/astronomy.json'
        params = {
            'key': self.api_key,
            'dt': str(date),
            'q': f'metar:{metar_code.upper()}'
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()['astronomy']['astro']

    def _get_api_key(self, conn_id: str) -> str:
        conn = self.get_connection(conn_id)

        if not conn.password:
            raise AirflowException('Missing API key (password) in connection settings')

        return conn.password
