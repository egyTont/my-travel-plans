import time
import webbrowser
total_counts=4
counts_done=0
print("Program started:"+time.ctime())
while counts_done<total_counts:
    time.sleep(10)
    webbrowser.open("google.com")
