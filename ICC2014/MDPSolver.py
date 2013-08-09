'''
Main File

Created on Jul 5, 2013

@author: yzhang28
'''

import numpy as np
import scipy as sp
from scipy.misc import factorial
import math
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import FuncFormatter
from copy import deepcopy
import random


def MDPOptimization(Q_max_inp=1+6, #[0(dumb), 123456], (Q_max_CONST-1) IS the upper bound
                    G_max_inp=1+4,  #[0(dumb), 1234], (G_max-1) IS the upper bound
                    R_clt_inp=10,
                    penalty_input = 10.0,
                    lam_q_inp=0.25,
                    lam_c_inp = 0.0001,
                    aph_r_inp = 1.0,
                    aph_l_inp = 1.0,
                    gamm_inp = 0.8,
                    actionflag_inp = '',
                    isRndThreshold = False,
                    setEtaDirectly = False,
                    eta_inp = 1.0,
                    epsilon_input = 0.8):
    '''
    =================================================================================================
    Functions and definitions
    =================================================================================================
    '''
    
    '''
    INITIALIZATION
    '''
    #original values, CONSTANTS
    Q_max_CONST = Q_max_inp
    G_max_CONST = G_max_inp
    R_clt_CONST = R_clt_inp
    lam_q_CONST = lam_q_inp
    lam_c_CONST = lam_c_inp #NOTE THAT: -pi*R^2*lam_c << 1 is a pre-condition
    aph_r_CONST = aph_r_inp
    aph_l_CONST = aph_l_inp
    gamm_CONST = gamm_inp
    actionflag_CONST = actionflag_inp
    #original values end
    
    '''
    Pre-defined function:
    N # of cloudlets trans matrix forming function
    '''
    def PNTransProb(N1=0, N2=0):
        def P_NPoisson(k=0):
            return np.exp(-1*math.pi*lam_c_CONST*np.power(R_clt_CONST,2))*np.power(math.pi*lam_c_CONST*np.power(R_clt_CONST,2), k)/factorial(k, exact=True)
        def AppxSumToOne(N2=0):
            '''
            summation of P^{N}(0), P^{N}(1), to P^{N}(N2)
            The function is used to check if P^{N}(N2+1) should be neglected  
            '''
            if N2<0:
                return 0
            else:
                return P_NPoisson(N2) + AppxSumToOne(N2-1) 
        if 1.0-AppxSumToOne(N2-1)<0.0001:
            return 0
        else:
            return P_NPoisson(N2)

    def NMaxFunc():
        for i in range(65535):
            if PNTransProb(0,i)==0:
                return i-1+1
     
    N_max = NMaxFunc() # N starts from ZERO! [0,1,2,...N_max-1]
    epsilon = epsilon_input
    tau = 0.05
    velocity = 1.0
    def ETAAvail(v=0.0,R=10.0):
        return epsilon*(1-3*v*tau/(2*R_clt_CONST))
    
    if setEtaDirectly==False:
        eta_CONST = ETAAvail(velocity,R_clt_CONST)
    else:
        eta_CONST = eta_inp
    
    '''
    Pre-defined functions:
    WHETHER THE PHASE IS FINISHING PHASE
    '''
    def ESg(g):
        if 3==g or 4==g:
            return True
        else:
            return False
        
    '''
    Pre-defined functions:
    COSTS
    '''
    def BaseCostG(G=-1):
#         baseG = [0,    0.01,0.1,0.2,0.15] #[0, 1234]
        baseG = [0,   0.1, 0.1, 10.0, 0.01] # in KBs
        #baseG = [0,   0.1*1000, 0.1*1000, 10.0*1000, 0.01*1000] # in MBs
        if -1==G:
            print "error in FUNCTION: BaseCostG(G)"
            exit()
        else:
            return baseG[G]
    
    
    def c_r(G, Q, N, act): # Cost of pure remote execution
        if 0==G or 0==Q:
            return 0
        if 0==N or 0.0==eta_CONST:
            return 2**256 # NO WAY TO OFFLOAD SINCE N==0
        if 1==act: # Remote execution
			return (1.0+((1.0-eta_CONST)**N)*penalty_input)*BaseCostG(G) #The second term is Penalty
            # print 'NOTE THAT COST OF OFFLOADING HAS CHANGED'
            # return (10.0+((1.0-eta_CONST)**N)*penalty_input)*BaseCostG(G) #The second term is Penalty
            #return 1.0
        else:
            return 0

    def c_l(G, Q, N, act): # Cost of pure local execution
        def coef_local_G(G):
            if BaseCostG(G)<=0.011:
                return 1.0
            elif BaseCostG(G)>0.011 and BaseCostG(G)<=1.0:
                return 2.0
            elif BaseCostG(G)>1.0:
                return 10.0
                
        if 0==G or 0==Q:
            return 0
        if (Q_max_CONST-Q)==0:
            print "WARNING, DIVIDING ZERO! in cl(...)"
        if 0==act: # Local execution
