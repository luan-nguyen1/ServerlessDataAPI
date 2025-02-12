# Automatically create ZIP for Lambda function
data "archive_file" "lambda_package" {
  type        = "zip"
  source_file = "../lambda/lambda_function.py"
  output_path = "lambda_function.zip"
}

# AWS Lambda Function
resource "aws_lambda_function" "lambda_api" {
  function_name = "serverless_api_lambda"
  runtime       = "python3.9"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "lambda_function.lambda_handler"

  filename         = data.archive_file.lambda_package.output_path
  source_code_hash = data.archive_file.lambda_package.output_base64sha256

  environment {
    variables = {
      DYNAMODB_TABLE = aws_dynamodb_table.data_table.name
    }
  }
}