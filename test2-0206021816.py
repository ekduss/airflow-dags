from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "test2-0206021816",
}

dag = DAG(
    "test2-0206021816",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `test2.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "elyra-airflow-examples-catalog", "component_ref": {"component-id": "bash_operator.py"}}

op_e5fbaa1b_2669_4c4f_b91e_641eadc585ec = BashOperator(
    task_id="bash_operator",
    bash_command="for i in {11..15}; do echo $i; sleep 1; done",
    xcom_push=True,
    env={},
    output_encoding="utf-8",
    executor_config={},
    dag=dag,
)
