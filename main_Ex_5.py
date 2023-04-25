import threading

mutex = threading.Semaphore(1)
empty = threading.Semaphore(1)
full = threading.Semaphore(1)

max_size = 10
size = 0
def producer():
    if full.
    mutex.acquire()
    a = int(input("How much to produce: "))
    if a>(max_size-size):
        print("refused cause over limit ")
        return False
    if a<size:
        size+=a
        print(f"produced {a} and added to buffer")
    if max_size-size == 0:
        full.acquire()
    

print(mutex)