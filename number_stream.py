import random
import time
#Generate a stream of T numbers
t = 8
n = 2
iterations = 545.e5 # why? well it'll take about 10 minutes on this computer
start = time.clock()
def stream(t, n):
    stream = []
    while t > 0:
        stream.append(random.uniform(1, 10))
        t -= 1
    register_max = []
    register_last = []
    i =0

    while i < n:
        register_last.append(stream[t-i])
        i += 1

    counter = 0
    while counter < n:
        register_max.append(max(stream))
        stream.remove(max(stream))
        counter += 1
    m = reduce(lambda x, y: x * y, register_max, 1)
    l = reduce(lambda x, y: x * y, register_last, 1)
    return m - l

holder = 0
counter = 0
while counter < iterations:
    counter += 1
    holder += stream(t, n)
print t, ',', n, ': ', holder / iterations
print time.clock() - start

t = 32
n = 4
iterations = 182.e5 # why? well it'll take about 10 minutes on this computer
counter = 0
holder = 0
start = time.clock()
while counter < iterations:
    counter += 1
    holder += stream(t, n)
print t, ',', n, ': ', holder / iterations
print time.clock() - start
