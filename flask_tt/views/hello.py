from flask import Blueprint
from flask import current_app
import logging

mod = Blueprint('hello', __name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


@mod.route('/', methods=['POST', 'GET'])
def hello_world():
    logger.warning("into index")
    return 'hello world'
