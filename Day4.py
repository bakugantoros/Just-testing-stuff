count = 0
# Elephant
with open('input.txt', mode = 'r') as my_file:
    print('a')
    while True:
        try:    
            # print('b')
            x = 'a'
            s = ''
            while x not in ['\n']:
                x = my_file.readline()
                # if x == 'break':
                #     j = 1
                #     break
                if x not in ['\n']:
                    s += x[:]
                    s += ' '
            # if j == 1:
            #     break
            # print('c')
            if x in ['\n']:
                lis = s.split(' ')
                lis.pop(-1)
                if len(lis) == 8:
                    count += 1
                elif len(lis) == 7 and 'cid' not in s:
                    count += 1
            print(lis)
                # else:
                #     continue
        except:
            # print('d')
            break

print(count)

