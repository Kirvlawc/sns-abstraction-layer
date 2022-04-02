# sns-abstraction-layer

This project was built to provide a layer of abstraction over of the AWS SNS service. It provides wrapper for SNS client
along  with an abstract class for notifications. Together they should allow the developer to build notification classes that
are specific to certain uses cases and in turn provide a less clunky way to send out push notifications.

## Table of contents

  - [Requirements](#requirements-heavy_check_mark)
  - [Build the application](#build-the-application-wrench)
  - [Deploy the application](#deploy-the-application-rocket)
  - [Cleanup](#cleanup-broom)

## Requirements :heavy_check_mark:
The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Python 3 - [Install Python 3](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

## Build the application :wrench:

To build the application, run the following command:

```bash
sam build --use-container
```
This command builds the source code of the application.

## Deploy the application :rocket:

To deploy your application, run the following in your shell:

```bash
sam deploy --guided
```
The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

## Cleanup :broom:

To delete the cloud formation stack that you created, use the AWS CLI. Assuming you used `WebhookAPI` as the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name WebhookAPI
```
