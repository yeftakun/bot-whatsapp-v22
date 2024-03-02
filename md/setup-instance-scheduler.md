# Start/stop EC2 instances | AWS Lambda and CloudWatch Events Scheduler

[source](https://youtu.be/kZOn46Us8WQ?si=Mzkl8EMW8YmSAyBc)

<blockquote>Nanti bakal diupdate untuk case ini</blockquote>

### Task 1: Create one Windows/Linux instance. 

### Task 2: Open the IAM service and create a role to access lambda services. 

Steps: 
- Select AWS services
- Choose lambda use case. 
- Click on permission and use two policies: AWSLambdaBasicExecutionRole (allow to use cloudwatch) and AmazonEC2Full Access. Note: You can create your policies, or you can select existing policies 
- Provide a tag. 
- Provide Role name and role description. 

### Task 3: Open Lambda services and create a new lambda function. 

Steps: 
- Provide function name. 
- Use Python as a runtime environment. 
- Go to permissions and use the created role in Task 2. 
- Now basic function code window will appear, and we need to write code for starting and stopping EC2 instances. 
 
**Code:**

> Start instance: 
```
import boto3 
region = 'us-east-2' 
instances = ['i-0f019ff0664238dcb'] 
ec2 = boto3.client('ec2', region_name=region) 

def lambda_handler(event, context): 
ec2.start_instances(InstanceIds=instances) 
print('starting your instances: ' + str(instances)) 
```
> Stop Instance: 
```
import boto3 
region = 'us-east-2' 
instances = ['i-0f019ff0664238dcb'] 
ec2 = boto3.client('ec2', region_name=region) 

def lambda_handler(event, context): 
ec2.stop_instances(InstanceIds=instances) 
print('stopped your instances: ' + str(instances)) 
```

### Task 4: Save the code. Select a test event and configure the test event. 

### Task 5: Test the EC2 events by clicking on the startEC2 event and stopEC2 event. 

### Task 6: Provide the execution details of the lambda function. 

### Task 7: Select the event bridge and click on create a rule to trigger the created lambda function. 

Steps: 
- Provide a name and description for the rule. 
- Define pattern as an event by providing Cron expression. 
- Select targets as Lambda function, provide the name of the function, and copy the JSON text from the event window. 
- Create the rule now.