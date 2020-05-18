from celery import Celery

app = Celery('flask_tt', include=['flask_tt.tasks.tasks'])
app.config_from_object('flask_tt.tasks.config')

if __name__ == '__main__':
    app.start()
