from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "custom-1-0205072117",
}

dag = DAG(
    "custom-1-0205072117",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `custom.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "elyra-airflow-examples-catalog", "component_ref": {"component-id": "bash_operator.py"}}

op_d12f4059_2969_4d5a_b563_c37b96823790 = BashOperator(
    task_id="custom_test",
    bash_command='from datetime import datetime, timedelta\nfrom airflow import DAG\nfrom airflow.operators.bash import BashOperator\n\ndefault_args = {\n    "owner": "airflow"\n}\n\nwith DAG(\n    dag_id="jupyter-1",\n    default_args=default_args,\n    schedule_interval="@daily",\n    start_date=datetime(2025, 2, 4),\n    catchup=False,\n    tags=["dayeon"],\n) as dag:\n\n    bb = BashOperator(\n        task_id="bash-test-1",\n        bash_command="for i in {1..10}; do echo $i; sleep 1; done"\n\n    bb',
    xcom_push=True,
    env={},
    output_encoding="utf-8",
    executor_config={},
    dag=dag,
)
