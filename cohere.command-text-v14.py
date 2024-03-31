import boto3
import json
import os 

# set the output file name
output_file=os.path.splitext(os.path.basename(__file__))[0]+'.md'

bedrock = boto3.client(
  service_name='bedrock-runtime', 
  region_name="us-east-1"
)

#prompt = """Write a medium blog post on how to use Amazon Bedrock to write an article on how to use Bedrock."""
prompt = """Write python code for uploading the image to Amazon S3 bucket. Certainly! Here's an example of python code to upload an image to Amazon S3 bucket:...."""

body = json.dumps({
    "prompt": prompt,
    "max_tokens": 1000,
    "temperature": 0.75,
    "p": 0.01,
    "k": 0,
})

modelId = 'cohere.command-text-v14'
accept = 'application/json'
contentType = 'application/json'

response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

response_body = json.loads(response.get('body').read())

content_text=(response_body['generations'][0]['text'])
print(content_text)
with open(output_file, 'w') as file:
    file.write(content_text)