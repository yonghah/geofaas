import aws_cdk as core
import aws_cdk.assertions as assertions

from geofaas.geofaas_stack import GeofaasStack

# example tests. To run these tests, uncomment this file along with the example
# resource in geofaas/geofaas_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = GeofaasStack(app, "geofaas")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
