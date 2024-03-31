import boto3
import json
import os

# set the output file name
output_file=os.path.splitext(os.path.basename(__file__))[0]+'.md'
# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name='us-east-1')

# Model and request configuration
modelId = "anthropic.claude-3-haiku-20240307-v1:0"
accept = "application/json"
contentType = "application/json"
prompt = """
Write a medium blog post on how to use 
Amazon Bedrock to write an article on how to use Bedrock.
"""

# Invoke the model
response = bedrock.invoke_model(
    modelId=modelId,
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

with open(output_file, 'w') as file:
    for output in output_list:
        file.write(output["text"])
        print(output["text"])