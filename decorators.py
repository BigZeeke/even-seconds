# Solution:
# Decorator accepts any func
# Wrapper intercepts every call to the decorated func
# Check if second is even
# Hand original function's result back to the caller
# Return the wrapper function
# Print current second
# Need to log seconds, don't need interception
# Run a loop 4 times
# Grab current clock second as integer
# Call wrapper(now), runs func, checks even/odd
# Pause 1 second so the clock can advance before next iteration
# Start the loop

from datetime import datetime
import time


def only_even_seconds(func):
    def wrapper(second):
        result = func(second)
        if second % 2 == 0:
            print("Even second - congrats")
        else:
            print("Odd second - alert")
        return result
    return wrapper


@only_even_seconds
def seconds_count(second):
    print(f"Current second: {second}")


def log_second(second):
    print(f"Logging: {second}")


def check_six_times():
    for i in range(4):
        now = datetime.now().second
        seconds_count(now)
        log_second(now)
        time.sleep(1)


check_six_times()
