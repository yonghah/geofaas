from aws_cdk import (
    Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_ecr as ecr,
)
from constructs import Construct

class GeofaasStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repo = ecr.Repository.from_repository_name(
            self, "Repository", 
            repository_name="geofaas")
        
        hello_lambda = _lambda.DockerImageFunction(
            self, "ECRFunction",
            code=_lambda.DockerImageCode.from_ecr(repo), 
            architecture=_lambda.Architecture.ARM_64,  #type: ignore
            timeout=Duration.seconds(900),
            memory_size=256
        )
       
