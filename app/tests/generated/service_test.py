import skyramp
from tests import (
    items_test,
)

global_vars={}

failure_list = []
def execute_tests(
    address="",
    override_code_path=None,
    global_vars={},
    namespace="",
    kubeconfig="",
    kubecontext="", 
    cluster_name="",
    **kwargs
):
    status_list = []
    status = None
    status=items_test.execute_tests(
            address=address,
            override_code_path=override_code_path,
            global_vars=global_vars,
            namespace=namespace,
            kubeconfig=kubeconfig,
            kubecontext=kubecontext,
            cluster_name=cluster_name,
            **kwargs
    )
    status_list.extend(status)
    print_test_status(test_name="items", status=status)
    return status_list

def print_test_status(test_name, status):
    if status.passed():
        print(f"Test case { test_name } passed")
    else:
        print(f"Test case { test_name } failed : { status.failed() }")
        failure_list.append(status.failed())

if __name__ == "__main__":
    args = skyramp.parse_args()
    status = execute_tests(**args)
    if len(failure_list) > 0:
        print(f"Some test cases failed : {failure_list}")
        exit(1)
    else:
        print("All test cases passed")
        exit(0)
