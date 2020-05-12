from flask import Blueprint
import os

mod = Blueprint('hello', __name__)


@mod.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'hello world'
