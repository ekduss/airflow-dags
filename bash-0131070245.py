from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "bash-0131070245",
}

dag = DAG(
    "bash-0131070245",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `bash.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "elyra-airflow-examples-catalog", "component_ref": {"component-id": "bash_operator.py"}}

op_f4600df6_e529_4542_9562_7f5a1c61d97d = BashOperator(
    task_id="bbash",
    bash_command="cat /etc/hosts && echo $TEST_ENV",
    xcom_push=True,
    env={"TEST_ENV": "Hello World dayeon"},
    output_encoding="utf-8",
    executor_config={},
    dag=dag,
)
