'''
Created on Aug 5, 2013

@author: yzhang28
'''

from Headers import *

################################################################################
#                                THE 4th EXP
#                        Different initial queue params
################################################################################
# q = [1,2,3,4,5,6]
# total_cost_list = [-1 for _ in range(len(q))]
# total_cost_list_alllocal = [-1 for _ in range(len(q))]
# total_cost_list_allremote = [-1 for _ in range(len(q))]
# total_cost_list_random = [-1 for _ in range(len(q))]
#  
# v_mat, a_mat = MDPOptimization()
# print "Alive!"
# v_mat_alllocal, a_mat_alllocal = MDPOptimization(actionflag_inp='AlwaysLocal',penalty_input=15.0)
# print "Alive!"
# v_mat_allremote, a_mat_allremote = MDPOptimization(actionflag_inp='AlwaysRemote',penalty_input=15.0)
# print "Alive!"
# v_mat_random, a_mat_random = MDPOptimization(actionflag_inp='Random',penalty_input=15.0)
# for i,elem in enumerate(q):
#     total_cost_list[i]=ValueOf(v_mat,1,elem,1)
#     total_cost_list_alllocal[i]=ValueOf(v_mat_alllocal,1,elem,1)
#     total_cost_list_allremote[i]=ValueOf(v_mat_allremote,1,elem,1)
#     total_cost_list_random[i]=ValueOf(v_mat_random,1,elem,1)
#  
# print 'q=',q
# print 'total_cost_list=', total_cost_list
# print 'total_cost_list_alllocal=', total_cost_list_alllocal
# print 'total_cost_list_allremote=', total_cost_list_allremote
# print 'total_cost_list_random=', total_cost_list_random


q= [1, 2, 3, 4, 5, 6]
total_cost_list= [61.051651575396221, 83.299998863009066, 92.283143093395068, 96.425602048017751, 98.66102294421384, 99.746772531526673]
total_cost_list_alllocal= [68.68821394323389, 95.540314454184823, 106.71964786824056, 111.99337389668624, 114.88630035418224, 116.32934086863747]
total_cost_list_allremote= [62.109267468286234, 84.673560309751792, 93.771082854026446, 97.95488070017872, 100.20496390337036, 101.29508030569778]
total_cost_list_random= [63.196342347720105, 86.816075891111112, 97.72549128061749, 101.0487557148674, 108.57621862217299, 108.04464747429144]

figa = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(q,total_cost_list,color='red',marker='o')
plot(q,total_cost_list_alllocal,color='black',linestyle='--',marker='x')
plot(q,total_cost_list_allremote,color='blue',linestyle='--',marker='x')
plot(q,total_cost_list_random,color='green',linestyle='--',marker='x')
xlabel('Initial queue length')
ylabel('User\'s cost at (1,Q,1)')
subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
# xlim([0.0,0.41])
# #ylim([30,90])
  
show()