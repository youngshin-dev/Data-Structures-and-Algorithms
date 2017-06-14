import sys
import math

# This will output the running median of numbers every time it read new number.
# The data structure is heap.
# The idea is to use MinHeap and MaxHip to keep the maximum of firs half in the MaxHeap
# and the minimum of second half in the MinHeap
# when a new number comes in, it will be compared with the current median and it will be inserted into Max or Min heap
# according to the comparison result.

# I've provided an array of numbers for testing


n = 6
a=[12,4,5,3,8,7]
MaxHeap=[]
MinHeap=[]

def InsertIntoMin(x):
    MinHeap.append(x)
    pos=len(MinHeap)
    if pos>=2:
        MinHeapifyUp(pos,x)


def MinHeapifyUp(pos, x):
    while pos // 2 >= 1 and MinHeap[pos//2-1] > x:
        ppos = pos// 2
        temp1 = MinHeap[pos-1]
        temp2 = MinHeap[ppos-1]
        MinHeap[ppos-1] = temp1
        MinHeap[pos-1] = temp2

        pos = ppos
        x = MinHeap[pos-1]


def ExtractMin():
    min=MinHeap[0]
    last=MinHeap[-1]
    del MinHeap[-1]
    MinHeap[0]=last
    MinHeapifyDown(1,last)
    return min



def MinHeapifyDown(pos, val):
    maxpos = len(MinHeap)
    while 2 * pos <= maxpos:
        if (2*pos+1>maxpos) or (2*pos+1<=maxpos and MinHeap[2 * pos-1] <= MinHeap[2 * pos ]):
            ind = 2 * pos-1
        elif 2*pos+1<=maxpos and MinHeap[2 * pos -1] > MinHeap[2 * pos ]:
            ind = 2 * pos

        if MinHeap[ind] < val:
            temp = MinHeap[ind]
            MinHeap[pos-1] = temp
            MinHeap[ind] = val

        pos = ind+1
        val=MinHeap[pos-1]

def InsertIntoMax(x):
    MaxHeap.append(x)
    if len(MaxHeap)>=2:
        pos=len(MaxHeap)
        MaxHeapifyUp(pos, x)


def MaxHeapifyUp(pos, x):
    while pos // 2 >= 1 and MaxHeap[pos // 2-1] < x:
        ppos = pos// 2
        temp1 = MaxHeap[pos-1]
        temp2 = MaxHeap[ppos-1]
        MaxHeap[ppos-1] = temp1
        MaxHeap[pos-1] = temp2

        pos = ppos
        x = MaxHeap[pos-1]


def ExtractMax():
    max = MaxHeap[0]
    last = MaxHeap[-1]
    del MaxHeap[-1]
    MaxHeap[0] = last
    MaxHeapifyDown(1, last)
    return max


def MaxHeapifyDown(pos, val):
    maxpos = len(MaxHeap)
    while 2 * pos <= maxpos:
        if (2*pos+1>maxpos) or (2*pos+1<=maxpos and MaxHeap[2 * pos-1] >= MaxHeap[2 * pos ]):
            ind = 2 * pos-1
        elif 2*pos+1<=maxpos and MaxHeap[2 * pos -1] < MaxHeap[2 * pos ]:
            ind = 2 * pos

        if MaxHeap[ind] > val:
            temp = MaxHeap[ind]
            MaxHeap[ind] = val
            MaxHeap[pos-1] = temp

        pos = ind+1
        val=MaxHeap[pos-1]


def main():
    median=0
    for count in range(n):
        num = a[count]
        if count ==0:
            median=float(num)
        elif count ==1 :
            if num>=median:
                InsertIntoMin(num)
                InsertIntoMax(median)
            else:
                InsertIntoMax(num)
                InsertIntoMin(median)
            median=(float(MinHeap[0])+float(MaxHeap[0]))/float(2)
        else:
            if num>=median:
                InsertIntoMin(num)

            else:
                InsertIntoMax(num)

            minLen=len(MinHeap)
            MaxLen=len(MaxHeap)

            if minLen==MaxLen:
                median=(float(MinHeap[0])+float(MaxHeap[0]))/float(2)

            elif minLen > MaxLen:
                if minLen-MaxLen==1:
                    median=float(MinHeap[0])
                elif minLen-MaxLen==2:
                    min=ExtractMin()
                    InsertIntoMax(min)
                    median=(float(min)+float(MinHeap[0]))/float(2)


            elif minLen < MaxLen:
                if MaxLen - minLen == 1:
                    median = float(MaxHeap[0])
                elif MaxLen - minLen == 2:
                    max = ExtractMax()
                    InsertIntoMin(max)
                    median = (float(max) + float(MaxHeap[0])) / float(2)

        print median

if __name__ == "__main__":
    main()






