from agents.planner import plan
from agents.executer import execute
from agents.verifier import verify

def main():
    print("=== AI Operations Assistant ===")
    task = input("Enter your task: ")

    plan_json = plan(task)
    print("\nPlanner Output:\n", plan_json)

    execution_result = execute(plan_json)
    print("\nExecutor Output:\n", execution_result)

    final_output = verify(execution_result)
    print("\nFinal Verified Output:\n", final_output)

if __name__ == "__main__":
    main()
