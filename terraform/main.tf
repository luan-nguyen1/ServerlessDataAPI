resource "aws_dynamodb_table" "data_table" {
  name         = var.dynamodb_table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

resource "aws_s3_bucket" "serverless_bucket" {
  provider = aws.eu
  bucket   = var.s3_bucket_name

  tags = {
    Name = "Serverless Storage Bucket"
  }
}
