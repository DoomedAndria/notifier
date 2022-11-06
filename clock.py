from apscheduler.schedulers.blocking import BlockingScheduler
from main import run

sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=15)
def timed_job():
    print("running..")
    run()


sched.start()
