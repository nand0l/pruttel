import streamlit as st
import boto3
import json
import os

# Set the output directory
output_dir = './output'
os.makedirs(output_dir, exist_ok=True)

# Set the output file path
output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(__file__))[0] + '.md')

def invoke_bedrock_model(prompt):
    # Create a Boto3 client for Bedrock Runtime
    client = boto3.client('bedrock-runtime', region_name="us-east-1")

    # Define the input data and model ID
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
    content_text = json.loads(inference_result)['content'][0]['text']
    
    return content_text

def main():
    # Streamlit UI
    st.title('Invoke Bedrock Model')
    prompt = st.text_input("Enter prompt:", "Write python code for uploading the image to Amazon S3 bucket. Certainly! Here's an example of python code to upload an image to Amazon S3 bucket:....")
    
    if st.button('Invoke Model'):
        content_text = invoke_bedrock_model(prompt)
        
        # Display the output
        st.write(content_text)

        # Write the output to the file
        with open(output_file, 'w') as file:
            file.write(content_text)

if __name__ == '__main__':
    main()
