'''
Created on Aug 12, 2013

@author: yzhang28
'''
from Headers import *

expnum = 200+1
lamc_list = [0.00001, 0.0001, 0.0002, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007, 0.0008, 0.0009, 0.001]
lamc_list = [0.00001]
for i in range(0,200+1):
    lamc_list.append(0.0001+i*(0.001-0.0001)/200)
expnum = len(lamc_list)
total_cost_list_lamc = [-1 for _ in range(expnum)]
act_1_rate_list_lamc = [-1 for _ in range(expnum)]
 
total_cost_list_lamc_alllocal = [-1 for _ in range(expnum)]
total_cost_list_lamc_allremote = [-1 for _ in range(expnum)]
total_cost_list_lamc_random = [-1 for _ in range(expnum)]
total_cost_list_lamc_myopic = [-1 for _ in range(expnum)]
       
print "Ready to start..."
for i in range(expnum):    
    print "Alive..."
    lamc = lamc_list[i]
    v_mat, a_mat = MDPOptimization(penalty_input=20.0, lam_c_inp =lamc, setEtaDirectly=True, eta_inp=0.6)
    act_1_rate_list_lamc[i], total_N = OffloadingRate(a_mat,getN=True)
    total_cost_list_lamc[i] = ValueAverage(v_mat)
         
    print "   sub-Alive..."
    v_mat, a_mat = MDPOptimization(penalty_input=20.0, lam_c_inp =lamc, actionflag_inp='AlwaysLocal',setEtaDirectly=True, eta_inp=0.6)
    total_cost_list_lamc_alllocal[i] = ValueAverage(v_mat)
    print "   sub-Alive..."
    v_mat, a_mat = MDPOptimization(penalty_input=20.0, lam_c_inp =lamc, actionflag_inp='AlwaysRemote',setEtaDirectly=True, eta_inp=0.6)
    total_cost_list_lamc_allremote[i] = ValueAverage(v_mat)
#     print "   sub-Alive..."
#     v_mat, a_mat = MDPOptimization(penalty_input=20.0, lam_c_inp =lamc, actionflag_inp='Random',setEtaDirectly=True, eta_inp=0.6)
#     total_cost_list_lamc_random[i] = ValueAverage(v_mat)    
    print "   sub-Alive..."
    v_mat, a_mat = MDPOptimization(penalty_input=20.0, lam_c_inp =lamc, actionflag_inp='Myopic',setEtaDirectly=True, eta_inp=0.6)
    total_cost_list_lamc_myopic[i] = ValueAverage(v_mat) 
print "lamc_list=", lamc_list
print "total_cost_list_lamc=", total_cost_list_lamc
print "total_cost_list_lamc_alllocal=", total_cost_list_lamc_alllocal
print "total_cost_list_lamc_allremote=", total_cost_list_lamc_allremote
# print "total_cost_list_lamc_random=", total_cost_list_lamc_random
print "total_cost_list_lamc_myopic=", total_cost_list_lamc_myopic
print "act_1_rate_list_lamc=", act_1_rate_list_lamc

# # changed, 10 Sep 2013 
# lamc_list= [1e-05, 0.0001, 0.0002, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007, 0.0008, 0.0009, 0.001]
# total_cost_list_lamc= [115.16279123960203, 110.44711862924717, 109.82003028544393, 105.7749612105619, 105.1299640338985, 104.47106188531603, 103.79891936210164, 103.11388716395165, 99.976705338577872, 99.289554136074756, 98.596784386786382]
# total_cost_list_lamc_alllocal= [117.77329775074377, 117.77324575534264, 117.75870690495491, 117.77409057361142, 117.77140631054804, 117.76591913350681, 117.75624790584784, 117.74081380251646, 117.77251260964823, 117.77034586604908, 117.76707379666367]
# total_cost_list_lamc_allremote= [117.01794090470601, 112.0247057955384, 111.71503386797728, 107.66224304098921, 107.29192154776324, 106.88664805890164, 106.44727825318972, 105.9744538594983, 102.84571072859008, 102.33243334298855, 101.79473658980939]
# total_cost_list_lamc_myopic= [119.53400289874759, 114.9153066497679, 115.16468142728149, 111.11467855126405, 111.25389850879496, 111.33385457119873, 111.35492225164846, 111.31738902825002, 108.23279066563177, 108.1042803754526, 107.92641164480736]
# act_1_rate_list_lamc= [0.3541666666666667, 0.5555555555555556, 0.5555555555555556, 0.65625, 0.65625, 0.65625, 0.65625, 0.65625, 0.7166666666666667, 0.7166666666666667, 0.7166666666666667]


figa = plt.figure(figsize=(4.5,4.5))
# grid(True, which="both")
plot(lamc_list,act_1_rate_list_lamc,color='red',marker='o')
xlabel('Cloudlet density $\\lambda_c$',fontsize=16)
ylabel('Offloading rate', fontsize=16)
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
# xlim([4,36])
ylim([0.28,0.75])
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)

   
figc = plt.figure(figsize=(4.5,4.5))
# grid(True, which="both")
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
ylim([97,120])
   
show()
print "TERMINATED."