## Getting Started

1. Clone the repository: `git clone https://github.com/XValentavr/langchain.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set the necessary environment variables:
   - `AWS_ACCESS_KEY_ID`: Your AWS access key ID
   - `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key
   - `AWS_S3_BUCKET_NAME`: Name of the S3 bucket
4. Start the application: `python app.py` or `docker-compose up --build`
5. Access the API endpoints using the provided examples.
6. Make sure that you have files in S3 bucket

## Endpoint specification
1. /s3 - fetch PDF document from S3 bucket using boto3 client and unstructured library to process document
2. / - fetch PDF document from S3 bucket using langchain logic

## Dependencies

- Python 3.7 or higher
- Flask
- Boto3
- Langchain
- Unstructured 
- All dependencies are in requirements.txt file
## Notes
1. S3 bucket has no public access
