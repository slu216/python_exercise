import numpy as np
import time
from ipwhois import IPWhois
from multiprocessing import Pool

def get_ip(a):
    return str(a//256//256//256)+'.'+str((a//256//256)%256)+'.'+str((a//256)%256)+'.'+str(a%256)

#using for loop to generate the list.
def generate_ip_for_loop(data,list_range=range(2**24,2**24+2**8)):
    start=time.time()
    for i in list_range:
        ip_addr = get_ip(i)
        obj = IPWhois(ip_addr)
        res = obj.lookup_whois()
        data =  np.append(data,[ip_addr,res['nets'][0]['name']])
    stop=time.time()
    print("Runnign time is %.2f" % ((stop-start)/60))
    return data
		
#using list comprehenssion to generate the list.
def generate_ip_list_conpre(data,list_range=range(2**24,2**24+2**8)):
    start=time.time()
    data = [[get_ip(x),IPWhois(get_ip(x)).lookup_whois()['nets'][0]['name']] for x in list_range]
    stop=time.time()
    print("Runnign time is %.2f" % ((stop-start)/60))
    return data
