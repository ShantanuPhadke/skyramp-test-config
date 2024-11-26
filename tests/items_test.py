import skyramp

# Initialize Endpoint(s)
items_endpoint = skyramp.RestEndpoint(
    name="service",
    port=443,
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

def add_items_functional_scenario():
    scenario = skyramp.Scenario(
        "items_functional_scenario", ignore=False
    )

    scenario.add_request_v1(
        request=items_POST_request,
        step_name="items_functional_scenario-0",
        description="Endpoint /v1/items and Method POST"
    )

    scenario.add_assert_v1(
        assert_value="requests.items_POST.code",
        assert_expected_value="201",
        assert_step_name="items_functional_scenario-1",
        description="Asset of scenario step items_functional_scenario-0 - Endpoint /items and Method POST"
    )

    return scenario

def execute_tests(address="localhost:35142", global_vars={}, **kwargs):
    docker_client = skyramp.DockerClient()
    scenarios = [add_items_functional_scenario()]

    status = docker_client.tester_start_v1(
        scenario=scenarios, test_name="items test", address=address, blocked=True,
        global_vars=global_vars, override_code_path=kwargs.get("override_code_path", None),
        skip_verify=kwargs.get("skip_verify", False), blobs=kwargs.get("duration", None),
        at_once=kwargs.get("at_once", None), count=kwargs.get("count", None),
        is_formatting_enabled=True
    )

    return status

execute_tests()