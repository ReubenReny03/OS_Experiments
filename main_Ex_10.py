#Disk_Sheduling_Algo
'''
Our joub is that we are given a head and a list of numbers we just need to go through each of those number one after the other and
print the diffrence in the screen also the total sum of diffrences.
'''

#FCFS
def fcfs(head,o_list): # we take the head element and the list of all other positions 
    sum  = 0 
    print("head differences: ")
    print(abs(head-o_list[0])) #for the first line 
    sum += abs(head-o_list[0]) # adding it to sum 
    for x in range (1,len(o_list)):
        print(abs(o_list[x]-o_list[x-1]))  # for printing rest of the elements in the list
        sum += abs(o_list[x]-o_list[x-1])  # for adding them into the list
    print("Total head movements:",sum)      # printing the total sum

#SSTF
def sstf(head,o_list):
    '''
    for the 1st we take head and find the most sutable in the o_list then we take that as the temp and run through the o_list
    and remember we will remove this temp from the list so that it does not find itself again and then we create a new temp_n for 
    the chosen element and then print that abs and then make temp = temp_n and remove the old temp from the list : ) easy way out
    '''
    sum =0
    leng = len(o_list)
    min = 98129038
    for x in range(leng):
        if min>abs(head-o_list[x]):
            min = abs(head-o_list[x])
            target = x
            temp = o_list[target]
    print("target",o_list[target])
    out = abs(head-temp)
    print(out)
    sum +=out
    o_list.pop(target)
    while o_list:
        min = 98129038
        for x in range (len(o_list)):
            if min>abs(temp-o_list[x]):
                min = abs(temp-o_list[x])
                target = x
                temp_n = o_list[target]
        print("target",o_list[target])
        out = abs(temp_n-temp)
        print(out)
        sum +=out
        o_list.pop(target)
        temp = temp_n
    print(sum)

#fcfs(53,[98,183,37,122,14,124,65,67]) # code to run fcfs
#sstf(53,[98,183,37,122,14,124,65,67]) # code to run sstf

