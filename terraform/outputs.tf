output "api_gateway_url" {
  value = "https://${aws_api_gateway_rest_api.api.id}.execute-api.eu-central-1.amazonaws.com/prod/"
}

output "dynamodb_table_arn" {
  value = aws_dynamodb_table.data_table.arn
}
