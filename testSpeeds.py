import speedtest
import time, math
import json

st = speedtest.Speedtest()
counter = 1
a = {}

#Filename based on starting time
fname = str(math.floor(time.time()))

#wait time for each speedtest
wait = 300

while True:
    #take speedtest
    speed = st.download()
    
    #make a file and write data to it
    f = open("./JSON/" + fname +".json","w+")
    a[counter] = speed/(1024*1024)
    b = json.dumps(a)
    json.dump(b, f)
    f.close()
    
    #show success message and wait for waiting time
    print("successful:",counter)
    counter += 1
    time.sleep(wait)
