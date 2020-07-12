from apscheduler.schedulers.blocking import BlockingScheduler
from whatsappAuto import send_message

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_message, 'interval', hours=24)

sched.start()
