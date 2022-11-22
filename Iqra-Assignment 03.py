# -*- coding: utf-8 -*-
disks=int(input('please state the number of disks:'))


if disks%2 == 0:
    for i in range (1, pow(2,disks)):
        if i%3==1:
            if index%2==0:
                print('move form source to auxiliary')
            else:
                print('move form auxiliary to source')
        elif i%3==2:
            if index%2==0:
                print('move form destination to source')
            else:
                print('move form source to destination')
        else:
            if index%2==0:
                print('move form auxiliary to destination')
            else:
                print('move form destination to auxiliary')
        i=i+1
        index=index+1
else:
    for i in range (1, pow(2,disks)):
        if i%3==1:
            if index%2==0:
                print('move form source to destination')
            else:
                print('move form destination to source')
        elif i%3==2:
            if index%2==0:
                print('move form auxiliary to source')
            else:
                print('move form source to auxiliary')
        else:
            if index%2==0:
                print('move form auxiliary to source')
            else:
                print('move form destination to auxiliary')
        i=i+1
        index=index+1