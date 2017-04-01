time=input()
if int(time[0:2])>0 and int(time[3:5])<60 and int(time[6:8])<60 and (time[8:10]=="AM" or time[8:10]=="PM"):
    if int(time[0:2])==12 and time[8:10]=="AM":
        time1="00"+time[2:8]
        print(time1)
    elif int(time[0:2])==12 and time[8:10]=="PM":
        print(time[0:8])
    elif time[8:10]=="AM":
        print(time[0:8])
    elif time[8:10]=="PM":
        t=int(time[0:2])
        t=t+12
        time1=str(t)+time[2:8]
        print(time1)
