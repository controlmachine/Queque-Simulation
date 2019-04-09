import simpy
import numpy as np
import pandas as pd
from time import sleep
from collections import namedtuple
from pprint import pprint

class Process:
    procsall = []
    procs = namedtuple('arrival', 'time burst')
    def __init__(self):
        self.name = self._namecalc()
        

    @staticmethod
    def calc_arrival(procsall=procsall,procs=procs): 
        arrv = 0
        burst = 0 
        for i in range(10):
            arrv += np.random.poisson()
            burst += np.random.exponential()
            procsall.append(procs(time=arrv,burst=burst))
            
                      
    def _namecalc():
        pass
