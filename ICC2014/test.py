'''
Created on Aug 7, 2013

@author: yzhang28
'''

from Headers import *

# Q_max_CONST = 1 + 6
# lam_q_CONST = 0.25
# def PoissonQ(q1, q2):
#     if 0<q1 and q1<(Q_max_CONST-1) and q1<=q2 and q2<(Q_max_CONST-1):
#         return np.exp(-1*lam_q_CONST)*np.power(lam_q_CONST,q2-q1)/factorial(q2-q1,exact=True)
#     #2
#     if 0<q1 and q1<(Q_max_CONST-1) and (Q_max_CONST-1)==q2:
#         sum_tmp = 0.0
#         for k in range(q1,Q_max_CONST-1): #\mathcal{Q},\mathcal{Q}+1,...,(Q_max_CONST-1)-1 (i.e., Q-1)
#             sum_tmp = sum_tmp + np.exp(-1*lam_q_CONST)*np.power(lam_q_CONST,(k-q1))/factorial((k-q1),exact=True)
#         tmp = (1.0-sum_tmp)
#         return tmp
#     #3
#     if (Q_max_CONST-1)==q1 and (Q_max_CONST-1)==q2:
#         return 1.0
#     else:
#         return 0
#       
# for q1 in range(0,7):
#     print 'Q=%d:'%q1
#     for q2 in range(0,7):
#         print 'Q=%d,Q\'=%d, P=%f'%(q1,q2,PoissonQ(q1,q2))
#     print

# FAILED CASE!
# v_mat, a_mat = MDPOptimization(lam_q_inp=0.0001,penalty_input=0.0)
# ShowActionMatrix(a_mat)

# FAILED CASE TOO
v_mat, a_mat = MDPOptimization(lam_q_inp=0.25,penalty_input=15.0,gamm_inp=0.7,setEtaDirectly = True, eta_inp = 0.9)
ShowActionMatrix(a_mat)