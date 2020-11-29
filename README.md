# AWS CloudFormation

## Basics

- Parameters
- Resources
- Outputs
- Mappings
- Conditions
- WaitCondition
- cfn-init
- cfn-signal
- nested stack
- DeletionPolicy

## Intrinsic functions

- Ref
- Join
- GetAtt
- Sub
- ImportValue
- FindInMap
- If
- Equals
- GetAZs
- Select
- Split
- Base64

## Deploy Python lambda function with dependencies

1 - install packages

```shell
pip install --target ./package requests
```

2 - zip packages and source code

```shell
cd package
zip -r zipped-function.zip ./*
mv zipped-function.zip ../
cd ../
zip -g zipped-function.zip index.py
```

3 - upload to S3

```shell
aws s3 cp zipped-function.zip s3://<BUCKET_NAME>/functions/
```
