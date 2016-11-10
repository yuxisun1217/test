import time
timestamp=time.strftime("%Y%m%d %H:%M:%S", time.localtime())
with open("/tmp/test.log",'a') as f:
    f.write(timestamp+'aaa\n')
