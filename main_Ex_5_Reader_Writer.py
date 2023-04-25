import threading
read_count = 0
mutex = threading.Semaphore(1)
writer_lock = threading.Semaphore(1)

def reader():
    global read_count
    writer_lock.acquire()
    mutex.acquire()
    writer_lock.release()
    read_count += 1
    if read_count == 1:
        writer_lock.acquire()
    mutex.release()
    print("Reading...")

    mutex.acquire()
    read_count -=1
    if read_count == 0:
        writer_lock.release()
    mutex.release()

def writer():
    writer_lock.acquire()
    print("writing")
    writer_lock.release()
threads = []
for i in range(5):
    threads.append(threading.Thread(target=reader))
    threads.append(threading.Thread(target=writer))
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
