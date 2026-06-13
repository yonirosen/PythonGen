import os
import sys
import argparse

def expendS(a, n):
    listOfSs=[]
    for i in range(0, len(a)+1):
        listOfSs.append(a[0:i] + [n] + a[i:])
    return listOfSs

def getAllPerm(n):
    allS = [[1]]
    for j in range(2, n+1):
        extS = []
        for a in allS:
            extS = extS + (expendS(a, j))
        allS = extS
    return allS

def applyPerm(base, perm):
    permutate = []
    for i in range(0, len(perm)):
        permutate.append(base[perm[i]-1])
    return permutate

def isSameCyclic(a, b):
    if len(a) != len(b):
        return False
    for i in range(0, len(b)):
        if a == b:
            return True
        a = [a[len(a)-1]] + a[0:-1]
    return False

def isAbelicWithinCycle(s_size):
    base = [chr(96+n) for n in range(1,s_size+1)]
    print(s_size)
    print(base)
    allS = getAllPerm(s_size)
#    print(allS)
    for i in range(0, len(allS)):
        for j in range(i+1, len(allS)):
            jXi = applyPerm(applyPerm(base, allS[i]), allS[j])
            iXj = applyPerm(applyPerm(base, allS[j]), allS[i])
            if not isSameCyclic(iXj, jXi):
                print(f' i:{allS[i]}, j:{allS[j]} => jXi:{jXi}, iXj={iXj}')
                return False
    return True

def printPerm(s_size):
    isAbel = isAbelicWithinCycle(s_size)
    print(f' S{s_size} ==> {isAbel}')
        
#    for perm in allS:
#        print(applyPerm(base, perm))


if __name__ == '__main__':
    print("here we come together")
    parser = argparse.ArgumentParser(description='Here we are')
    parser.add_argument('--size', dest='s_szie', type=int, required=True, help='S group size')
    args = parser.parse_args()
    s_size = int(args.s_szie)
    printPerm(s_size)
    
