import streamlit as st
import boto3
import json
import os
import datetime
import time
from botocore.exceptions import ClientError

# Set the output directory and create it if it doesn't exist
output_dir = './output'
os.makedirs(output_dir, exist_ok=True)

prompt_start = './prompt-start.txt'


class ClaudeModelInvoker:
    def __init__(self, region_name="us-east-1"):
        """
        Initializes the invoker with an AWS region.
        :param region_name: AWS region name.
        """
        self.client = boto3.client('bedrock-runtime', region_name=region_name)

    def invoke_model(self, model_id, body):
        """
        Invokes the specified Bedrock model with the given body.
        :param model_id: Model ID to invoke.
        :param body: Request body for the model invocation.
        :return: The response from the model.
        """
        try:
            response = self.client.invoke_model(
                modelId=model_id,
                body=json.dumps(body),
                contentType='application/json'
            )
            result = json.loads(response.get("body").read())
            return result
        except ClientError as err:
            st.error(
                f"Couldn't invoke the model. Here's why: {err.response['Error']['Code']}: {err.response['Error']['Message']}"
            )
            raise


def main():
    st.title('Invoke Bedrock Model with Streamlit and File Input')

    version = st.selectbox('Choose model version:',
                           ('Cohere', 'Haiku', 'Sonnet'))
    input_file_name = st.text_input('Enter the path to your input file:', '')

    if st.button('Invoke Model') and input_file_name:
        try:
            with open(prompt_start, 'r') as file:
                prompt1 = file.read().strip()

            with open(input_file_name, 'r') as file:
                prompt2 = file.read().strip()
            lines = prompt2.splitlines()
            header_text = next((line.strip() for line in lines if line.strip()), None)
            header_text= header_text.replace(" ", "").replace("#", "")
            prompt = prompt1+'\n\n'+prompt2
            # st.write(prompt)
            invoker = ClaudeModelInvoker()
            model_id, body = '', {}

            if version == 'Cohere':
                client = boto3.client(
                    'bedrock-runtime', region_name='us-east-1')
                model_id = 'cohere.command-text-v14'
                accept = 'application/json'
                content_type = 'application/json'
                body = {
                    "prompt": prompt,
                    "max_tokens": 1000,
                    "temperature": 0.75,
                    "p": 0.01,
                    "k": 0
                }
                response = client.invoke_model(
                    body=body, modelId=model_id, accept=accept, contentType=content_type)

                # Retrieve the inference response
                response_body = json.loads(response.get('body').read())
                content_text = response_body['generations'][0]['text']

                return content_text
            elif version == 'Sonnet' or version == 'Haiku':
                model_id = 'anthropic.claude-3-sonnet-20240229-v1:0' if version == 'Sonnet' else "anthropic.claude-3-haiku-20240307-v1:0"
                body = {
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 4096,  # if version == 'Sonnet' else 1024,
                    "temperature": 0.99,
                    "top_p": 0.01,
                    "top_k": 0,
                    "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
                }

            response = invoker.invoke_model(model_id, body)

            # Processing and displaying the response
            if version == 'Haiku':
                for content in response.get("content", []):
                    output_text = (content["text"])
            else:
                output_text = (response['content'][0]['text'])
            st.write(output_text)
            # Optionally, save the response to a file
            timestamp = time.mktime(datetime.datetime.now().timetuple())
            output_file = os.path.join(
                output_dir, f'{version}-{header_text}.md')
            with open(output_file, 'w') as file:
                file.write(output_text)
            st.success(
                f"Model invoked successfully. Output saved to {output_file}.")

        except FileNotFoundError:
            st.error("The specified file was not found.")


if __name__ == '__main__':
    main()
