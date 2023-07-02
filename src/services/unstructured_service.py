import logging
import os
import tempfile
import boto3
from flask import jsonify
from langchain.document_loaders import UnstructuredFileLoader

import creds

logger = logging.getLogger('app.services.unstructured')


class UnstructuredBaseService:
    def __init__(self):
        self.__s3 = boto3.client(
            's3', aws_access_key_id=creds.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=creds.AWS_SECRET_ACCESS_KEY
        )

    def retrieve_from_s3_and_handle_unstructured(self, doc_key):
        """
        Method to fetch PDF documents from S3 resource
        :param doc_key: key to find necessary PDF document
        :return: PDF document from S3 resource
        """
        with tempfile.TemporaryDirectory() as temporary:
            file_path = f"{temporary}/{doc_key}"
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            self.__s3.download_file(creds.AWS_S3_BUCKET_NAME, doc_key, file_path)
            loader = UnstructuredFileLoader(file_path)

            return loader.load()


class UnstructuredService:
    def __init__(self):
        self.__base_service = UnstructuredBaseService()
        self.__s3 = boto3.resource(
            's3', aws_access_key_id=creds.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=creds.AWS_SECRET_ACCESS_KEY
        )

    def prepare_pdf_content(self):
        """
        Base method to fetch PDF from S3 using simple boto library
        :return: jsonified PDF document
        """
        try:
            pdf = self._handle_s3_objects(prefix='s3')
            return jsonify(pdf[0].page_content[::])
        except FileNotFoundError as error:
            logger.error(error, exc_info=True)
            return jsonify(error_code=404, description="File not found"), 500

    def _handle_s3_objects(self, prefix):
        """
        Creates resource to fetch PDF file from
        :param prefix: prefix to filter unnecessary documents
        :return: Document which have been found in S3
        """
        bucket = self.__s3.Bucket(os.getenv("AWS_S3_BUCKET_NAME"))
        for s3_object in bucket.objects.filter(Prefix=prefix):
            return self.__base_service.retrieve_from_s3_and_handle_unstructured(s3_object.key)


unstructured_service = UnstructuredService()
