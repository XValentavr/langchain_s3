import logging

from flask import Blueprint

from services.langchain_service import langchain_service
from services.unstructured_service import unstructured_service

logger = logging.getLogger('app.controller.content')
logger.setLevel(logging.INFO)

content = Blueprint('content', __name__)


@content.route('/', methods=['GET'])
def get_pdf_content_with_langchain():
    return langchain_service.retrieve_document_from_s3()


@content.route('/s3', methods=['GET'])
def get_pdf_content_with_s3_client():
    return unstructured_service.prepare_pdf_content()
