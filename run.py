# -*- coding: utf-8 -*-

import constants
import time
import schedule
import searchjob

schedule.every(constants.JOB_RUNNING_MINUTES_INTERVAL).minutes.do(searchjob.job)
while 1:
    schedule.run_pending()
    time.sleep(1)