data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/../../python/process-sqs/process_sqs.py"
  output_path = "${path.module}/../../python/process-sqs/process_sqs.zip"
}




resource "aws_lambda_function" "test_lambda" {

  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = data.archive_file.lambda_zip.output_path
  function_name = var.function_name
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "process_sqs.lambda_handler"

  source_code_hash = data.archive_file.lambda_zip.output_base64sha256

  runtime = var.runtime

 
}