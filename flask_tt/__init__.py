from flask import Flask, render_template
from datetime import datetime
from flask_tt.views.hello import mod as hello
from flask_tt.views.user import mod as user
from flask_tt import config
from flask_tt.models import db
from logging.handlers import TimedRotatingFileHandler
import logging
import os

app = Flask("flask_tt")
app.config['SECRET_KEY'] = os.urandom(24)
app.config.from_object(config.config['dev'])


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.before_request
def load_current_user():
    pass


@app.teardown_request
def remove_db_session(exception):
    pass


@app.context_processor
def current_year():
    return {'current_year': datetime.utcnow().year}


# 注册路由
app.register_blueprint(hello)
app.register_blueprint(user)
# 数据库操作类配置初始化
db.init_app(app)

# 日志配置
time_file_handler = logging.handlers.TimedRotatingFileHandler(
    config.LOG_FILE,
    when='M',
    backupCount=10
)


def split_name(filename):
    return filename.split(config.LOG_FILE.replace('logs/', '') + ".")[1]


time_file_handler.namer = split_name
time_file_handler.suffix = f"logs/%Y-%m-%d({str(os.getpid())}).log"
logging.basicConfig(format=config.LOG_FORMAT_STR, level=logging.WARNING, handlers=[time_file_handler])
