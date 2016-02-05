import hashlib

print('Please provide your file path:')     ###provide the path of the file to be hashed.
file_path = raw_input()

print('Please provide the correct hash number')
correct_hash = raw_input()

hash_num=hashlib.sha256()       ###SHA256 is taken here. Users can change it to any other hash algorithm.
blocksize = 65536               ###2^32 = 65536

with open(file_path,'rb') as file:     ###open the local file
    buf = file.read(blocksize)              ###get the hash number
    while len(buf)>0:
        hash_num.update(buf)
        buf = file.read(blocksize)

print hash_num.hexdigest()

if hash_num.hexdigest() == correct_hash:
    print("------Cool! File is not modified or corrupted.------")
else:
    print("------File content may be altered. Please download the file again.------")
