import logging

from flask import Flask

from controllers.content_controller import content

logger = logging.getLogger('app')

# initializing flask app
application = Flask(__name__)

application.register_blueprint(content)


if __name__ == '__main__':
    application.run(port=5000, host='0.0.0.0')
