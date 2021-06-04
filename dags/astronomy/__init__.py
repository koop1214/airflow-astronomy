import datetime as dt

from airflow.decorators import dag
from airflow.providers.postgres.operators.postgres import PostgresOperator

# import pydevd_pycharm
# pydevd_pycharm.settrace('172.21.0.1', port=9091, stdoutToServer=True, stderrToServer=True)

from .operator import WeatherApiOperator

default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2021, 6, 1),
}


@dag(
    default_args=default_args,
    schedule_interval='@daily',
    dag_id='astronomy'
)
def astronomy_etl():
    create_table = PostgresOperator(
        task_id='create_table_task',
        sql='sql/create_table.sql',
        postgres_conn_id='postgres_default',
    )

    get_astronomy = WeatherApiOperator(
        task_id='get_astronomy',
        metar_code='ULLI',
        conn_id='weather_api_conn_id',
        do_xcom_push=True,
    )

    insert_astronomy = PostgresOperator(
        task_id='insert_astronomy',
        postgres_conn_id='postgres_default',
        sql='sql/insert_astronomy.sql',
        params={
            'metar_code': 'ULLI'
        }
    )

    create_table >> get_astronomy >> insert_astronomy


main_dag = astronomy_etl()
