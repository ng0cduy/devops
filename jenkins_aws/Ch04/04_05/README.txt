Enter the following script into an Execute Shell build step to deploy your
elastic beanstalk application:

#!/bin/bash -xe

APPLICATION=YOUR_APPLICATION_NAME_HERE
REGION=YOUR_REGION_NAME_HERE
ENVIRONMENT=YOUR_ENVIRONMENT_NAME_HERE
PLATFORM=YOUR_PLATFORM_HERE

# confirm the role being used
aws sts get-caller-identity

# intialize the application
eb init "${APPLICATION}" --platform "${PLATFORM}"  --region "${REGION}"

# select the environment
eb use "${ENVIRONMENT}"

# deploy the application
eb deploy

# get the deployment's health and status information
eb health
eb status