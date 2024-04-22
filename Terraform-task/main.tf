module "sqs"{
    source="./modules/sqs"
    queue_name="Task-Queue"
    lambda_function_name=module.lambda.lambda_arn

}
module "lambda"{
    source="./modules/lambda"
    function_name="process_sqs_s3"
    
}
module "s3"{
    source="./modules/s3"
    bucket_name="s3-bucket-terr"
}