from celery import Celery
import time

app = Celery('flask_tt', broker='redis://127.0.0.1:6379/6')


@app.task
def test_clery():
    print("into task")
    time.sleep(10)
    print('out task')
    return 'ok'
