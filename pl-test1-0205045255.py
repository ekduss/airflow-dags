from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "pl-test1-0205045255",
}

dag = DAG(
    "pl-test1-0205045255",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `untitled.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "elyra-airflow-examples-catalog", "component_ref": {"component-id": "bash_operator.py"}}

op_c86b1529_42c6_48e0_905e_49bef0f89226 = BashOperator(
    task_id="bash_dy",
    bash_command="cat /etc/hosts && echo $TEST_ENV",
    xcom_push=True,
    env={"TEST_ENV": "Hello World dayeon"},
    output_encoding="utf-8",
    executor_config={},
    dag=dag,
)
