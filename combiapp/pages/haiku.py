import streamlit as st
import boto3
import json
import os
# Set the output file name

# Set the output file path
# Set the output directory
output_dir = './output'
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(__file__))[0] + '.md')

def invoke_bedrock_model(prompt):
    # Initialize the Bedrock client
    bedrock = boto3.client(service_name="bedrock-runtime", region_name='us-east-1')
    
    # Model and request configuration
    model_id = "anthropic.claude-3-haiku-20240307-v1:0"
    accept = "application/json"
    content_type = "application/json"
    
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
    return result

def main():
    # Create the output directory if it doesn't exist
    output_dir = './output'
    os.makedirs(output_dir, exist_ok=True)
    
    # Streamlit UI
    st.title('Invoke Bedrock Model')
    prompt = st.text_input("Enter prompt:", "Write python code for uploading the image to Amazon S3 bucket. Certainly! Here's an example of python code to upload an image to Amazon S3 bucket:....")
    
    if st.button('Invoke Model'):
        result = invoke_bedrock_model(prompt)
        
        # Process the response
        input_tokens = result["usage"]["input_tokens"]
        output_tokens = result["usage"]["output_tokens"]
        output_list = result.get("content", [])
        
        # Display the invocation details
        st.write("Invocation details:")
        st.write(f"- The input length is {input_tokens} tokens.")
        st.write(f"- The output length is {output_tokens} tokens.")
        st.write(f"- The model returned {len(output_list)} response(s):")
        
        # Write the output to the file and display
        with open(output_file, 'w') as file:
            for output in output_list:
                file.write(output["text"])
                st.write(output["text"])

if __name__ == '__main__':
    main()
