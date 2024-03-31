import boto3
import botocore
import json
import logging
from botocore.exceptions import ClientError

# importing datetime module
import datetime
import time
date_time = datetime.datetime.now()
timestamp = (time.mktime(date_time.timetuple()))
input_file_name = 'C:\\code\\Essa\\_ESSA-react\\src\\assets\\courseware.org\\Module18-WrapupandReview.md'
# input_file_name = input_file_name.replace('\', '/')
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ClaudeModelInvoker:
    def __init__(self, profile_name="default", region_name="us-east-1"):
        """
        Initializes the invoker with an AWS CLI profile and region.

        :param profile_name: Name of the AWS CLI profile to use.
        :param region_name: AWS region name.
        """
        # Using a specific profile from your AWS credentials file
        boto3.setup_default_session(profile_name=profile_name)
        self.client = boto3.client(
            'bedrock-runtime',
            region_name=region_name
        )

    def invoke_claude_3_with_text(self, prompt):
        """
        Invokes Anthropic Claude 3 Sonnet to run an inference using the input
        provided in the request body.

        :param prompt: The prompt that you want Claude 3 to complete.
        :return: Inference response from the model.
        """
        # Initialize the Amazon Bedrock runtime client if not already initialized
        client = self.client

        # Invoke Claude 3 with the text prompt
        model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

        try:
            response = client.invoke_model(
                modelId=model_id,
                body=json.dumps(
                    {
                        "anthropic_version": "bedrock-2023-05-31",
                        "max_tokens": 4096,
                        "messages": [
                            {
                                "role": "user",
                                "content": [{"type": "text", "text": prompt}],
                            }
                        ],
                    }
                ),
            )

            # Process and print the response
            result = json.loads(response.get("body").read())
            input_tokens = result["usage"]["input_tokens"]
            output_tokens = result["usage"]["output_tokens"]
            output_list = result.get("content", [])

            logger.info("Invocation details:")
            logger.info(f"- The input length is {input_tokens} tokens.")
            logger.info(f"- The output length is {output_tokens} tokens.")

            logger.info(
                f"- The model returned {len(output_list)} response(s):")
            for output in output_list:
                logger.info(output["text"])

            return result

        except ClientError as err:
            logger.error(
                "Couldn't invoke Claude 3 Sonnet. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise


# Example usage
# Note: Replace 'myprofile' with the name of your AWS CLI configured profile
invoker = ClaudeModelInvoker(profile_name='default')
# Name of the output markdown file
output_name = 'response'+str(timestamp)+'.md'

# Read the prompt from 'prompt.txt'
with open('prompt-start.txt', 'r') as file:
    # .strip() removes any leading/trailing whitespace
    prompt1 = file.read().strip()+'\n'
with open(input_file_name, 'r') as file:
    # .strip() removes any leading/trailing whitespace
    prompt2 = file.read().strip()+'\n</document>\n'
prompt = prompt1+prompt2
response = invoker.invoke_claude_3_with_text(prompt)
response_text = json.dumps(response, indent=4)  # Pretty print the JSON

# Write the JSON string to a file
with open('response.json', 'w') as f:
    f.write(response_text)

with open('response.json', 'r') as file:
    data = json.load(file)

# Assuming the structure of your JSON and that you want to write each text content to the markdown file
with open(output_name, 'w') as markdown_file:
    for item in data['content']:
        if item['type'] == 'text':
            # Adds two newlines for markdown paragraph separation
            markdown_file.write(item['text'] + '\n\n')
