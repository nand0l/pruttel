Sure, here's an example Python code to upload an image to an Amazon S3 bucket:

```python
import boto3
from botocore.exceptions import NoCredentialsError

# Replace these with your own values
AWS_ACCESS_KEY_ID = 'your_aws_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_aws_secret_access_key'
BUCKET_NAME = 'your_bucket_name'
FILE_PATH = 'path/to/your/image.jpg'
S3_KEY = 'images/image.jpg'  # the key (filename) to be used in the S3 bucket

# Create an S3 client
s3 = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Upload the file to S3
try:
    s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)
    print(f"File '{FILE_PATH}' uploaded to S3 bucket '{BUCKET_NAME}' with key '{S3_KEY}'")
except FileNotFoundError:
    print(f"Error: The file '{FILE_PATH}' was not found.")
except NoCredentialsError:
    print("Error: AWS credentials not available.")
except Exception as e:
    print(f"Error uploading file: {str(e)}")
```

Here's what the code does:

1. Import the necessary modules: `boto3` for the AWS SDK for Python, and `NoCredentialsError` from `botocore.exceptions`.
2. Set the necessary variables:
   - `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
   - `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
   - `BUCKET_NAME`: The name of your S3 bucket.
   - `FILE_PATH`: The path to the image file you want to upload.
   - `S3_KEY`: The key (filename) to be used for the uploaded file in the S3 bucket.
3. Create an S3 client using the `boto3.client()` function, passing in the necessary AWS credentials.
4. Use the `upload_file()` method of the S3 client to upload the file to the S3 bucket. The method takes three arguments: the local file path, the bucket name, and the S3 key.
5. Handle any exceptions that may occur during the upload process, such as the file not being found or the AWS credentials not being available.

To use this code, you'll need to replace the placeholders (`your_aws_access_key_id`, `your_aws_secret_access_key`, `your_bucket_name`, `path/to/your/image.jpg`, and `images/image.jpg`) with your actual values.

Make sure that you have the necessary AWS credentials (access key ID and secret access key) and that the IAM user associated with these credentials has the required permissions to upload files to the specified S3 bucket.