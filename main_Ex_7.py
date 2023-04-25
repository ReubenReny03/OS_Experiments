#Contiguous Memory Allocation
#worst fit
def worst_fit(blockSize,processSize):
    new_block_size = sorted(blockSize,reverse=True)
    for x in processSize:
        if x < new_block_size[0]:
            print(f"{x} --> {new_block_size[0]}")
            new_block_size.pop(0)
        else:
            print(f"{x} --> Could not be placed")

def first_fit(blockSize,processSize):
    for x in processSize:
        for y in blockSize:
            if x<y:
                print(f"{x} --> {y}")
                blockSize.remove(y)
                break
        else:
            print(f"{x} --> cannot be placed")

def best_fit(blockSize,processSize):
    new_pro = sorted(processSize,reverse=True)
    new_blo = sorted(blockSize,reverse=True)
    first_fit(new_blo,new_pro)








blockSize= [100, 500, 200, 300, 600]
Block_no= [1, 2, 3, 4, 5]
processSize= [212, 417, 112, 426]

best_fit(blockSize,processSize)

