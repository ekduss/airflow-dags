from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "test-0206032706",
}

dag = DAG(
    "test-0206032706",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `test.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "url-catalog", "component_ref": {"url": "https://raw.githubusercontent.com/elyra-ai/examples/main/pipelines/run-pipelines-on-apache-airflow/components/bash_operator.py"}}

op_a97f8e4c_8879_4bc3_9825_7ede96f1b975 = BashOperator(
    task_id="BashOperator",
    bash_command="echo 'hi dayeon'",
    do_xcom_push=False,
    env={},
    output_encoding="utf-8",
    executor_config={},
    dag=dag,
)
