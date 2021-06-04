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

    tasks = []

    for metar_code in [
        'ULLI',
        'UUEE',
        'UWKD',
    ]:
        get_astronomy_task = WeatherApiOperator(
            task_id=f'get_astronomy_{metar_code.lower()}',
            metar_code=metar_code,
            conn_id='weather_api_conn_id',
            do_xcom_push=True,
        )

        insert_astronomy = PostgresOperator(
            task_id=f'insert_astronomy_{metar_code.lower()}',
            postgres_conn_id='postgres_default',
            sql='sql/insert_astronomy.sql',
            params={
                'metar_code': metar_code,
                'get_astronomy_task_id': f'get_astronomy_{metar_code.lower()}'
            }
        )

        get_astronomy_task >> insert_astronomy

        tasks.append(get_astronomy_task)

    create_table.set_downstream(tasks)


main_dag = astronomy_etl()
