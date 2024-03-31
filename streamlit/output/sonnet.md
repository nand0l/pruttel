Sure, here's an example Python code to upload an image to an Amazon S3 bucket:

```python
import boto3
from botocore.exceptions import NoCredentialsError

# Replace with your AWS access key and secret access key
AWS_ACCESS_KEY_ID = 'your_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'

# Replace with the name of your S3 bucket
BUCKET_NAME = 'your_bucket_name'

# Replace with the path to your local image file
IMAGE_FILE_PATH = '/path/to/your/image/file.jpg'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

try:
    # Upload the image file to the S3 bucket
    s3.upload_file(IMAGE_FILE_PATH, BUCKET_NAME, 'uploaded_image.jpg')
    print('Image uploaded successfully!')
except NoCredentialsError:
    print('Credentials not available.')
except Exception as e:
    print('Error uploading image:', str(e))
```

Here's how the code works:

1. Import the necessary libraries: `boto3` for interacting with Amazon S3, and `NoCredentialsError` from `botocore.exceptions` to handle credential-related exceptions.

2. Set your AWS access key ID and secret access key. You can obtain these credentials from the AWS Management Console.

3. Set the name of your S3 bucket where you want to upload the image.

4. Set the path to your local image file that you want to upload.

5. Create an S3 client using `boto3.client('s3')` and passing your AWS credentials.

6. Use the `upload_file` method of the S3 client to upload the local image file to the S3 bucket. This method takes three arguments:
   - The path to your local image file (`IMAGE_FILE_PATH`)
   - The name of your S3 bucket (`BUCKET_NAME`)
   - The desired name for the uploaded file in the S3 bucket (`'uploaded_image.jpg'` in this case)

7. Handle exceptions:
   - If no AWS credentials are available, the `NoCredentialsError` exception is raised.
   - If any other exception occurs during the upload process, it is caught and printed.

Make sure to replace the placeholders (`'your_access_key_id'`, `'your_secret_access_key'`, `'your_bucket_name'`, and `'/path/to/your/image/file.jpg'`) with your actual AWS credentials, bucket name, and the path to your local image file, respectively.

Note: This code assumes that you have the necessary permissions to upload files to the specified S3 bucket. Also, ensure that you have the `boto3` library installed (`pip install boto3`) before running the code.