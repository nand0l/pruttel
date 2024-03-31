import boto3
import json
import os

# Set the output file name
output_file = os.path.splitext(os.path.basename(__file__))[0] + '.md'

# Create a Boto3 client for Bedrock Runtime
client = boto3.client('bedrock-runtime', region_name="us-east-1")

# Define the prompt and other parameters
prompt = """Write python code for uploading the image to Amazon S3 bucket. Certainly! Here's an example of python code to upload an image to Amazon S3 bucket:...."""
input_data = {
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt.replace("\n", "\\n")
                }
            ]
        }
    ],
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 2000
}
model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'

# Convert input data to JSON string
input_data_json = json.dumps(input_data)

# Invoke the model for inference
response = client.invoke_model(contentType='application/json', body=input_data_json, modelId=model_id)

# Retrieve the inference response
inference_result = response['body'].read().decode('utf-8')

# Process the inference result
print(inference_result)
content_text = json.loads(inference_result)['content'][0]['text']
print(content_text)

# Write the output to the file
with open(output_file, 'w') as file:
    file.write(content_text)
