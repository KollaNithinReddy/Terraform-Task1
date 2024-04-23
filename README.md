
# SQS-LAMBDA-S3

created a sample application that reads a message
from an SQS queue using a Lambda function
and then puts the message as a JSON object in an S3 bucket

 ## Introduction
    1.Amazon SQS (Simple Queue Service):Amazon SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.
    In this application, we utilize SQS as the message queue, where messages are stored and processed by a consumer.
    2.AWS Lambda:AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers.
    In this application, Lambda functions are triggered automatically whenever a new message is available in the SQS queue and processes them, and then uploads them as JSON objects to an S3 bucket.
    3.Amazon S3 (Simple Storage Service):Amazon S3 is an object storage service.In this application,we used it to store messages in the form of JSON objects.
### Workflow
    1.Messages are sent to an SQS queue
    2.When a new message is detected in SQS queue, the Lambda function is triggered automatically.
    3.The Lambda function retrieves the message from the SQS queue, processes it, and converts it into a JSON object.
    4.The processed message, is uploaded to an S3 bucket for storage.




## Installation



#### AWS Toolkit:
To install the AWS Toolkit for Visual Studio, follow these steps:

    1.Open Visual Studio: Launch Visual Studio on your computer.
    2.Open Extensions: Go to the "Extensions" menu at the top of Visual Studio and select "Manage Extensions."
    3.Search for AWS Toolkit: In the Extensions window, search for "AWS Toolkit" using the search bar at the top right corner.
    4.Install AWS Toolkit: Find the AWS Toolkit for Visual Studio in the search results and click the "Download" button next to it.
    5.Follow Installation Steps: Follow the prompts to complete the installation process. 
    You may need to restart Visual Studio after the installation is complete.
    6.Configure AWS Credentials: Once the toolkit is installed, you'll need to configure your AWS credentials in Visual Studio. Go to the "AWS Explorer" window, 
    which should now be available in Visual Studio after installing the toolkit. Follow the prompts to enter your AWS Access Key ID and Secret Access Key.

#### AWS Command Line Interface (CLI):
    1.Visit the AWS CLI documentation page and download AWS CLI 
    2.Verify AWS CLI Installation:open a command prompt and run "aws --version"
    3.Configure AWS CLI:Enter the command "aws configure" in the command prompt.
    Enter your AWS Access Key ID and Secret Access Key when prompted. These credentials belong to an IAM user.Enter the AWS region
#### Terraform:
    1.Visit the Terraform download page,Download the Terraform for Windows.Terraform is distributed as a zip archive.
    2.Extract the contents of the zip archive to a directory of your choice
    3.Right-click on the "Start" button and select "System", click on "Advanced system settings",click the "Edit" button,
    Click the "New" button and add the path to the directory where Terraform is installed,
    Click the "New" button and add the path to the directory where Terraform is installed
    4.Verify the Installation:Open a new command prompt window
    5.Run the following command to verify that Terraform is installed and accessible from the command prompt:"terraform version",
    you should see the version number displayed in the command prompt.
### AWS Account
    1.sign up for aws Account
    2.Create a New IAM User
    3.After creating the user, you'll be presented with the user's access key ID and secret access key.Add these credentials to vs.net
   



## Documentation
#### Manual Inplementation
    1.Sign in to the AWS Management Console as IAM user
    2.In the Simple Queue Service (SQS)  dashboard, click on the "Create Queue" button,Enter a name for queue.
    3.In the S3 (Simple Storage Service) bucket dashboard, click on the "Create bucket" button.
    Enter a unique name for your bucket. Bucket names must be globally unique across all of AWS.
- Go to Vs.net select the the template ,AWS Lambda Poject and click on next ,enter a name for lambda function,click on create and choose "Simple SQS Function" as blue print
- publish the code to AWS Lambda

##### To add a trigger to an AWS Lambda function that is invoked by an SQS (Simple Queue Service) queue, follow these steps
    1.Select the Lambda Function: Click on the Lambda function to which you want to add the SQS trigger.
    2.In the Lambda function's configuration page, scroll down to the "Add triggers" section.Click on the "Add trigger" button.
    3.Select "SQS" from the list of trigger types and select the queue to add trigger.
    4.Click "Add" to add the SQS trigger to your Lambda function.
    5.click "Save" to apply the changes to your Lambda function.
- Process the received messages from SQS into JSON object.
- Use the "put_object" to upload the JSON data to the S3 bucket

### IAC(Terraform)
    1.provider:A provider is responsible for managing the interaction between Terraform and a specific service provider.In this application we use "aws provider"
    2.SQS Resource:Use "aws_sqs_queue" to create SQS resource and configure vatious properties of the SQS queue according to your requirements
    3.AWS Lambda:Use "aws_lambda_function" to create Lambda resource.
    The elements that need to be defines in the lambda file are aws_iam_role,aws_iam_policy,aws_iam_role_policy_attachment,data "archive_file",aws_lambda_function.
    4.Mapping:For mapping sqs queue and lambda,we use "aws_lambda_event_source_mapping" resource
    5.S3 (Simple Storage Service):use "aws_s3_bucket" resource to create s3 bucket.

- Lambda function code has "lambda_handler" and it has 2 parameters event and context.archive_file is used to zip this code and then this zip file is uploaded to the aws

#### IAM Roles
IAM roles and permissions for the Lambda function to access SQS and S3 are 

    1.SQS queue:ReceiveMessage.
    2.S3:GetObject,PutObject.
    3.Logs:CreateLogGroup,CreateLogStream,PutLogEvents.



## Execution

#### Use  AWS CLI to send a test message to the SQS queue
- Open command promt and enter the below command to send message to queue
```bash
    aws sqs send-message --queue-url "QUEUE_URL" --message-body "This is a test message"

```
To deploy this project run the below commands in the terminal

```bash
  terraform init
  terraform apply
```

