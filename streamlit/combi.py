import streamlit as st
import boto3
import json
import os

# Set the output directory and create it if it doesn't exist
output_dir = './output'
os.makedirs(output_dir, exist_ok=True)

def invoke_bedrock_model(version, prompt):
    client = boto3.client('bedrock-runtime', region_name="us-east-1")

    if version == 'Cohere':
            # Create a Boto3 client for Bedrock Runtime
    #bedrock = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")
    
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
        response = client.invoke_model(body=body, modelId=model_id, accept=accept, contentType=content_type)
        
        # Retrieve the inference response
        response_body = json.loads(response.get('body').read())
        content_text = response_body['generations'][0]['text']
        
        return content_text
    elif version == 'Sonnet':
        # Model configuration for Sonnet
        model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
        input_data = {
            "messages": [{"role": "user", "content": [{"type": "text", "text": prompt.replace("\n", "\\n")}]}],
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 2000
        }
        body = json.dumps(input_data)
    elif version == 'Haiku':
        # Model configuration for Haiku
        model_id = "anthropic.claude-3-haiku-20240307-v1:0"
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
        })
    
    response = client.invoke_model(contentType='application/json', body=body, modelId=model_id)
    result = json.loads(response['body'].read())

    # Processing response differently for Haiku because of its different response structure
    if version == 'Haiku':
        return result.get("content", [])
    else:
        return result['content'][0]['text']

def main():
    st.title('Invoke Bedrock Model with Selection')
    version = st.selectbox('Choose model version:', ('Cohere', 'Haiku', 'Sonnet'))
    prompt = st.text_input("Enter prompt:", "Write a Python code snippet.")

    if st.button('Invoke Model'):
        result = invoke_bedrock_model(version, prompt)

        if version == 'Haiku':
            for output in result:
                st.write(output["text"])
        else:
            st.write(result)

        # Save the result to a file
        output_file = os.path.join(output_dir, version.lower() + '.md')
        with open(output_file, 'w') as file:
            if version == 'Haiku':
                for output in result:
                    file.write(output["text"] + '\n')
            else:
                file.write(result)

if __name__ == '__main__':
    main()
