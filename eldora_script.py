import urllib
import time
import datetime
import smtplib

# from __future__ import print_function
# Begin Helper Functions

# Update Next Check Time
def get_next_time():
    seconds_in_day = 86400
    cur_time = time.time()
    tomorrow_time = cur_time+seconds_in_day
    t_tomorrow = time.localtime(tomorrow_time)
    # Update Time
    t_hour = 6 # am
    t_min = 50 # give them 5 minutes to get it up
    t_sec = 0
    d = datetime.datetime(t_tomorrow.tm_year,t_tomorrow.tm_mon,t_tomorrow.tm_mday,t_hour,t_min,t_sec)
    next_time = time.mktime(d.timetuple())
    return next_time

# Get Eldora Data
def get_snow_report():
    urlStr = "http://www.eldora.com/mountain.snow.php"
    try:
        fileObj = urllib.urlopen(urlStr)
        for line in fileObj:
            if('New snow in the last 24 hours:' in line):
                startIndex = line.find(':')+1
                endIndex = line.find('inch')
                str_val = line[startIndex:endIndex]
                eldora_24_snow_val = float(str_val)
            if('New snow in the last 48 hours:' in line):
                startIndex = line.find(':')+1
                endIndex = line.find('inch')
                str_val = line[startIndex:endIndex]
                eldora_48_snow_val = float(str_val)
            if('New snow in the last 72 hours:' in line):
                startIndex = line.find(':')+1
                endIndex = line.find('inch')
                str_val = line[startIndex:endIndex]
                eldora_72_snow_val = float(str_val)
        err_val = 0
    except:
        eldora_24_snow_val = 0
        eldora_48_snow_val = 0
        eldora_72_snow_val = 0
        err_val = 1
    return eldora_24_snow_val,eldora_48_snow_val,eldora_72_snow_val,err_val

# End Helper Functions

# Begin Vars
wait_period = 2 # seconds - 15 minutes
update_req = True
count = 0
log_file = "eldora_snow_log.txt"
f = open(log_file,'w')
f.close()

# Begin Loop
while(1):
    if(update_req):
        t = time.localtime()
        count=count+1
        f = open(log_file,'a')
        update_val = get_next_time()
        e_24,e_48,e_72,e_val = get_snow_report()
        f.write(str(count))
        f.write(" ")
        f.write(str(t.tm_year))
        f.write(" ")
        f.write(str(t.tm_mon))
        f.write(" ")
        f.write(str(t.tm_mday))
        f.write(" ")
        f.write(str(e_24))
        f.write(" ")
        f.write("\n")
        f.close()
        print e_24
        print e_48
        print e_72
        print e_val
        update_req = False
    # Check Time
    time.sleep(wait_period)
    if(time.time()>update_val):
        update_req = True
    # Debug    
    update_req = True    
    




        



