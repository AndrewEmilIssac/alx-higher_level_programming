#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None:
            maxV = 0
            maxK = None
            for K, V in a_dictionary.items():
                if V > maxV
                maxV = V
                maxK = k                
            return maxK:
