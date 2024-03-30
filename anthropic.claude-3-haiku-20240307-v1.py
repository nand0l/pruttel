import boto3
import json

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name='us-east-1')

# Model and request configuration
modelId = "anthropic.claude-3-haiku-20240307-v1:0"
accept = "application/json"
contentType = "application/json"
prompt = """If you could interview any historical figure using a time machine, who would it be and what would you ask them?"""

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
for output in output_list:
    print(output["text"])