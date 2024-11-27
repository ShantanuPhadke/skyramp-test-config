import skyramp

items_endpoint = skyramp.RestEndpoint(
    name="service",
    port=8000,
    rest_path="/items/"
)

items_request_data = r'''{
    "name": "Sample Item 1",
    "price": 10.0,
    "description": "Sample item 1 description."
}'''

items_POST_request = skyramp.Request(
    name="items_POST",
    method_name="POST",
    endpoint_descriptor=items_endpoint,
    vars_={},
    blob=items_request_data
)

#Define scenarios
def add_items_performance_scenario():
    scenario = skyramp.Scenario(
        "items_functional_scenario",
        ignore=False,
        vars_={"token":"_token"}
    )
    # Endpoint /v1/artists and Method POST
    scenario.add_request_v1(
        request=items_POST_request,
        step_name="items_performance_scenario-0",
        vars_override={},
        description="Endpoint /v1/items and Method POST"
    )
    # Assert of scenario step artists_functional_scenario-0 - Endpoint /v1/artists and Method POST
    scenario.add_assert_v1(
        assert_value="requests.items_POST.code",
        assert_expected_value="201", 
        assert_step_name="items_functional_scenario-1",
        description="Assert of scenario step items_performance_scenario-0 - Endpoint /v1/items and Method POST"
    )
    return scenario
    
def get_test_scenarios():
    scenario = skyramp.Scenario(
        "items_full_scenario",
        ignore=True,
        vars_={"token":"globalVars.token"},
        headers={"X-API-Key":"vars.token"}
    )
    artists_performance_scenario = add_items_performance_scenario()
    scenario.add_scenario_v1(
        artists_performance_scenario,
        step_name="items_full_scenario-0" ,
        description="performance scenario of /v1/items" ,
        vars_override={"token":"vars.token"}
    )
    return scenario
    
def execute_tests(
    address="localhost:35142",
    override_code_path=None,
    global_vars={"token":"defaultValue"},
    **kwargs
):
    docker_client = skyramp.DockerClient()
    scenarios = get_test_scenarios()
    status = docker_client.tester_start_v1(
        scenario=scenarios,
        test_name="items test",
        address=address,
        blocked=True,
        global_vars=global_vars,
        override_code_path=override_code_path, 
        skip_verify=kwargs.get("skip_verify", False),
        blobs=kwargs.get("blobs", {}), 
        loadtest_config=skyramp.LoadTestConfig(
            target_rps=1000,
            at_once=2,
            duration=10,
            rampup_interval=1,
            rampup_duration=5,
            stop_on_failure=True
        )
    )
    return status

if __name__ == "__main__":
    args = skyramp.parse_args()
    execute_tests(**args)