#Page Replacement
#FiFo
def fifo(pages,page_size):
    page_holder = []
    print(page_holder)
    for x in pages:
        if x not in pages and len(page_holder)<page_size:
            page_holder.append(x)
            print("miss")
            print(page_holder)
        elif x not in page_holder:
            page_holder.append(x)
            page_holder.pop(0)
            print("miss")
            print(page_holder)
        else:
            print("hit")
            print(page_holder)

from collections import deque
def lru(pages,page_size):
    page_holder = deque(maxlen=page_size)
    print(page_holder)
    for x in pages:
        if x not in page_holder and len(page_holder)<page_size:
            page_holder.append(x)
            print("miss")
            print(page_holder)
        elif x not in page_holder:
            page_holder.popleft()
            page_holder.append(x)
            print("miss")
            print(page_holder)
        else:
            page_holder.remove(x)
            page_holder.append(x)
            print("hit")
            print(page_holder)

def opti(pages,page_size):
    page_holder = deque(maxlen=page_size)
    for x in range(len(pages)):
        if pages[x] not in page_holder and len(page_holder)<page_size:
            page_holder.append(pages[x])
            print("miss")
        elif pages[x] not in page_holder:
            fu_pages = pages[x+1:]
            for old in page_holder:
                index_rm = -1
                if old not in fu_pages:
                    rm = old
                    print("miss")
                    break
                elif old in fu_pages:
                    if fu_pages.index(old)>index_rm:
                        index_rm = fu_pages.index(old)
                        rm = old
            page_holder.remove(rm)
            page_holder.append(pages[x])
        else:
            print("hit")

            


#fifo([1,3,0,3,5,6,3],3)
opti([7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2,3],4)
