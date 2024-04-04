import streamlit as st
import boto3
import botocore
import json
from botocore.exceptions import ClientError
import datetime
import time
import os

prompt_start = ".\\sources\\prompt-start.txt"
prompt_start = prompt_start.replace('\\', '/')

model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
model_id = "anthropic.claude-3-haiku-20240307-v1:0"


class ClaudeModelInvoker:
    def __init__(self, region_name="us-east-1"):
        """
        Initializes the invoker with an AWS region.

        :param region_name: AWS region name.
        """
        self.client = boto3.client('bedrock-runtime', region_name=region_name)

    def invoke_claude_3_with_text(self, prompt):
        """
        Invokes Anthropic Claude 3 Sonnet to run an inference using the input
        provided in the request body.

        :param prompt: The prompt that you want Claude 3 to complete.
        :return: Inference response from the model.
        """
        client = self.client
        # model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

        try:
            response = client.invoke_model(
                modelId=model_id,
                body=json.dumps({
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 2048,
                    "temperature": 0.99,
                    "top_p": 0.01,
                    "top_k": 0,
                    "messages": [{
                        "role": "user",
                        "content": [{"type": "text", "text": prompt}],
                    }],
                }),
            )

            result = json.loads(response.get("body").read())
            return result

        except ClientError as err:
            st.error(
                f"Couldn't invoke Claude 3 Sonnet. Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}"
            )
            raise

input_file_name = input("Please enter the name of the file: ")
output_file_name = os.path.basename(input_file_name)

# Read the prompt from a fixed 'prompt-start.txt' file, you need to ensure it exists or alternatively use an input box
try:
    with open(prompt_start, 'r') as file:
        prompt1 = file.read().strip()+'\n'
except FileNotFoundError:
    prompt1 = ""
    print("prompt-start.txt not found, please ensure it exists in your directory.")

if input_file_name:
    try:
        with open(input_file_name, 'r') as file:
            raw_header = file.readline().strip()
            header_text = raw_header.split('-')[1].strip()
            prompt2 = file.read().strip()+'\n</document>\n'
        prompt = prompt1 + prompt2

        if st.button('Invoke Model'):
            invoker = ClaudeModelInvoker()
            response = invoker.invoke_claude_3_with_text(prompt)
            response_text = json.dumps(
                response, indent=4)  # Pretty print the JSON

            # Saving the response to a JSON file
            with open('response.json', 'w') as f:
                f.write(response_text)

            # Assuming the structure of your JSON and writing each text content to a markdown file
            output_name = './output/'+ output_file_name
            with open(output_name, 'w') as markdown_file:
                for item in response['content']:
                    if item['type'] == 'text':
                        markdown_file.write(item['text'] + '\n\n')
            print(
                f"Model invoked successfully. Output saved to {output_name}.")
    except FileNotFoundError:
        print("The specified file was not found.")


