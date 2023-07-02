import logging

from flask import jsonify
from langchain.document_loaders import S3DirectoryLoader

import creds

logger = logging.getLogger('app.services.langchain')


class LangchainService:
    @staticmethod
    def retrieve_document_from_s3():
        """
        Method to use langchain library to work with S3 objects and write data on webpage
        :return: jsonified pdf document
        """
        try:

            loader = S3DirectoryLoader(creds.AWS_S3_BUCKET_NAME, prefix='langchain')
            # S3DirectoryLoader is already used unstructured library within itself
            pdf = loader.load()
            return jsonify(pdf[0].page_content[::])
        except FileNotFoundError as error:
            logger.error(error, exc_info=True)
            return (
                jsonify(error_code=404, description="File not found"),
                500,
            )


langchain_service = LangchainService()
