import os
import boto3
from botocore.exceptions import ClientError, NoCredentialsError
from werkzeug.utils import secure_filename
from flask import current_app

class S3Handler:
    def __init__(self):
        try:
            # Log AWS configuration (without sensitive details)
            current_app.logger.info(f"Initializing S3 handler with region: {os.getenv('AWS_REGION', 'eu-north-1')}")
            current_app.logger.info(f"Using bucket: {os.getenv('AWS_BUCKET_NAME')}")
            
            if not os.getenv('AWS_ACCESS_KEY_ID'):
                current_app.logger.error("AWS_ACCESS_KEY_ID is not set")
            if not os.getenv('AWS_SECRET_ACCESS_KEY'):
                current_app.logger.error("AWS_SECRET_ACCESS_KEY is not set")
            if not os.getenv('AWS_BUCKET_NAME'):
                current_app.logger.error("AWS_BUCKET_NAME is not set")
            
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                region_name=os.getenv('AWS_REGION', 'eu-north-1')
            )
            self.bucket_name = os.getenv('AWS_BUCKET_NAME')
            
            # Verify bucket exists and is accessible
            try:
                self.s3_client.head_bucket(Bucket=self.bucket_name)
                current_app.logger.info("Successfully connected to S3 bucket")
            except ClientError as e:
                error_code = e.response['Error']['Code']
                if error_code == '404':
                    current_app.logger.error(f"Bucket {self.bucket_name} does not exist")
                elif error_code == '403':
                    current_app.logger.error(f"Permission denied accessing bucket {self.bucket_name}")
                raise
                
        except NoCredentialsError:
            current_app.logger.error("AWS credentials not found or invalid")
            raise
        except Exception as e:
            current_app.logger.error(f"Error initializing S3 handler: {str(e)}")
            raise

    def upload_file(self, file, folder=''):
        """
        Upload a file to S3 bucket
        """
        if not file:
            current_app.logger.error("No file provided for upload")
            return None
            
        try:
            # Log file details
            current_app.logger.info(f"Attempting to upload file: {file.filename}")
            current_app.logger.info(f"Content type: {file.content_type}")
            
            # Secure the filename
            filename = secure_filename(file.filename)
            
            # Create a unique filename with folder structure
            if folder:
                s3_path = f"{folder}/{filename}"
            else:
                s3_path = filename

            current_app.logger.info(f"S3 path for upload: {s3_path}")

            # Upload the file
            self.s3_client.upload_fileobj(
                file,
                self.bucket_name,
                s3_path,
                ExtraArgs={
                    'ContentType': file.content_type
                }
            )

            # Generate the URL
            url = f"https://{self.bucket_name}.s3.{os.getenv('AWS_REGION', 'eu-north-1')}.amazonaws.com/{s3_path}"
            current_app.logger.info(f"File successfully uploaded. URL: {url}")
            return url

        except ClientError as e:
            error_code = e.response['Error']['Code']
            error_message = e.response['Error']['Message']
            current_app.logger.error(f"AWS S3 error: {error_code} - {error_message}")
            current_app.logger.error(f"Full error: {str(e)}")
            return None
        except Exception as e:
            current_app.logger.error(f"Unexpected error uploading file: {str(e)}")
            return None

    def delete_file(self, file_url):
        """
        Delete a file from S3 bucket
        """
        if not file_url:
            current_app.logger.error("No file URL provided for deletion")
            return False
            
        try:
            current_app.logger.info(f"Attempting to delete file: {file_url}")
            
            # Extract the key from the URL
            try:
                key = file_url.split(f"https://{self.bucket_name}.s3.{os.getenv('AWS_REGION', 'eu-north-1')}.amazonaws.com/")[1]
                current_app.logger.info(f"Extracted S3 key: {key}")
            except IndexError:
                current_app.logger.error(f"Invalid S3 URL format: {file_url}")
                return False
            
            # Delete the file
            self.s3_client.delete_object(
                Bucket=self.bucket_name,
                Key=key
            )
            current_app.logger.info(f"Successfully deleted file with key: {key}")
            return True
            
        except ClientError as e:
            error_code = e.response['Error']['Code']
            error_message = e.response['Error']['Message']
            current_app.logger.error(f"AWS S3 error deleting file: {error_code} - {error_message}")
            current_app.logger.error(f"Full error: {str(e)}")
            return False
        except Exception as e:
            current_app.logger.error(f"Unexpected error deleting file: {str(e)}")
            return False 