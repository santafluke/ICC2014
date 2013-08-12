'''
Created on Aug 5, 2013

@author: yzhang28
'''

# -*- coding: utf-8 -*-
import numpy as np
import scipy as sp
from scipy.misc import factorial
import math
#from pulp import *
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import FuncFormatter
from matplotlib.transforms import Bbox

from MDPSolver import MDPOptimization

def OffloadingRate(a_mat,getN=False):
    total_act = 0
    act_1 = 0
    for i_g, dim1 in enumerate(a_mat):
        for i_q, dim2 in enumerate(dim1):
            for i_n, elem in enumerate(dim2):
                if i_g!=0 and i_q!=0:
                    total_act = total_act + 1
                    if 1==elem:
                        act_1 = act_1 + 1
    if False==getN:
        return act_1*1.0/(total_act*1.0)
    else:
        return act_1*1.0/(total_act*1.0), total_act
    
def ValueAverage(v_mat):
    total_states = 0
    total_value = 0.0
    for i_g, dim1 in enumerate(v_mat):
        for i_q, dim2 in enumerate(dim1):
            for i_n, elem in enumerate(dim2):
                if i_g!=0 and i_q!=0:
                    total_states = total_states + 1
                    total_value = total_value + elem
    return total_value*1.0/(total_states*1.0)

def ValueOf(v_mat, G=1,Q=1,N=0):
    if 0==G or 0==Q:
        print "Outta bound. ERROR in FUNC: ValueOf(G=1,Q=1,N=0)"
    return v_mat[G][Q][N]


def ShowActionMatrix(mat,G=-1):
        if -1==G: #default
            for i_g,dim1 in enumerate(mat):
                if i_g!=0:
                    print 'State G=', i_g
                for i_q,dim2 in enumerate(dim1):
                    for i_n,elem in enumerate(dim2):
                        if i_g!=0 and i_q!=0:
                            print '(Q%dN%d Act:) %d   '%(i_q,i_n,mat[i_g][i_q][i_n]),
                    print
                print
            print
        else:
            # Print the threshold graph for given phase G
            print 'G =', G
            for i_q,dim2 in enumerate(mat[G]):
                for i_n,elem in enumerate(dim2):
                    print '(Q%dN%d Act:) %d   '%(i_q,i_n,elem),
                print
