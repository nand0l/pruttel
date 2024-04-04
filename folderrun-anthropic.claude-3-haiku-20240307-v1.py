import boto3
import json
import os

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name='us-east-1')

# Model and request configuration
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

def read_markdown_files(input_path, output_extension='.output.md'):
    if not os.path.isdir(input_path):
        print(f"The provided path '{input_path}' does not exist or is not a directory.")
        return

    markdown_files = [f for f in os.listdir(input_path) if f.endswith('.md')]

    for file_name in markdown_files:
        print(f"Processing file: {file_name}")
        file_path = os.path.join(input_path, file_name)
        output_file_name = os.path.splitext(file_name)[0] + output_extension
        script_folder = os.path.dirname(os.path.abspath(__file__))
        output_file_path = os.path.join(script_folder, "output", output_file_name.replace(' ',''))
        print(f"Output file path: {output_file_path}")
        print(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            prompt = file.read()
            response = bedrock.invoke_model(
                modelId=model_id,
                body=json.dumps({
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 4096,
                    "temperature": 0.99,
                    "top_p": 0.01,
                    "top_k": 0,
                    "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
                })
            )
            result = json.loads(response['body'].read())
            output_list = result.get("content", [])

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for output in output_list:
                    output_file.write(output["text"])
                # Use output_file_path to print the full path of the output file
                print(f"Output written to {output_file_path}")


input_path = "C:\\code\\Essa\\ESSA-pptx\\input.old\\Introduction into AWS"
read_markdown_files(input_path)
