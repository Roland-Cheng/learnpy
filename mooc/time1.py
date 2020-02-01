import time
for i in range(100):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.1)
time.sleep(10)
print("\r100%")