import numpy as np

def knapsack_greedy(W, wt, val, n):

    value_weight_ratio = val/wt

    sorted_vw = -np.sort(-value_weight_ratio)
    sorted_vw_index = np.argsort(-value_weight_ratio)

    value_packed =0
    sum = 0
    i=0
    while sum<W:
        sum += wt[sorted_vw_index[i]]
        value_packed += val[sorted_vw_index[i]]
        print("item added" , val[sorted_vw_index[i]])
        i+=1



def knapSack_dynamic(W, wt, val, n):
    mat = [[0 for x in range(W+1)] for x in range(n+1)]
    items_added =[]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                mat[i][w] = 0
            elif wt[i-1] <= w:
                mat[i][w] = max(val[i-1] + mat[i-1][w-wt[i-1]],  mat[i-1][w])
            else:
                mat[i][w] = mat[i-1][w]
    return mat


def knapSack_fptas(W, wt, val, n, k):

    val_new = [x/k for x in val]

    return knapSack_dynamic(W, wt, val_new, n)


# test
val = np.array([1, 10, 6])
wt = np.array([1, 2, 3])
W = 5
n = len(val)


knapsack_greedy(W, wt, val, n)


result = knapSack_dynamic(W, wt, val, n)
for i in result:
    print (i)

vo = np.sum(val)
n_sq = len(val)**len(val)
epsilon = 0.1
approx = vo/(n_sq*(1+(1/epsilon)))

result = knapSack_fptas(W, wt, val, n,approx)
for i in result:
    print (i)