#             print 'NOTE THAT COST OF LOCALEXECUTION HAS CHANGED'
            return (coef_local_G(G) + (Q*1.0)/((Q_max_CONST-1)*1.0))*BaseCostG(G)
        else:
            return 0
    
    def ShowActionMatrix(act_m,G=-1):
        if -1==G: #default
            for g in range(1,G_max_CONST):
                print 'State G=', g
                for q in range(1,Q_max_CONST):
                    for n in range(N_max):
                        print 'Q',q,'| N',n,'| ACT',act_m[g][q][n],",",
                    print
                print
            print
        #elif 0==G:
        #    print "ERROR, G=0 is an empty phase state. FUNCTION:ShowActionMatrix()"
        else:
            # Print the threshold graph for given phase G
            print 'G =', G
            print 'Q in lines, N in rows:'
            for q in range(1,Q_max_CONST):
                for n in range(N_max):
                    print act_m[G][q][n],
                print

    '''
    Pre-defined function:
    G Q N combined transition function
    '''
    def PGQNTransProb(G1=0, Q1=0, N1=0, G2=0, Q2=0, N2=0, ACT=0):        
        '''
        not important
        Pre-defined functions:
        G PHASE trans prob
        '''
        def PGOnlyTransProb(g1=0, g2=0):
            pg_matrix = np.array([
            #G2=  0    1    2    3    4
                [0.0, 0.0, 0.0, 0.0, 0.0], # G1=0
                [0.0, 0.0, 1.0, 0.0, 0.0], #    1
                [0.0, 0.0, 0.0, 0.8, 0.2], #    2
                [0.0, 0.0, 0.0, 0.0, 0.0], #    3
                [0.0, 0.0, 0.0, 0.0, 0.0]  #    4
                ])
                #             ___ 3 
                #            |
                #  1 -- 2 ---<
                #            |___ 4
                #
            return pg_matrix[g1][g2]
    
        '''
        Pre-defined functions:
        Successful prob caused by eta_CONST
        '''
        def ProbETA(n1,eta1,act1):
            if 0==act1:
                return 1
            else: # when act==1
                return 1.0-np.power((1.0-eta1),n1)
                
    
        def PGQTransProb(g1=0,q1=0, g2=0,q2=0, n1=0,act1=0):  #P^{G,Q}((G,Q),(G',Q') | N,Act)
            #1
            if g1>0 and ESg(g1)==False and g1!=g2 and 0<q1 and q1<(Q_max_CONST-1) and q1<=q2 and q2<(Q_max_CONST-1):
                return ProbETA(n1,eta_CONST,act1)*PGOnlyTransProb(g1,g2)*np.exp(-1*lam_q_CONST)*np.power(lam_q_CONST,q2-q1)/factorial(q2-q1,exact=True)
            #2
            if g1>0 and ESg(g1)==False and g1!=g2 and 0<q1 and q1<(Q_max_CONST-1) and (Q_max_CONST-1)==q2:
                sum_tmp = 0.0
                for k in range(q1,Q_max_CONST-1): #\mathcal{Q},\mathcal{Q}+1,...,(Q_max_CONST-1)-1 (i.e., Q-1)
                    sum_tmp = sum_tmp + np.exp(-1*lam_q_CONST)*np.power(lam_q_CONST,(k-q1))/factorial((k-q1),exact=True)
                tmp = ProbETA(n1,eta_CONST,act1)*PGOnlyTransProb(g1,g2)*(1.0-sum_tmp)
                return tmp
            #3
            if g1>0 and ESg(g1)==False and g1!=g2 and (Q_max_CONST-1)==q1 and (Q_max_CONST-1)==q2:
                return ProbETA(n1,eta_CONST,act1)*PGOnlyTransProb(g1,g2)
            #4
            if g1>0 and g1==g2 and 0<q1 and q1<(Q_max_CONST-1) and q1<=q2 and q2<(Q_max_CONST-1):
                return (1.0-ProbETA(n1,eta_CONST,act1))*np.exp(-1*lam_q_CONST)*np.power(lam_q_CONST,q2-q1)/factorial(q2-q1,exact=True)
            #5
            if g1>0 and g1==g2 and 0<q1 and q1<(Q_max_CONST-1) and (Q_max_CONST-1)==q2:
                sum_tmp = 0.0
                for k in range(q1,Q_max_CONST-1):
                    sum_tmp = sum_tmp + np.exp(-1*lam_q_CONST)*np.power(lam_q_CONST,(k-q1))/factorial((k-q1),exact=True)
                tmp = (1.0-ProbETA(n1,eta_CONST,act1))*(1.0-sum_tmp)
                return tmp
            #6
            if g1>0 and g1==g2 and (Q_max_CONST-1)==q1 and (Q_max_CONST-1)==q2:
                return 1.0-ProbETA(n1,eta_CONST,act1)
            
            #7
            if ESg(g1)==True and 1==q1 and 0==g2 and 0==q2:
                return ProbETA(n1,eta_CONST,act1)
            #8
            if ESg(g1)==True and q1>1 and q1<=(Q_max_CONST-1) and 1==g2 and q2==(q1-1):
                return ProbETA(n1,eta_CONST,act1)
            #9
            else:
                return 0
        #
        # Then, return P^{G,Q,N}((G,Q,N),(G',Q',N'))
        #
        if G1>(G_max_CONST-1) or G2>(G_max_CONST-1) or Q1>(Q_max_CONST-1) or Q2>(Q_max_CONST-1) or N1>(N_max-1) or N2>(N_max-1):
            print "my error signal, out of bound"
            return -1
        else:
            return PGQTransProb(G1,Q1, G2,Q2, N1,ACT)*PNTransProb(N1,N2)
    '''
    =================================================================================================
    END: Functions and definitions
    =================================================================================================
    '''
    
    
    '''
    =================================================================================================
    SOLVING THE PROBLEM BY DYNAMIC PROGRAMMING
    =================================================================================================
    '''
    ############################################################################
    ############################################################################
    ############################################################################
    #                                CORE                                      #
    ############################################################################
    ############################################################################
    ############################################################################
    def DynaProgSolve(actionflag_CONST=''):
        def cost_inside(g1,q1,n1,act): 
            return aph_r_CONST*act*c_r(g1,q1,n1,act) + aph_l_CONST*(1-act)*c_l(g1,q1,n1,act)
        
        #init
        v_matrix = [[[0.0 for _ in range(N_max)] for _ in range(Q_max_CONST)] for _ in range(G_max_CONST)]
        act_matrix = [[[0 for _ in range(N_max)] for _ in range(Q_max_CONST)] for _ in range(G_max_CONST)]
        # act_rand_matrix if we choose to randomize the user's actions
        act_rand_matrix_preset = [[[random.randint(0,1) for _ in range(N_max)]for _ in range(Q_max_CONST)] for _ in range(G_max_CONST)]
        #iteration
