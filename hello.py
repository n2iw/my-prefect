from prefect import flow, task

@task
def print_hello(who):
    print(f"Hello, {who}!")

@flow(name="Ming's test flow", log_prints=True)
def first_flow(who):
    print_hello(who)

if __name__ == "__main__":
    first_flow("Pure Python")