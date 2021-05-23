# -*- coding: utf-8 -*-

import config
import time
import schedule
import searchjob

searchjob.job()

schedule.every(
    config.config_file['constants']['job_running_minutes_interval']
).minutes.do(searchjob.job)
while 1:
    schedule.run_pending()
    time.sleep(1)
