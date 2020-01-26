import sys


def sg(p, l, r, c):
    if (l == r):
        b = p[0]
        #print(p[0])
        for i in range(1, len(p)):
            #print (p[i])
            b ^= p[i]
        #c += 1
        if (b < 1):
            c += 1
        return c
    else:
        i = l
        for i in range(l, r + 1):
            p[l], p[i] = p[i], p[l]
            c = sg(p, l + 1, r, c)
            p[l], p[i] = p[i], p[l]
    return c

def stoneGame(p):
    b = sg(p, 0, len(p) - 1, 0)
    print (b)


if __name__ == "__main__":
   # p = [1, 2, 3]
    p = [10, 10, 1, 1, 1, 1, 1, 10, 10, 10]
    stoneGame(p)

#
#
#
#
# # Program to print all combination
# # of size r in an array of size n
#
# # The main function that prints all
# # combinations of size r in arr[] of
# # size n. This function mainly uses
# # combinationUtil()
# def printCombination(arr, n, r):
#
# 	# A temporary array to store
# 	# all combination one by one
# 	data = [0] * r
#
# 	# Print all combination using
# 	# temprary array 'data[]'
# 	combinationUtil(arr, n, r, 0, data, 0)
#
# ''' arr[] ---> Input Array
# n	 ---> Size of input array
# r	 ---> Size of a combination to be printed
# index ---> Current index in data[]
# data[] ---> Temporary array to store
# 			current combination
# i	 ---> index of current element in arr[]	 '''
# def combinationUtil(arr, n, r, index, data, i):
#
# 	# Current cobination is ready,
# 	# print it
# 	if (index == r):
# 		for j in range(r):
# 			print(data[j], end = ' ')
# 		print()
# 		return
#
# 	# When no more elements are
# 	# there to put in data[]
# 	if (i >= n):
# 		return
#
# 	# current is included, put
# 	# next at next location
# 	data[index] = arr[i]
# 	combinationUtil(arr, n, r, index + 1,
# 					data, i + 1)
#
# 	# current is excluded, replace it
# 	# with next (Note that i+1 is passed,
# 	# but index is not changed)
# 	combinationUtil(arr, n, r, index,
# 					data, i + 1)
#
# # Driver Code
# if __name__ == "__main__":
# 	arr = [10, 10, 1, 1, 1, 1, 1, 10, 10, 10]
# 	n = len(arr)
# 	r = n
# 	printCombination(arr, n, r)
#
# # This code is contributed
# # by ChitraNayal
