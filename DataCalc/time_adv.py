import time
# from time import perf_counter as my_timer
# from time import monotonic as my_timer
from time import process_time as my_timer
import random

input("Please enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
star_time = my_timer()

input("Please enter to stop")

end_time = my_timer()

print("started at: " + time.strftime("%X", time.localtime(star_time)))
print("stopped at: " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - star_time))
