from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "use_example-0206022916",
}

dag = DAG(
    "use_example-0206022916",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `use_component.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "elyra-airflow-examples-catalog", "component_ref": {"component-id": "bash_operator.py"}}

op_fddea23e_3981_4a3d_ba66_55e03872607a = BashOperator(
    task_id="bash_1",
    bash_command="for i in {11..15}; do echo $i; sleep 1; done",
    xcom_push=True,
    env={},
    output_encoding="utf-8",
    executor_config={},
    dag=dag,
)
