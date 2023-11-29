from neo4j import Driver
from prefect import flow, task

@task
def print_hello():
    print("Hello, Prefect!")

@flow(name="Hello", log_prints=True)
def first_flow():
    print_hello()