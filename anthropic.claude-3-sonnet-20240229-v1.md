Sure, here's an example Python code to upload an image file to an Amazon S3 bucket:

```python
import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY_ID = 'YOUR_ACCESS_KEY_ID'
ACCESS_SECRET_KEY = 'YOUR_ACCESS_SECRET_KEY'
BUCKET_NAME = 'YOUR_BUCKET_NAME'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID,
                  aws_secret_access_key=ACCESS_SECRET_KEY)

# Specify the file to upload
file_path = 'path/to/your/image/file.jpg'

try:
    # Upload the file to S3
    s3.upload_file(file_path, BUCKET_NAME, 'path/in/s3/image.jpg')
    print('File uploaded successfully!')
except NoCredentialsError:
    print('Credentials not available.')
except Exception as e:
    print('Error occurred: ', e)
```

Here's what the code does:

1. Import the necessary modules: `boto3` (the AWS SDK for Python) and `NoCredentialsError` from `botocore.exceptions`.
2. Set your AWS credentials (`ACCESS_KEY_ID` and `ACCESS_SECRET_KEY`) and the name of your S3 bucket (`BUCKET_NAME`).
3. Create an S3 client using `boto3.client('s3')` and pass your AWS credentials.
4. Specify the file path of the image you want to upload (`file_path`).
5. Use the `s3.upload_file()` method to upload the file to your S3 bucket. This method takes three arguments:
   - The file path of the local file (`file_path`).
   - The name of the S3 bucket (`BUCKET_NAME`).
   - The desired path and file name for the uploaded file in your S3 bucket (`'path/in/s3/image.jpg'`).
6. Handle exceptions:
   - If AWS credentials are not available, it will raise a `NoCredentialsError`.
   - If any other exception occurs, it will print the error message.

Make sure to replace `'YOUR_ACCESS_KEY_ID'`, `'YOUR_ACCESS_SECRET_KEY'`, `'YOUR_BUCKET_NAME'`, and `'path/to/your/image/file.jpg'` with your actual AWS credentials, bucket name, and file path, respectively.

Note: Before running this code, you need to have the `boto3` library installed. You can install it using pip:

```
pip install boto3
```

Also, make sure you have the necessary permissions to upload files to the S3 bucket you specified.