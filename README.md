ServerlessDataAPI
A fully serverless API using AWS Lambda, API Gateway, and DynamoDB. Infrastructure is managed using Terraform for repeatability and scalability.

📌 Overview
This project provides an event-driven, serverless backend for storing and retrieving data using AWS services. It demonstrates Infrastructure as Code (IaC), API Gateway integrations, and AWS security best practices.

Tech Stack
AWS Lambda (Python)
AWS API Gateway
DynamoDB (NoSQL)
Terraform (Infrastructure as Code)
AWS CloudWatch (Logging & Monitoring)
📂 Architecture
plaintext
Copy
Edit
Client → API Gateway → Lambda → DynamoDB
API Gateway handles HTTP requests.
Lambda processes the request and interacts with DynamoDB.
Terraform provisions infrastructure.
🚀 Deployment Guide
1️⃣ Prerequisites
Ensure you have:

AWS CLI configured with appropriate permissions
Terraform installed (terraform -v)
Git installed
2️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/ServerlessDataAPI.git
cd ServerlessDataAPI
3️⃣ Deploy Using Terraform
bash
Copy
Edit
cd terraform
terraform init
terraform apply -auto-approve
Note: The Terraform script provisions the Lambda function, API Gateway, DynamoDB table, and IAM roles.

4️⃣ Test API
Store Data

bash
Copy
Edit
curl -X POST "https://YOUR_API_ID.execute-api.eu-central-1.amazonaws.com/prod/" \
     -H "Content-Type: application/json" \
     -d '{"id": "123", "name": "Luan"}'
Retrieve Data

bash
Copy
Edit
curl -X GET "https://YOUR_API_ID.execute-api.eu-central-1.amazonaws.com/prod/?id=123"
🔧 Features
✅ Fully Serverless – No need for EC2 or manual infrastructure
✅ Infrastructure as Code – Terraform ensures reproducibility
✅ Scalable – Uses API Gateway and DynamoDB for serverless scaling
✅ Secure – Uses IAM roles for least privilege access

🛠 Development Guide
1️⃣ Modify Lambda Code
Edit lambda/lambda_function.py
Zip and redeploy:
bash
Copy
Edit
cd lambda
zip lambda_function.zip lambda_function.py
aws lambda update-function-code --function-name serverless_api_lambda \
    --zip-file fileb://lambda_function.zip --region eu-central-1
2️⃣ Debugging
Check logs:

bash
Copy
Edit
aws logs tail /aws/lambda/serverless_api_lambda --region eu-central-1 --format short
📌 Next Steps
[ ] Add Authentication (Cognito, API Keys)
[ ] Implement CI/CD using GitHub Actions
[ ] Optimize Terraform Modules
📝 Lessons Learned
🔗 Read the full technical breakdown on Medium (Link to be added after the blog post is written.)
