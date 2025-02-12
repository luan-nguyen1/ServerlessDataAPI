# ServerlessDataAPI
A fully **serverless** API using AWS Lambda, API Gateway, and DynamoDB. Infrastructure is managed using **Terraform** for repeatability and scalability.

## 📌 Overview
This project provides an **event-driven, serverless backend** for storing and retrieving data using AWS services. It demonstrates:
- **Infrastructure as Code (IaC)** with Terraform
- **API Gateway integration** for routing requests
- **AWS security best practices** for least privilege access


## ⚡ Tech Stack
- **AWS Lambda** (Python)
- **AWS API Gateway**
- **DynamoDB** (NoSQL)
- **Terraform** (Infrastructure as Code)
- **AWS CloudWatch** (Logging & Monitoring)


## 📂 Architecture

Client → API Gateway → Lambda → DynamoDB

- **API Gateway** handles HTTP requests.
- **Lambda** processes the request and interacts with **DynamoDB**.
- **Terraform** provisions all infrastructure as code.

## 🚀 Deployment Guide

### Prerequisites
- **AWS CLI** installed and configured  
- **Terraform** installed (`terraform -v`)  
- **Git** installed (`git --version`)  

### Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/ServerlessDataAPI.git
cd ServerlessDataAPI
```
### Deploy Using Terraform
```bash
cd terraform
terraform init
terraform apply -auto-approve
```
---

## 🔍 Testing the API
## Store Data
```bash
curl -X POST "https://YOUR_API_ID.execute-api.eu-central-1.amazonaws.com/prod/" \
     -H "Content-Type: application/json" \
     -d '{"id": "123", "name": "Luan"}'
```
## Retrieve Data

```bash
curl -X GET "https://YOUR_API_ID.execute-api.eu-central-1.amazonaws.com/prod/?id=123"
```

---

## 🔧 Features
- Fully Serverless – No need for EC2 or manual infrastructure
- Infrastructure as Code – Terraform ensures reproducibility
- Scalable – Uses API Gateway and DynamoDB for serverless scaling
- Secure – Uses IAM roles for least privilege access

## 🛠 Development Guide
## 🔹 1. Modify Lambda Code
- Zip and redeploy:
```bash
cd lambda
zip lambda_function.zip lambda_function.py
aws lambda update-function-code --function-name serverless_api_lambda \
    --zip-file fileb://lambda_function.zip --region eu-central-1
```
## 🔹 2. Debugging
Check logs:
```bash
aws logs tail /aws/lambda/serverless_api_lambda --region eu-central-1 --format short
```
📌 Next Steps
 Add Authentication (Cognito, API Keys)
 Implement CI/CD using GitHub Actions
 Optimize Terraform Modules
 
📝 Lessons Learned
🔗 Read the full technical breakdown on Medium (Link to be added after the blog post is written.)
