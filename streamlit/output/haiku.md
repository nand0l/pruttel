Sure, here's an example of Python code to upload an image to an Amazon S3 bucket:

```python
import boto3
from botocore.exceptions import NoCredentialsError

# Set your AWS credentials
AWS_ACCESS_KEY_ID = 'your_aws_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_aws_secret_access_key'

# Set the S3 bucket name and file path
BUCKET_NAME = 'your_s3_bucket_name'
FILE_PATH = 'path/to/your/image.jpg'

# Create an S3 client
s3 = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def upload_to_aws(local_file, bucket, s3_file):
    """
    Upload a file to an S3 bucket

    :param local_file: Path to the local file
    :param bucket: Bucket to upload to
    :param s3_file: S3 file name
    :return: True if file was uploaded, else False
    """
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print(f"Upload Successful: {s3_file}")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

# Call the upload_to_aws function to upload the image
upload_to_aws(FILE_PATH, BUCKET_NAME, 'image.jpg')
```

Here's what the code does:

1. Import the necessary libraries: `boto3` for interacting with the AWS SDK, and `botocore.exceptions.NoCredentialsError` for handling the case where AWS credentials are not available.

2. Set your AWS access key ID and secret access key. You can find these in the AWS Management Console under your IAM user's security credentials.

3. Set the name of your S3 bucket and the file path of the image you want to upload.

4. Create an S3 client using `boto3.client('s3', ...)`.

5. Define a function `upload_to_aws` that takes the local file path, the S3 bucket name, and the desired S3 file name as arguments, and uploads the file to the specified S3 bucket.

6. Call the `upload_to_aws` function to upload the image to the specified S3 bucket.

Make sure to replace `'your_aws_access_key_id'`, `'your_aws_secret_access_key'`, `'your_s3_bucket_name'`, and `'path/to/your/image.jpg'` with your actual AWS credentials and file path.

Note that this example assumes you have the necessary AWS permissions to upload files to the specified S3 bucket. If you encounter any issues, make sure to check your AWS credentials and permissions.