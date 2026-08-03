

try:
    j = []
    for i in range(6):
        p = int(input())
        j.append(p)

        for i in j:
            if i < 0:
                j.remove(i)
        print(j)
except: 
    print('stupid idiot error error')
    

