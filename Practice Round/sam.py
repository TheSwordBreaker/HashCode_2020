import numpy as np
from collections import defaultdict, namedtuple
from tqdm.autonotebook import tqdm
from os import path

class HC2020(dict):
    """Solve the practice problem of Hash Coce 2020"""
    
    class record:
        def __init__(self):
            self.selection = []
    
    
    Data = namedtuple('Data', ['target', 'slices'])
    
    IN = "in"
    OUT = "out"
    FILES = ( 'a_example.in', 'b_small.in', 'c_medium.in', 'd_quite_big.in',  'e_also_big.in' )
    
    def __init__(self):
        """Initialize data structures and read input files."""
        for file in self.FILES:
            self[file] = self.record()
            data = self.Data(*self.load_file(file))
            self[file].data = data
            
    def __repr__(self):
        return str({ file: self[file].selection for file in self.FILES })
            
    def load_file(self, file):
        with open(path.join(self.IN, file), 'r') as input:
            (capacity, count) = map(int, input.readline().split())
            slices = tuple(map(int, input.readline().split()))
                
            # print(f"file: {file}\ntarget: {capacity}\nslices: {slices}\n")
            return (capacity, slices)
        
    def save_file(self, file):
        with open(path.join(self.OUT, file), 'w') as output:
            selection = self[file].selection
            output.write(f"{len(selection)}\n")
            for s in selection:
                output.write(f"{s} ")
                
    def optimize(self, file, dp_limit=10000):
        """Optimize pizza selection with a hybrid approach.
        
        Start with a greedy approach until the remaining problem size is small enough for 
        an exact solution with dynamic programming.
        """
        
        weights = list(self[file].data.slices)
        bound = self[file].data.target
        select = []
        score = 0
        
        for i in reversed(range(len(weights))):
            if bound - score < dp_limit:
                _select, _score = self.ssp_dp(weights[:i+1], bound-score)
                print(f"dp sub-score: {_score} {bound-score} {bound-score-_score} {_select}")
                score += _score
                select += _select
                break
                
            if score + weights[i] < bound:
                score += weights[i]
                select.append(i)
        
        print(f"result: {score} {bound} {bound-score}")
        return select, score
    
    def ssp_dp(self, weights, bound):
        """Solve subset sum problem with dynamic programming
        
        See http://www.or.deis.unibo.it/kp/Chapter4.pdf
        """

        n = len(weights)
        r = np.zeros((n, bound+1), dtype=int)
        
        # fill matrix with partial solutions, i.e. with reduced bound and number of weights
        #   first dimension: maximum index of weights included
        #   second dimension: bound of sub problem
        # we need a matrix of size len(weights) * bound for this - way too much for the large instances
        for j in range(bound + 1):
            if weights[0] <= j:
                r[0][j] = weights[0]
                
        
        for i in range(1, n):
            for j in range(bound + 1):
                if weights[i] <= j:
                    r[i][j] = max(weights[i] + r[i-1][j - weights[i]], r[i-1][j])
                else:
                    r[i][j] = r[i-1][j]
        
        # Now use backtracking to get the selected weights
        select = []
        # The optimum value is r[n-1][bound]
        # Now we track the "calculation path", i.e. the cases where the first term 
        # in the max(...) was selected.
        j = r[n-1][bound]
        for i in reversed(range(n)):
            if weights[i] <= j and weights[i] + r[i-1][j - weights[i]] > r[i-1][j]:
                j -= weights[i]
                select.append(i)
        if weights[0] <= j:
            select.append(0)

        # print(r)
      
        return select, r[n-1][bound]

hc = HC2020()
    
for file in hc.FILES:
    selection, score = hc.optimize(file)
    hc[file].selection = selection
    hc[file].score = score
    hc.save_file(file)