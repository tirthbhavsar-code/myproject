import datetime

def show_time():
    now = datetime.datetime.now()
    print("Current time:", now.time())

show_time()
