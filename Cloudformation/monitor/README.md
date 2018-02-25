1. Package:
> aws --profile teamzerolabs cloudformation package --template-file ./template.yaml --s3-bucket monitor-test --output-template-file packaged-template.yaml
2. Deploy:
> aws --profile teamzerolabs cloudformation deploy --template-file ./packaged-template.yaml --stack-name monitor-test-stack-1 --capabilities CAPABILITY_IAM --region us-east-1
3. Remove:
> aws --profile teamzerolabs cloudformation delete-stack --stack-name monitor-test-stack-1 --region us-east-1