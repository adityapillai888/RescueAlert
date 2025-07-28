#!/bin/bash

set -e  # Stop if any command fails

echo "Building Lambda functions..."
sam build --template-file infra/template.yaml

echo "Deploying to AWS..."
sam deploy \
  --template-file .aws-sam/build/template.yaml \
  --stack-name contact-system-stack \
  --capabilities CAPABILITY_IAM \
  --region ap-south-1 \
  --no-fail-on-empty-changeset \
  --resolve-s3
echo "Deployment completed successfully."