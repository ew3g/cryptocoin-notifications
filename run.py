# -*- coding: utf-8 -*-

import time
import schedule
import searchjob

schedule.every(10).seconds.do(searchjob.job)
while 1:
    schedule.run_pending()
    time.sleep(1)