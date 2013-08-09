'''
Created on Aug 5, 2013

@author: yzhang28
'''

from Headers import *


################################################################################
#                                THE 1st EXP
#                           Different weight factors
################################################################################
# coef_list = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
# total_cost_list_r = [-1 for _ in range(len(coef_list))]
# act_1_rate_list_r = [-1 for _ in range(len(coef_list))]
# #total_cost_list_l = [-1 for _ in range(len(coef_list))]
# #act_1_rate_list_l = [-1 for _ in range(len(coef_list))]
# total_cost_list_compare = [-1 for _ in range(len(coef_list))]
# act_1_rate_list_compare = [-1 for _ in range(len(coef_list))]
# print '-----------------------'
# for i in range(len(coef_list)):
#     aph_r = coef_list[i]
#     aph_l = 1.0
#     print "REMOTE coef changing..."
#     v_mat, a_mat = MDPOptimization(aph_r_inp=aph_r,aph_l_inp=aph_l)
#     act_1_rate_list_r[i], total_N = OffloadingRate(a_mat,getN=True)
#     total_cost_list_r[i] = ValueOf(v_mat, 1,1,0)
#     print '-'
#         
#     #aph_r = 0.5
#     #aph_l = coef_list[i]
#     #print "LOCAL coef changing..."
#     #total_cost, act_1_rate, total_N = MDPOptimization(aph_r_inp=aph_r,aph_l_inp=aph_l)
#     #total_cost_list_l[i] = total_cost 
#     #act_1_rate_list_l[i] = act_1_rate
#     #print '-----------------------'
#   
#     aph_r = coef_list[i]
#     aph_l = 1.0
#     v_mat, a_mat = MDPOptimization(aph_r_inp=aph_r,aph_l_inp=aph_l)
#     #act_1_rate_list_compare[i], total_N = OffloadingRate(a_mat,getN=True)
#     total_cost_list_compare[i] = ValueOf(v_mat, 1,1,0)
#     print '-----------------------'
# print coef_list
# print "Action 1 rate (a_r changing)", act_1_rate_list_r
# print "Total Average Cost (a_r changing)", total_cost_list_r
# #print "Total Average Cost (a_l changing)", total_cost_list_l
# #print "Action 1 rate (a_l changing)", act_1_rate_list_l
# print "Total Average Cost (Compare)", total_cost_list_compare
# 
# figa = plt.figure(figsize=(4.5,4.5))
# grid(True, which="both")
# plot(coef_list,act_1_rate_list_r,color='red',marker='o',label="$\\alpha_l=1.0$, changing $\\alpha_r$")
# subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
# xlabel('Weight factor $\\alpha_r$')
# ylabel('Rate of offloading decisions')
# legend(loc='lower left')
# #plot(coef_list,act_1_rate_list_l,color='blue',marker='x')
# xlim([0.0,10.1])
# ylim([0.0,0.75])
#   
# figb = plt.figure(figsize=(4.5,4.5))
# grid(True, which="both")
# plot(coef_list,total_cost_list_r,color='red',marker='o',label="MDP")
# plot(coef_list,total_cost_list_compare,color='blue',linestyle='--',marker='x',label="Always offload")
# xlim([0.0,10.1])
# ylim([25,38.5])
# subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
# xlabel('Weight factor $\\alpha_r$')
# ylabel("User\'s cost at state (1,1,0)")
# legend(loc='upper left')
# show()
# print "TERMINATED."