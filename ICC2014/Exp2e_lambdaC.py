'''
Created on Aug 12, 2013

@author: yzhang28
'''
from Headers import *

expnum = 11
lamc_list = [0.00001, 0.0001, 0.0002, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007, 0.0008, 0.0009, 0.001]
total_cost_list_lamc = [-1 for _ in range(expnum)]
act_1_rate_list_lamc = [-1 for _ in range(expnum)]

total_cost_list_lamc_alllocal = [-1 for _ in range(expnum)]
total_cost_list_lamc_allremote = [-1 for _ in range(expnum)]
total_cost_list_lamc_random = [-1 for _ in range(expnum)]
total_cost_list_lamc_myopic = [-1 for _ in range(expnum)]
      
# print "Ready to start..."
# for i in range(expnum):    
#     print "Alive..."
#     lamc = lamc_list[i]
#     v_mat, a_mat = MDPOptimization(penalty_input=20.0, lam_c_inp =lamc, setEtaDirectly=True, eta_inp=0.6)
#     act_1_rate_list_lamc[i], total_N = OffloadingRate(a_mat,getN=True)
#     total_cost_list_lamc[i] = ValueAverage(v_mat)
#        
#     print "   sub-Alive..."
#     v_mat, a_mat = MDPOptimization(penalty_input=20.0, lam_c_inp =lamc, actionflag_inp='AlwaysLocal',setEtaDirectly=True, eta_inp=0.6)
#     total_cost_list_lamc_alllocal[i] = ValueAverage(v_mat)
#     print "   sub-Alive..."
#     v_mat, a_mat = MDPOptimization(penalty_input=20.0, lam_c_inp =lamc, actionflag_inp='AlwaysRemote',setEtaDirectly=True, eta_inp=0.6)
#     total_cost_list_lamc_allremote[i] = ValueAverage(v_mat)
# #     print "   sub-Alive..."
# #     v_mat, a_mat = MDPOptimization(penalty_input=20.0, lam_c_inp =lamc, actionflag_inp='Random',setEtaDirectly=True, eta_inp=0.6)
# #     total_cost_list_lamc_random[i] = ValueAverage(v_mat)    
#     print "   sub-Alive..."
#     v_mat, a_mat = MDPOptimization(penalty_input=20.0, lam_c_inp =lamc, actionflag_inp='Myopic',setEtaDirectly=True, eta_inp=0.6)
#     total_cost_list_lamc_myopic[i] = ValueAverage(v_mat) 
# print "lamc_list=", lamc_list
# print "total_cost_list_lamc=", total_cost_list_lamc
# print "total_cost_list_lamc_alllocal=", total_cost_list_lamc_alllocal
# print "total_cost_list_lamc_allremote=", total_cost_list_lamc_allremote
# # print "total_cost_list_lamc_random=", total_cost_list_lamc_random
# print "total_cost_list_lamc_myopic=", total_cost_list_lamc_myopic
# print "act_1_rate_list_lamc=", act_1_rate_list_lamc

# changed, 10 Aug 2013 
lamc_list= [1e-05, 0.0001, 0.0002, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007, 0.0008, 0.0009, 0.001]
total_cost_list_lamc= [112.90219412266396, 108.24085667130383, 107.67088660472957, 103.66786245486333, 103.07536565967428, 102.46711879414364, 101.84388505531878, 101.20613408589234, 98.102016345471284, 97.457917483668723, 96.806491932378094]
total_cost_list_lamc_alllocal= [115.42793602951228, 115.42788762929932, 115.41435392708919, 115.42867403274538, 115.42617536956514, 115.42106756853111, 115.41206490584807, 115.39769751136929, 115.42720517613014, 115.42518824566829, 115.42214240293013]
total_cost_list_lamc_allremote= [114.77671675471072, 109.84255056068618, 109.60337947113109, 105.60212231746266, 105.29556232040277, 104.95120347671542, 104.57008623989587, 104.15302910458855, 101.06418235639723, 100.60104068705395, 100.11111248614817]
total_cost_list_lamc_myopic= [117.21731138383491, 112.61132178654572, 112.87840634326048, 108.84427683567451, 109.00166670600197, 109.10051851108669, 109.14123982880902, 109.12416386788414, 106.05454275816494, 105.94646942723672, 105.78943790072795]
act_1_rate_list_lamc= [0.3541666666666667, 0.5555555555555556, 0.5555555555555556, 0.65625, 0.65625, 0.65625, 0.65625, 0.65625, 0.7166666666666667, 0.7166666666666667, 0.7166666666666667]


figa = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(lamc_list,act_1_rate_list_lamc,color='red',marker='o')
xlabel('Cloudlet density $\\lambda_c$',fontsize=16)
ylabel('Offloading rate', fontsize=16)
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
# xlim([4,36])
ylim([0.28,0.75])
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)

   
figc = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(lamc_list,total_cost_list_lamc,color='red',marker='o',label='MDP')
plot(lamc_list,total_cost_list_lamc_alllocal,color='black',linestyle='--', fillstyle='none', marker='s',label='LOC')
plot(lamc_list,total_cost_list_lamc_allremote,color='blue',linestyle='--', fillstyle='none', marker='x',label='OFF')
# plot(lamc_list,total_cost_list_lamc_random,color='cyan',linestyle='--', fillstyle='none', marker='^',label='RND')
plot(lamc_list,total_cost_list_lamc_myopic,color='green',linestyle='--', fillstyle='none', marker='^',label='MYO')
xlabel('Cloudlet density $\\lambda_c$',fontsize=16)
ylabel('User\'s avg. cost', fontsize=16)
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
legend(loc='lower left')
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)
# xlim([4,36])
ylim([93,120])
   
show()
print "TERMINATED."