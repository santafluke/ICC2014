'''
Created on Aug 5, 2013

@author: yzhang28
'''

from Headers import *

################################################################################bofA
#                                THE 2st EXP
#                               Different Rs
################################################################################
expnum = 8
R_list = [1.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0]
total_cost_list_R = [-1 for _ in range(expnum)]
total_N_list_R = [-1 for _ in range(expnum)]
act_1_rate_list_R = [-1 for _ in range(expnum)]
      
total_cost_list_R_alllocal = [-1 for _ in range(expnum)]
total_cost_list_R_allremote = [-1 for _ in range(expnum)]
total_cost_list_R_random = [-1 for _ in range(expnum)]
total_cost_list_R_myopic = [-1 for _ in range(expnum)]
      
# print "Ready to start..."
# for i in range(expnum):    
#     print "Alive..."
#     R_clt = R_list[i]
#     v_mat, a_mat = MDPOptimization(penalty_input=20.0, R_clt_inp = R_clt,setEtaDirectly=True, eta_inp=0.6)
#     act_1_rate_list_R[i], total_N = OffloadingRate(a_mat,getN=True)
#     total_cost_list_R[i] = ValueAverage(v_mat)
#     total_N_list_R[i] = total_N/(6*4) # Q_max=6, G_max=4
#        
#     print "   sub-Alive..."
#     v_mat, a_mat = MDPOptimization(penalty_input=20.0, R_clt_inp = R_clt,actionflag_inp='AlwaysLocal',setEtaDirectly=True, eta_inp=0.6)
#     total_cost_list_R_alllocal[i] = ValueAverage(v_mat)
#     print "   sub-Alive..."
#     v_mat, a_mat = MDPOptimization(penalty_input=20.0, R_clt_inp = R_clt,actionflag_inp='AlwaysRemote',setEtaDirectly=True, eta_inp=0.6)
#     total_cost_list_R_allremote[i] = ValueAverage(v_mat)
#     print "   sub-Alive..."
#     v_mat, a_mat = MDPOptimization(penalty_input=20.0, R_clt_inp = R_clt,actionflag_inp='Random',setEtaDirectly=True, eta_inp=0.6)
#     total_cost_list_R_random[i] = ValueAverage(v_mat)    
#     print "   sub-Alive..."
#     v_mat, a_mat = MDPOptimization(penalty_input=20.0, R_clt_inp = R_clt,actionflag_inp='Myopic',setEtaDirectly=True, eta_inp=0.6)
#     total_cost_list_R_myopic[i] = ValueAverage(v_mat) 
# print "R_list=", R_list
# print "total_cost_list_R=", total_cost_list_R
# print "total_cost_list_R_alllocal=", total_cost_list_R_alllocal
# print "total_cost_list_R_allremote=", total_cost_list_R_allremote
# print "total_cost_list_R_random=", total_cost_list_R_random
# print "total_cost_list_R_myopic=", total_cost_list_R_myopic
# print "total_N_list_R=", total_N_list_R
# print "act_1_rate_list_R=", act_1_rate_list_R

# # changed, 10 Aug 2013 
# R_list= [1.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0]
# total_cost_list_R= [112.95168395575058, 112.8132337211497, 108.24085667130383, 107.52304036139986, 103.07536565967428, 101.68579585507598, 97.457917483668723, 95.317965018927069]
# total_cost_list_R_alllocal= [115.42985458375288, 115.41780065652591, 115.42788762929932, 115.40790659030566, 115.42617536956514, 115.40903699940702, 115.42518824566829, 115.4097579405657]
# total_cost_list_R_allremote= [114.7933829345248, 114.74198302304224, 109.84255056068618, 109.53464586026558, 105.29556232040277, 104.4691634220746, 100.60104068705395, 98.91819337198848]
# total_cost_list_R_random= [114.80238561475085, 114.86797664500774, 112.03877511816277, 113.34297087858828, 110.61433469388344, 107.92329579749311, 109.0229508671539, 104.45104263871779]
# total_cost_list_R_myopic= [117.18595385868763, 117.26223278018955, 112.61132178654572, 112.9332407483645, 109.00166670600197, 109.1423777014068, 105.94646942723672, 105.26472950121423]
# total_N_list_R= [2, 2, 3, 3, 4, 4, 5, 5]
# act_1_rate_list_R= [0.3541666666666667, 0.3541666666666667, 0.5555555555555556, 0.5555555555555556, 0.65625, 0.65625, 0.7166666666666667, 0.7166666666666667]

# Sep 10 2013
R_list= [1.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0]
total_cost_list_R= [115.21774638870635, 115.064298140689, 110.44711862924717, 109.65803471812212, 105.1299640338985, 103.62886182870936, 99.289554136074756, 97.021076606779616]
total_cost_list_R_alllocal= [117.77535881889121, 117.76240959636688, 117.77324575534264, 117.75178082315499, 117.77140631054804, 117.75299516583107, 117.77034586604908, 117.75376963833973]
total_cost_list_R_allremote= [117.04142425600726, 116.97144973553183, 112.0247057955384, 111.62899628315824, 107.29192154776324, 106.33218761919164, 102.33243334298855, 100.50232985950427]
total_cost_list_R_random= [118.11582511292438, 117.4231282628192, 115.65037053720965, 113.40319723361635, 114.0001394752896, 110.42753193719467, 109.2284880698744, 107.40777216082951]
total_cost_list_R_myopic= [119.50419958935409, 119.57583531637952, 114.9153066497679, 115.21477953288672, 111.25389850879496, 111.35102310791625, 108.1042803754526, 107.35344930820833]
total_N_list_R= [2, 2, 3, 3, 4, 4, 5, 5]
act_1_rate_list_R= [0.3541666666666667, 0.3541666666666667, 0.5555555555555556, 0.5555555555555556, 0.65625, 0.65625, 0.7166666666666667, 0.7166666666666667]

figa = plt.figure(figsize=(4.5,4.5))
# grid(True, which="both")
plot(R_list,act_1_rate_list_R,color='red',marker='o')
xlabel('Cloudlet coverage radius $R$',fontsize=16)
ylabel('Offloading rate',fontsize=16)
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
# xlim([4,36])
ylim([0.30,0.75])
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)
   
figb = plt.figure(figsize=(4.5,4.5))
# grid(True, which="both")
plot(R_list,total_N_list_R,color='red',marker='o')
xlabel('Cloudlet coverage radius $R$',fontsize=16)
ylabel('Maxmum number of cloudlets',fontsize=16)
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)
# xlim([4,36])
#ylim([1,8])
   
figc = plt.figure(figsize=(4.5,4.5))
# grid(True, which="both")
plot(R_list,total_cost_list_R,color='red',marker='o',label='MDP')
plot(R_list,total_cost_list_R_alllocal,color='black',linestyle='--',fillstyle='none',marker='s',label='LOC')
plot(R_list,total_cost_list_R_allremote,color='blue',linestyle='--',fillstyle='none',marker='x',label='OFF')
# plot(R_list,total_cost_list_R_random,color='cyan',linestyle='--',fillstyle='none',marker='^',label='RND')
plot(R_list,total_cost_list_R_myopic,color='green',linestyle='--',fillstyle='none',marker='^',label='MYO')
xlabel('Cloudlet coverage radius $R$',fontsize=16)
ylabel('User\'s avg. cost',fontsize=16)
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
legend(loc='lower left')
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)
# xlim([4,36])
#ylim([30,90])
   
show()
print "TERMINATED."
