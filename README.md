# skyramp-test-config
Sample test configuration using Skyramp's set of tools

## Written API Test Cases Feedback
(1) There should be an additional step to dockerize the current project that the user is trying to test. This step should be added in case a developer is:<br/>&nbsp(a) trying to use skyramp for a toy use case prior to integrating into their companies larger projects <br/>&nbsp(b) is part of a smaller startup OR a new team in a larger company that is getting its infra set up / has a very small project where the v1 is still being built up.

## Performance Test Cases Feedback
(1) The documentation has a slight issue where it assigns invalid integers to input variables like duration (eg duration=10s). Using just normal integers fixes the runtime issues here.

## Generated Test Cases Feedback
(1) The documentation should show what is the expected format for the sample request file. Additionally, could this step be automated?<br/>
(2) [Slight optimization] Would it be possible to automatically detect information like the worker address from the Docker YAML file itself? Reason for this is in some companies there may be multiple personas: software engineers and qa engineers. Here QA engineers may be the ones heavily interacting with skyramp but they may not know the ins and outs of Docker all the time (compared to software engineers).
