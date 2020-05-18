from flask_tt.tasks.tasks import test_clery
import time

t1 = time.time()

tt = test_clery.delay()

while not tt.ready():
    pass
print(tt.result)

t2 = time.time()

print(t2 - t1)
