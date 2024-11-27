import skyramp

# Initialize Endpoint(s)
items_endpoint = skyramp.RestEndpoint(
    name="service",
    port=8000,
    rest_path="/items"
)

# Create JSON Payload Constants

# Define Requests
items_GET_request = skyramp.Request(
    name="items_GET",
    method_name="GET",
    endpoint_descriptor=items_endpoint,
    vars_={}
)

# Define Scenarios
def add_items_functional_scenario():
    scenario = skyramp.Scenario(
        "items_functional_scenario",
        ignore=False
    )
    return scenario

def get_test_scenarios():
    scenario = skyramp.Scenario(
        "items_full_scenario"
    )
    items_functional_scenario = add_items_functional_scenario()
    scenario.add_scenario_v1(
        items_functional_scenario,
        step_name="items_full_scenario-0" ,
        description="functional scenario of /items" 
    )
    return scenario

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
    skyramp_client = skyramp.Client(kubeconfig, kubecontext, cluster_name, namespace, address)
    scenarios = get_test_scenarios()

    status = skyramp_client.tester_start(
        scenario=scenarios,
        test_name=kwargs.get("override_test_name", "items test"),
        blocked=True,
        global_vars=global_vars,
        override_code_path=override_code_path,
        skip_verify=kwargs.get("skip_verify", False),
        blobs=kwargs.get("blobs", {}),
        loadtest_config=skyramp.LoadTestConfig.from_kwargs(**kwargs),
        is_formatting_enabled=True,
        **kwargs
    )
    return status

if __name__ == "__main__":
    args = skyramp.parse_args()
    execute_tests(**args)
