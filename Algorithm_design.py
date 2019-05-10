# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:39:31 2019

@author: yatha
"""
import functions as func
import random
import numpy as np
import math

def equal(f1, f2,tries=100,tolerance=0.0001):
    for i in range(tries):
        #x = random.random()
        x = 0
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True

def prime(n,tries=1000):
    m = int(np.sqrt(n))
    for i in range(tries):
        x = random.randint(2, m)
        if n%x==0:
            print(x)
            return False
    return True  

def subsetsum(S,last,goal):
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last]) # Take S[last]
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S,last-1,goal) # Don't take S[last]


def part_set(set1,set2,take):
    if sum(set1) == sum(set2):
        return set1,set2
    if set1 == None:
        print('no sets found')
        return -1
    for i in range(take):
        if take < len(set1):
            list1 = list(set1)
            print(list1)
            last = list1.pop(-1)
            set2.add(last)
            set1.remove(last)
    return part_set(set1,set2,take+1)
    
def edit_distance(s1,s2):
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[0,:] = np.arange(len(s2)+1)
    d[:,0] = np.arange(len(s1)+1)
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] ==s2[j-1]:
                d[i,j] =d[i-1,j-1]
            else:
                n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                d[i,j] = min(n)+1
    #print(d)          
    return d[-1,-1]

def find_ident(L):
    idents = []
    print('Identities are:')
    for i in range(len(L)):
        j = i +1
        if j<len(L)-1:
            if equal(L[i],L[j]) == True:
                idents.append([i,j])
    return idents

if __name__ == "__main__":  
    test_set ={1,2,3,4}
    empty_set = set()
    
    func = func.get_func_list()
    print(find_ident(func)) 
    print()
    print(part_set(test_set,empty_set,1))
    
    
"""
    f1 = 'x*x + x - 12'
    f2 = '(x+4)*(x-3)'
    print(equal(f1,f2))
    
    f1 = 'sin(x)/cos(x)'
    f2 = 'tan(x)'
    print(equal(f1,f2))
    
    f1 = 'sin(x)*sin(x) + cos(x)*cos(x)'
    f2 = '1'  
    print(equal(f1,f2))
    
    f1 = '(x+1)*(x-1)'
    f2 = 'x*x-1'  
    print(equal(f1,f2))
    
    f1 = '(x+10)/10'
    f2 = 'x'  
    print(equal(f1,f2))
    
    print(prime(997))
    print(prime(1008))
    
    s2='MONEY'
    d = edit_distance('MINERS','MONEY')
    print(d)
    
    S = [2,5,8,9,12,21,33]
    
    for i in range(100):
        print('Goal =',i)
        a,s = subsetsum(S,len(S)-1,i)
        if a:
            print('Solution:',s)
        else:
            print('There is no solution')
"""