#         for g1 in range(1,G_max_CONST):               #
#                 for q1 in range(1,Q_max_CONST):       # s \in S
#                     for n1 in range(N_max):           #
#                         v_matrix[g1][q1][n1] = cost_inside(g1,q1,n1,0)
        
        k = 1
        v_s = 0
        v_old = 0
        while 1:
            delta = 0.0
            stable = True
            for g1 in reversed(range(1,G_max_CONST)):           #
                for q1 in reversed(range(1,Q_max_CONST)):       # s \in S
                    for n1 in reversed(range(N_max)):   #
                        v_old = v_matrix[g1][q1][n1]
                        act_old = act_matrix[g1][q1][n1]
                        # Policy
                        vsum = 0.0
                        act = 0
                        tmp_sum_act_0 = 0.0
                        tmp_sum_act_1 = 0.0
                        for g2 in range(1,G_max_CONST):            #
                            for q2 in range(1,Q_max_CONST):        # s', a=0/a=1
                                for n2 in range(N_max):      #
                                    tmp_sum_act_0 = tmp_sum_act_0 + PGQNTransProb(g1,q1,n1, g2,q2,n2, 0) * v_matrix[g2][q2][n2]
                                    tmp_sum_act_1 = tmp_sum_act_1 + PGQNTransProb(g1,q1,n1, g2,q2,n2, 1) * v_matrix[g2][q2][n2]
                                    # ########## FOR TEST ##########
                                    # if g1==2 and q1==1 and n1==1: #########################################################################
                                        # f = open('../runningrecords'+str(g1)+str(q1)+str(n1)+str(lam_q_CONST)+'.txt', 'a')
                                        # f.write('  ROUND %d. lambda_q=%f\n'%(k, lam_q_CONST))
                                        # f.write('  (G=%d,Q=%d,N=%d) to (G\'=%d,Q\'=%d,N\'=%d)\n'%(g1,q1,n1, g2,q2,n2))
                                        # f.write('   - Act 0: P*V\' = %f * %f = %f\n' %(PGQNTransProb(g1,q1,n1, g2,q2,n2, 0), v_matrix[g2][q2][n2], PGQNTransProb(g1,q1,n1, g2,q2,n2, 0)*v_matrix[g2][q2][n2]))
                                        # f.write('   - Act 1: P*V\' = %f * %f = %f\n' %(PGQNTransProb(g1,q1,n1, g2,q2,n2, 1), v_matrix[g2][q2][n2], PGQNTransProb(g1,q1,n1, g2,q2,n2, 1)*v_matrix[g2][q2][n2]))
                                        # f.write('   - tmp_sum_act_0=%f, tmp_sum_act_1=%f'%(tmp_sum_act_0,tmp_sum_act_1))
                                        # f.write('\n')
                                        # f.close()
                        vsum_act_0 = cost_inside(g1,q1,n1,0) + gamm_CONST * tmp_sum_act_0
                        vsum_act_1 = cost_inside(g1,q1,n1,1) + gamm_CONST * tmp_sum_act_1        
                        if vsum_act_0<=vsum_act_1:
                            act = 0
                            vsum = vsum_act_0
                        else: # vsum_act_0>vsum_act_1
                            act = 1
                            vsum = vsum_act_1
                        # ########## FOR TEST ##########
                        # if g1==2 and q1==1 and n1==1: #########################################################################
                            # f = open('../runningrecords'+str(g1)+str(q1)+str(n1)+str(lam_q_CONST)+'.txt', 'a')
                            # f.write('ROUND %d. lambda_q=%f\n'%(k, lam_q_CONST))
                            # f.write('SUM THEM ALL: V(G=%d,Q=%d,N=%d)\n'%(g1,q1,n1))
                            # f.write('Act 0: Cost(0) + gamm*PV\' = %f + %f * %f= %f\n' %(cost_inside(g1,q1,n1,0),gamm_CONST,tmp_sum_act_0,vsum_act_0))
                            # f.write('Act 1: Cost(1) + gamm*PV\' = %f + %f * %f= %f\n' %(cost_inside(g1,q1,n1,1),gamm_CONST,tmp_sum_act_1,vsum_act_1))
                            # ('ACT=%d TAKEN, vsum=%f'%(act,vsum))
                            # f.write('\n\n')
                            # f.close()
                        # Special offloading schemes, just for comparisons in experiments
                        if actionflag_CONST=='AlwaysLocal':
                            act_matrix[g1][q1][n1] = 0
                            vsum = vsum_act_0
                        elif actionflag_CONST=='AlwaysRemote':
                            if n1!=0:
                                act_matrix[g1][q1][n1] = 1
                                vsum = vsum_act_1
                            else:
                                act_matrix[g1][q1][n1] = 0
                                vsum = vsum_act_0
                        elif actionflag_CONST=='Random':
                            if 0==n1:
                                act_rand_matrix_preset[g1][q1][n1] = 0
                            act_matrix[g1][q1][n1] = act_rand_matrix_preset[g1][q1][n1]
                            if 1==act_matrix[g1][q1][n1]:
                                vsum = vsum_act_1
                            else:
                                vsum = vsum_act_0
                        elif actionflag_CONST=='Myopic':
							if cost_inside(g1,q1,n1,0) <= cost_inside(g1,q1,n1,1):
								act_matrix[g1][q1][n1] = 0
								vsum = vsum_act_0
							else:
								act_matrix[g1][q1][n1] = 1
								vsum = vsum_act_1
                        # END. Special offloading schemes, just for comparisons in experiments    
                        if 0==g1 or 0==q1:
                            vsum = 0.0
                            act = 0
                        if 0==eta_CONST:
                            act = 0
                            vsum = vsum_act_0
                            
                        act_matrix[g1][q1][n1] = act
                        v_matrix[g1][q1][n1] = vsum
                        # ########## FOR TEST ##########
                        # if g1==2 and q1==1 and n1==1: #########################################################################
                            # f = open('../vmatrix'+str(g1)+str(q1)+str(n1)+str(lam_q_CONST)+'.txt', 'a')
                            # if delta>=np.fabs(vsum-v_old):
                                # f.write('ROUND %d. V matrix.(G=%d,Q=%d,N=%d) UPDATED\n'%(k,g1,q1,n1))
                            # else:
                                # f.write('ROUND %d. V matrix.(G=%d,Q=%d,N=%d) DID NOT update\n'%(k,g1,q1,n1))
                            # for i_g,dim1 in enumerate(v_matrix):
                                # f.write('State G=%d\n'%(i_g))
                                # for i_q,dim2 in enumerate(dim1):
                                    # for i_n,elem in enumerate(dim2):
                                        # f.write('Q%d-N%d, V=%f   ' %(i_q,i_n,elem))
                                    # f.write('\n')
                                # f.write('\n')
                            # f.write('\n')
                            # f.close()
                            # 
                            # f = open('../amatrix'+str(g1)+str(q1)+str(n1)+'.txt', 'a')
                            # if act == act_old:
                                # f.write('ROUND %d. A matrix.(G=%d,Q=%d,N=%d) DID NOT update\n'%(k,g1,q1,n1))
                            # else:
                                # f.write('ROUND %d. A matrix.(G=%d,Q=%d,N=%d) UPDATED\n'%(k,g1,q1,n1))
                            # for i_g,dim1 in enumerate(act_matrix):
                                # f.write('State G=%d\n'%(i_g))
                                # for i_q,dim2 in enumerate(dim1):
                                    # for i_n,elem in enumerate(dim2):
                                        # f.write('Q%d-N%d, ACT=%d   ' %(i_q,i_n,elem))
                                    # f.write('\n')
                                # f.write('\n')
                            # f.write('\n')
                            # f.close()
                            
                        delta = delta if delta>=np.fabs(vsum-v_old) else np.fabs(vsum-v_old)
                        stable = (act == act_old) or stable
                        k = k + 1
            if delta<0.0001 and stable==True:
                return v_matrix, act_matrix
                
    ############################################################################
    ############################################################################
    ############################################################################
    #                                CORE ENDS                                 #
    ############################################################################
    ############################################################################
    ############################################################################
    
    
    #
    # Randomized action scheme for illustrating threshold situations
    #
    def DynaProgSolveEvaluation():
        def cost_inside(g1,q1,n1,act1): 
            return aph_r_CONST*act1*c_r(g1,q1,n1,act1) + aph_l_CONST*(1-act1)*c_l(g1,q1,n1,act1)
        
        def v_average(v_mat):
            sum_tmp = 0.0
            count_index = 0
            for g,dim1 in enumerate(v_mat):
                for q,dim2 in enumerate(dim1):
                    for dim3 in dim2:
                        if g!=0 or q!=0:
                            sum_tmp = sum_tmp + dim3
                            count_index = count_index + 1
            return 1.0*sum_tmp / (1.0*count_index)
        
        #init
        v_matrix = None
        v_rnd_matrix = [[[0.0 for dim3 in range(N_max)]for dim2 in range(Q_max_CONST)] for dim1 in range(G_max_CONST)]
        act_matrix = [[[0 for dim3 in range(N_max)]for dim2 in range(Q_max_CONST)] for dim1 in range(G_max_CONST)]
        for i_g in range(G_max_CONST):
            for i_q in range(Q_max_CONST):
                for i_n in range(N_max):
                    if 0==i_g or 0==i_q:
                        act_matrix[i_g][i_q][i_n] = 0
        #iteration
    
        print "...........ready for the loop.."        
        stop_count = 0
        v_current_max = 13800138000.0
        while stop_count<=999:
            act_rnd_matrix = deepcopy(act_matrix)
            cnt = np.random.choice([1,2,3,4])
            for i in range(cnt):
                g_rnd = np.random.randint(1,G_max_CONST)
                q_rnd = np.random.randint(1,Q_max_CONST)
                n_rnd = np.random.randint(0,N_max)
                act_rnd_matrix[g_rnd][q_rnd][n_rnd] = int(np.fabs(1-act_rnd_matrix[g_rnd][q_rnd][n_rnd]))
            ShowActionMatrix(act_rnd_matrix,1)
            print "**********************************************"
            while 1:
                delta = 0.0
                for g1 in range(1,G_max_CONST):           #
                    for q1 in range(1,Q_max_CONST):       # s \in S
                        for n1 in range(N_max):     #
                            v_old = v_rnd_matrix[g1][q1][n1]
                            # Policy
                            vsum = 0.0
                            for g2 in range(1,G_max_CONST):            #
                                for q2 in range(1,Q_max_CONST):        # s', a=0/a=1
                                    for n2 in range(N_max):      #
                                        vsum = vsum + PGQNTransProb(g1,q1,n1, g2,q2,n2, act_rnd_matrix[g1][q1][n1])*(cost_inside(g1,q1,n1,act_rnd_matrix[g1][q1][n1])+gamm_CONST*v_rnd_matrix[g2][q2][n2])
                            if 0==g1 or 0==q1:
                                vsum = 0.0
                            v_s = vsum
                            v_rnd_matrix[g1][q1][n1] = v_s
                            delta = delta if delta>=np.fabs(v_s-v_old) else np.fabs(v_s-v_old)
                if delta<0.001:
                    if v_average(v_rnd_matrix)<=v_current_max:
                        act_matrix = deepcopy(act_rnd_matrix)
                        v_matrix = deepcopy(v_rnd_matrix)
                        v_current_max = v_average(v_matrix)
                        stop_count = 0
                        ShowActionMatrix(act_matrix,1)
                        print "Cost:",v_average(v_matrix), "Renewed."
                    else:
                        stop_count = stop_count + 1
                        ShowActionMatrix(act_matrix,1)
                        print "Cost:",v_average(v_matrix),"No renewal."
                    break
        
        print "...........ready for the 2nd loop.."
        v_mat_compare, a_mat_compare = MDPOptimization(Q_max_inp=1+4, R_clt_inp=10, isRndThreshold = False, setEtaDirectly = True, eta_inp = 0.7, penalty_input=10.0)                    
            
        cost_rand = v_average(v_matrix)
        cost_compare = v_average(v_mat_compare)
        print "--------begin--------"
        print "Rand matrix:"
        ShowActionMatrix(act_matrix,1) # print the threshold matrix
        print "- - -"
        print "MDP matrix"
        ShowActionMatrix(a_mat_compare,1) # print the threshold matrix
        print "The rand results:", cost_rand
        print "The Opt results:", cost_compare
        if cost_rand>cost_compare:
            print "IDEAL RESULT"
        else:
            print "BAD RESULT!"
        print "-------- end --------"
        print
    
    '''
    =================================================================================================
    END: SOLVING THE PROBLEM BY DYNAMIC PROGRAMMING
    =================================================================================================
    '''
    if isRndThreshold==False: # Normal experiments
        return DynaProgSolve(actionflag_CONST)
    elif isRndThreshold: # Random scheme to show the thresholds' existance
        DynaProgSolveEvaluation()
