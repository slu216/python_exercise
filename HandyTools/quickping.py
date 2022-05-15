import multiprocessing
import subprocess
import os
from quickping_helper import pinger

def ping(host:str,opt:str='-c',cnt:str='1',opt2:str='-t',timeout:str='1'):
    cmd = ['ping',opt,cnt,opt2,timeout,host]
    ret = subprocess.call(cmd,stdout=open(os.devnull, 'w'))
    # ret = subprocess.run(cmd)
    return ret

def loopPing(ip_addr='10.81.0', first=0, last=255):
    ip_vals = []
    for val in range(first,last+1):
        new_addr = ip_addr+'.'+str(val)
        ret = ping(host=new_addr)
        if ret == 0:
            ip_vals.append(new_addr)
            print(new_addr)
    return ip_vals


if __name__ == "__main__":
    # ret = ping(host='google.com') 
    # loopPing()
    pool_size = 64

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs,results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    for i in range(1,255):
        jobs.put('10.81.0.{0}'.format(i))

    for p in pool:
        jobs.put(None)  

    for p in pool:
        p.join()

    while not results.empty():
        ip = results.get()
        print(ip)
