import boto3
import json
import os

# Set the output file name
output_file = os.path.splitext(os.path.basename(__file__))[0] + '.md'

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name='us-east-1')

# Model and request configuration
model_id = "anthropic.claude-3-haiku-20240307-v1:0"
accept = "application/json"
content_type = "application/json"
prompt = """Write python code for uploading the image to Amazon S3 bucket. Certainly! Here's an example of python code to upload an image to Amazon S3 bucket:...."""

# Invoke the model
response = bedrock.invoke_model(
    modelId=model_id,
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [{
            "role": "user",
            "content": [{
                "type": "text",
                "text": prompt
            }]
        }]
    })
)

# Process the response
result = json.loads(response.get("body").read())
input_tokens = result["usage"]["input_tokens"]
output_tokens = result["usage"]["output_tokens"]
output_list = result.get("content", [])

# Display the invocation details
print("Invocation details:")
print(f"- The input length is {input_tokens} tokens.")
print(f"- The output length is {output_tokens} tokens.")
print(f"- The model returned {len(output_list)} response(s):")

# Write the output to the file and print
with open(output_file, 'w') as file:
    for output in output_list:
        file.write(output["text"])
        print(output["text"])
