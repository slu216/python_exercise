import multiprocessing
import subprocess
import os


def ping(host:str, opt:str='-c', cnt:str='1', opt2:str='-t', timeout:str='1'):
    cmd = ['ping', opt, cnt, opt2, timeout, host]
    ret = subprocess.call(cmd,stdout=open(os.devnull, 'w'))
    # ret = subprocess.run(cmd)
    return ret


def loopping(ip_addr='10.81.0', first=0, last=255):
    ip_vals = []
    for val in range(first,last+1):
        new_addr = ip_addr+'.'+str(val)
        ret = ping(host=new_addr)
        if ret == 0:
            ip_vals.append(new_addr)
            print(new_addr)
    return ip_vals


def pinger(job_q, results_q):
    devnull = open(os.devnull, 'w')
    while True:
        ip = job_q.get()
        if ip is None: break
        try:
            ret = subprocess.call(['ping','-c1','-t1',ip],
                                  stdout=devnull)
            if ret == 0:
                results_q.put(ip)
            # print(ip)
        except:
            pass


if __name__ == "__main__":
    # ret = ping(host='google.com') 
    # loopping()
    pool_size = 64

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs,results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    for i in range(0,255):
        for j in range(0,255):
            jobs.put('169.254.{0}.{1}'.format(i,j))

    for p in pool:
        jobs.put(None)  

    for p in pool:
        p.join()

    while not results.empty():
        ip = results.get()
        print(ip)
