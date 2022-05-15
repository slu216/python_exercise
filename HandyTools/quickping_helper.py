import multiprocessing
import os
import subprocess


def pinger(job_q, results_q):
    DEVNULL = open(os.devnull,'w')
    while True:
        ip = job_q.get()
        if ip is None: break
        try:
            ret = subprocess.call(['ping','-c1','-t1',ip],
                                  stdout=DEVNULL)
            if ret == 0:
                results_q.put(ip)
            # print(ip)
        except:
            pass
