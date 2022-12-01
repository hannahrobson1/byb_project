processed = []
with open('input.txt','r') as my_file:
    for line in my_file:
        pre = line.strip().split(':')
        post = [int(x) for x in pre[1].split(',')]
        if pre[0] in ['min','max','sum']:
            calc = eval('{0}({1})'.format(pre[0],post))
            processed.append('The {0} of {1} is {2}'.format(pre[0],post,calc))
            for item in processed:
                print(item)

import numpy as np 
