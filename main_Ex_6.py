def safe_or_not(avalable,max,allocation):
    '''
    our main goal is to find out if the state is safe or not safe
    rememmber the short cut to make the need array
    and the valuews array can have numbers depending on the number of elements in avalable
    these numbers are used to show the number in the output
    while need is not empty we set a tripper to trip if it is again and a

    '''
    n = len(avalable)
    values = [1,2,3,4,5]
    need = [[max[i][j]-allocation[i][j] for j in range(len(max[i]))]for i in range(len(max))]
    print(need)

    while need:
        tripper = 0
        a = 0 
        for x in range(a,len(need)):
            for y in range(n):
                if need[x][y] > avalable[y] and len(need) == 1:
                    need = []
                    break
                elif need[x][y] > avalable[y]:
                    break

            else:
                print(f"{values[x]} executed ")
                for z in range(n):
                    avalable[z]+= need[x][z]
                values.pop(need.index(need[x]))
                need.remove(need[x])
                tripper = 1
                if  need != []:
                    a = x%len(need)
                break
        if tripper == 0:
            print("not safe")
            break


max = [[100,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
avalable = [3,3,2]
safe_or_not(avalable,max,allocation)