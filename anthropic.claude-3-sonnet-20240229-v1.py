import boto3
# Create a Boto3 client for Bedrock Runtime

client = boto3.client('bedrock-runtime',region_name="us-east-1")

# Specify the input data and model ID
input_data = "{\"messages\":[{\"role\":\"user\",\"content\":[{\"type\":\"text\",\"text\":\"Write python code for uploading the image to Amazon S3 bucket\\nCertainly! Here's an example of python code to upload an image to Amazon S3 bucket:\\n\\n....\"}]}],\"anthropic_version\":\"bedrock-2023-05-31\",\"max_tokens\":2000}"

model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'

# Invoke the model for inference
response = client.invoke_model(contentType='application/json', body=input_data, modelId=model_id)

# Retrieve the inference response
inference_result = response['body'].read().decode('utf-8')

# Process the inference result
print(inference_result)