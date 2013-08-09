'''
Created on Aug 5, 2013

@author: yzhang28
'''

from Headers import *

################################################################################
#                                THE 2st EXP
#                               Different Rs
################################################################################
# expnum = 8
# R_list = [1.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0]
# total_cost_list_R = [-1 for _ in range(expnum)]
# total_N_list_R = [-1 for _ in range(expnum)]
# act_1_rate_list_R = [-1 for _ in range(expnum)]
     # 
# total_cost_list_R_alllocal = [-1 for _ in range(expnum)]
# total_cost_list_R_allremote = [-1 for _ in range(expnum)]
# total_cost_list_R_random = [-1 for _ in range(expnum)]
# total_cost_list_R_myopic = [-1 for _ in range(expnum)]
     # 
# print "Ready to start..."
# for i in range(expnum):    
    # print "Alive..."
    # R_clt = R_list[i]
    # v_mat, a_mat = MDPOptimization(penalty_input=20.0, R_clt_inp = R_clt,setEtaDirectly=True, eta_inp=0.6)
    # act_1_rate_list_R[i], total_N = OffloadingRate(a_mat,getN=True)
    # total_cost_list_R[i] = ValueAverage(v_mat)
    # total_N_list_R[i] = total_N/(6*4) # Q_max=6, G_max=4
     # 
    # print "   sub-Alive..."
    # v_mat, a_mat = MDPOptimization(penalty_input=20.0, R_clt_inp = R_clt,actionflag_inp='AlwaysLocal',setEtaDirectly=True, eta_inp=0.6)
    # total_cost_list_R_alllocal[i] = ValueAverage(v_mat)
    # print "   sub-Alive..."
    # v_mat, a_mat = MDPOptimization(penalty_input=20.0, R_clt_inp = R_clt,actionflag_inp='AlwaysRemote',setEtaDirectly=True, eta_inp=0.6)
    # total_cost_list_R_allremote[i] = ValueAverage(v_mat)
    # print "   sub-Alive..."
    # v_mat, a_mat = MDPOptimization(penalty_input=20.0, R_clt_inp = R_clt,actionflag_inp='Random',setEtaDirectly=True, eta_inp=0.6)
    # total_cost_list_R_random[i] = ValueAverage(v_mat)    
    # print "   sub-Alive..."
    # v_mat, a_mat = MDPOptimization(penalty_input=20.0, R_clt_inp = R_clt,actionflag_inp='Myopic',setEtaDirectly=True, eta_inp=0.6)
    # total_cost_list_R_myopic[i] = ValueAverage(v_mat) 
# print "R_list=", R_list
# print "total_cost_list_R=", total_cost_list_R
# print "total_cost_list_R_alllocal=", total_cost_list_R_alllocal
# print "total_cost_list_R_allremote=", total_cost_list_R_allremote
# print "total_cost_list_R_random=", total_cost_list_R_random
# print "total_cost_list_R_myopic=", total_cost_list_R_myopic
# print "total_N_list_R=", total_N_list_R
# print "act_1_rate_list_R=", act_1_rate_list_R

# changed, 8 aug 2013 
R_list= [1.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0]
total_cost_list_R= [97.102710913722902, 97.000757997367472, 92.526844832451786, 91.991303997560379, 87.773749591271965, 86.713996030191538, 82.864747724766019, 81.192998081502608]
total_cost_list_R_alllocal= [99.47472146365034, 99.466052765184529, 99.473306924406344, 99.458937186456552, 99.472075544588463, 99.459750157519508, 99.471365647666218, 99.460268645163936]
total_cost_list_R_allremote= [98.956656780850366, 98.93079071686391, 94.092562549176279, 93.915421440485275, 89.839272158084199, 89.273592859273307, 85.716434185937658, 84.450327263022061]
total_cost_list_R_random= [99.293697840594021, 99.857386712153598, 95.454791004170531, 95.985276818485772, 94.782626027995263, 95.724559346225234, 92.208596718524788, 93.55083011375217]
total_cost_list_R_myopic= [101.24157232968093, 101.31003909849483, 96.625141069516616, 96.913679517013165, 92.95492068181558, 93.105113329470882, 89.970154877100256, 89.446184044384708]
total_N_list_R= [2, 2, 3, 3, 4, 4, 5, 5]
act_1_rate_list_R= [0.3333333333333333, 0.3333333333333333, 0.5277777777777778, 0.5277777777777778, 0.625, 0.625, 0.6916666666666667, 0.6916666666666667]

figa = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(R_list,act_1_rate_list_R,color='red',marker='o')
xlabel('Cloudlet coverage radius')
ylabel('Rate of offloading decisions')
subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
# xlim([4,36])
# ylim([0.35,0.80])
   
figb = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(R_list,total_N_list_R,color='red',marker='o')
xlabel('Cloudlet coverage radius')
ylabel('Maxmum number of cloudlets')
subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
# xlim([4,36])
#ylim([1,8])
   
figc = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(R_list,total_cost_list_R,color='red',marker='o')
plot(R_list,total_cost_list_R_alllocal,color='black',linestyle='--',marker='x')
plot(R_list,total_cost_list_R_allremote,color='blue',linestyle='--',marker='x')
plot(R_list,total_cost_list_R_random,color='green',linestyle='--',marker='x')
plot(R_list,total_cost_list_R_myopic,color='cyan',linestyle='--',marker='x')
xlabel('Cloudlet coverage radius')
ylabel('User\'s avg. cost')
subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
# xlim([4,36])
#ylim([30,90])
   
show()
print "TERMINATED."
