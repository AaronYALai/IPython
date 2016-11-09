#Data http://snap.stanford.edu/data/web-Google.txt.gz
# Directed graph (each unordered pair of nodes is saved once): web-Google.txt 
# Nodes: 875713 Edges: 5105039

import numpy as np
import time
from scipy.sparse import csr_matrix
import pandas as pd

start_time = time.clock()

web = pd.read_csv('web-Google.txt', sep='\t', comment='#', names=['from', 'to'])
print("Data Loaded... using %f seconds"%(time.clock()-start_time))

data = np.repeat(1, web.shape[0])
categories = np.unique(web.values) 
col_ind = pd.Categorical(web['from'], categories=categories).codes #get the colunmn indexes
row_ind = pd.Categorical(web['to'], categories=categories).codes #get the row indexes
A = csr_matrix((data, (row_ind, col_ind))) #sparse matrix with some entries = 1
A = A.multiply(csr_matrix(1 / A.sum(axis=0))) #Sparse matrix for PageRank
print("Sparse Matrix Constructed... using %f seconds"%(time.clock()-start_time))

r = np.empty(875713)
r.fill(1/875713)
dist = 10; cycle=0

while dist > 10**(-10):
    r_new = 0.8*A.dot(r)
    r_new = r_new + (1-np.sum(r_new))/875713
    dist = np.sum(np.abs(r-r_new))
    cycle += 1
    r = r_new

print("All Done. Using %f seconds, total %d cycles for epsilon less than e-10."%(time.clock()-start_time,cycle))
np.savez('PageRank',r) #r[95]
