import time
# complex_computation() simulates a slow function.
# time.sleep(n) causes the
# program to pause for n seconds.
# In real life, this might be a call to a
# database, or a request to another web service.
def complex_computation(a, b):
    time.sleep(.5)
    return a + b

# QUIZ - Improve the cached_computation()
# function below so that it caches
# results after computing them for the first
# time so future calls are faster
cache = {}
def cached_computation(a, b):
    key = (a,b)
    if key in cache.keys():
        return cache[key]
    else:
        computation = complex_computation(a,b)
        cache[key] = computation
        return computation


cached_computation(5,10)

start_time = time.time()
print(cached_computation(5, 3))
first_time = time.time() - start_time
print("The first computation took {} seconds./n".format(first_time))
start_time2 = time.time()
print(cached_computation(5, 3))
second_time = time.time() - start_time2
print("The second computation took {} seconds./n".format(second_time))
print("Result: {} times less".format(first_time/second_time))