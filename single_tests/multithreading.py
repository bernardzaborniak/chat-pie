import threading 
import time

done = False

def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)


thread1 = threading.Thread(target=worker)
thread1.start()

print('hello')
time.sleep(1)
print('hello again')
time.sleep(2)
input("Press enter to quit")



done = True

