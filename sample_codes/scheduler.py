import sched, time
import sys
sys.path.insert(1, "/examples")
from canvas import get_assignments

s = sched.scheduler(time.time, time.sleep)
def print_time(a='default'):
    print("From print_time", time.time(), a, ":")
    print(get_assignments())
    print("------------------------")

def print_some_times():
    interval = 5 # in seconds
    
    while True:
        s.enter(interval, 1, print_time)
        s.run()
    
print_some_times()