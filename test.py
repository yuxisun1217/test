import time
import yaml
with open("config.yaml") as f:
    p=yaml.load(f)
timestamp=time.strftime("%Y%m%d %H:%M:%S", time.localtime())
prefix="[%s] " % timestamp
string=prefix+"Project: %(project)s RHEL: %(rhel_version)s\n" % p
with open("/tmp/test.log",'a') as f:
    f.write(string)
