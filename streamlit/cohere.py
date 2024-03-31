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
    bedrock = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")
    
    # Define the body parameters
    body = json.dumps({
        "prompt": prompt,
        "max_tokens": 1000,
        "temperature": 0.75,
        "p": 0.01,
        "k": 0,
    })
    
    # Define the model ID and content types
    model_id = 'cohere.command-text-v14'
    accept = 'application/json'
    content_type = 'application/json'
    
    # Invoke the model for inference
    response = bedrock.invoke_model(body=body, modelId=model_id, accept=accept, contentType=content_type)
    
    # Retrieve the inference response
    response_body = json.loads(response.get('body').read())
    content_text = response_body['generations'][0]['text']
    
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
