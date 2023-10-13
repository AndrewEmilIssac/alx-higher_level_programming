#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None:
            MaxV=0
            MaxK=None
            for K, V in a_dictionary.items():
                if V > MaxV
                MaxV = V
                MaxK = K
                return MaxK
