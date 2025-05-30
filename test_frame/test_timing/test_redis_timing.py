import time

from funboost import run_forever,funboost_aps_scheduler
from funboost.timing_job.apscheduler_use_redis_store import funboost_background_scheduler_redis_store
from apscheduler import version
from apscheduler.schedulers.background import BackgroundScheduler

print(version)
from test_frame.test_timing.test_timming import consume_func



funboost_aps_scheduler.add_push_job(consume_func, 'interval', id='3_second_job', seconds=3, kwargs={"x": 5, "y": 6},replace_existing=True)  # 每隔3秒发布一次任务，自然就能每隔3秒消费一次任务了。
funboost_aps_scheduler.start(paused=True)
# funboost_background_scheduler_redis_store.start()

time.sleep(20)
funboost_aps_scheduler.resume()
run_forever()