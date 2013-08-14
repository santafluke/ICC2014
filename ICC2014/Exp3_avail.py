'''
Created on Aug 5, 2013

@author: yzhang28
'''

from Headers import *

################################################################################
#                                THE 3rd EXP
#                          Different ETA and penalty
################################################################################
eta_list = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
penalty_list =[0.0, 15.0, 25.0]
eta_list.reverse()
act_1_rate_list = [[-1 for _ in range(len(eta_list))] for _ in range(len(penalty_list))]
total_cost_list = [[-1 for _ in range(len(eta_list))] for _ in range(len(penalty_list))]
total_cost_list_alllocal_nopen = [-1 for _ in range(len(eta_list))]
total_cost_list_allremote_nopen = [-1 for _ in range(len(eta_list))]
total_cost_list_random_nopen = [-1 for _ in range(len(eta_list))]
total_cost_list_myopic_nopen = [-1 for _ in range(len(eta_list))]
total_cost_list_alllocal_highpen = [-1 for _ in range(len(eta_list))]
total_cost_list_allremote_highpen = [-1 for _ in range(len(eta_list))]
total_cost_list_random_highpen = [-1 for _ in range(len(eta_list))]
total_cost_list_myopic_highpen = [-1 for _ in range(len(eta_list))]
# # 
# for p in range(len(penalty_list)):
#     for i in range(len(eta_list)):    
#         print "(",p,i,")s","alive!"
#         eta = eta_list[i]
#         penalty = penalty_list[p]
#         v_mat, a_mat = MDPOptimization(penalty_input=penalty, setEtaDirectly = True, eta_inp = eta)
#         total_cost_list[p][i] = ValueAverage(v_mat)
#         act_1_rate_list[p][i] = OffloadingRate(a_mat)
# # THE FOLLOWING IS ONLY FOR THE COMPARISON PART
# # Firstly, no penalty case
# for i in range(len(eta_list)):
#     print 'ALIVE!'
#     eta = eta_list[i]
#     v_mat, a_mat = MDPOptimization(penalty_input=penalty_list[0], setEtaDirectly = True,eta_inp = eta, actionflag_inp='AlwaysLocal')
#     total_cost_list_alllocal_nopen[i] = ValueAverage(v_mat)
#     print 'sub-ALIVE!'
#     if i==0:
#         total_cost_list_allremote_nopen[i] = total_cost_list_alllocal_nopen[i]
#     else:
#         v_mat, a_mat = MDPOptimization(penalty_input=penalty_list[0], setEtaDirectly = True,eta_inp = eta, actionflag_inp='AlwaysRemote')
#         total_cost_list_allremote_nopen[i] = ValueAverage(v_mat)
#     print 'sub-ALIVE!'
#     if i==0:
#         total_cost_list_random_nopen[i] = total_cost_list_alllocal_nopen[i]
#     else:
#         v_mat, a_mat = MDPOptimization(penalty_input=penalty_list[0], setEtaDirectly = True,eta_inp = eta, actionflag_inp='Random')
#         total_cost_list_random_nopen[i] = ValueAverage(v_mat)
#     v_mat, a_mat = MDPOptimization(penalty_input=penalty_list[0], setEtaDirectly = True,eta_inp = eta, actionflag_inp='Myopic')
#     total_cost_list_myopic_nopen[i] = ValueAverage(v_mat)
# # Then, high penalty case
# for i in range(len(eta_list)):
#     print 'ALIVE!'
#     eta = eta_list[i]
#     v_mat, a_mat = MDPOptimization(penalty_input=penalty_list[2], setEtaDirectly = True,eta_inp = eta, actionflag_inp='AlwaysLocal')
#     total_cost_list_alllocal_highpen[i] = ValueAverage(v_mat)
#     print 'sub-ALIVE!'
#     if i==0:
#         total_cost_list_allremote_highpen[i] = total_cost_list_alllocal_highpen[i]
#     else:
#         v_mat, a_mat = MDPOptimization(penalty_input=penalty_list[2], setEtaDirectly = True,eta_inp = eta, actionflag_inp='AlwaysRemote')
#         total_cost_list_allremote_highpen[i] = ValueAverage(v_mat)
#     print 'sub-ALIVE!'
#     if i==0:
#         total_cost_list_random_highpen[i] = total_cost_list_alllocal_highpen[i]
#     else:
#         v_mat, a_mat = MDPOptimization(penalty_input=penalty_list[2], setEtaDirectly = True,eta_inp = eta, actionflag_inp='Random')
#         total_cost_list_random_highpen[i] = ValueAverage(v_mat)
#     v_mat, a_mat = MDPOptimization(penalty_input=penalty_list[2], setEtaDirectly = True,eta_inp = eta, actionflag_inp='Myopic')
#     total_cost_list_myopic_highpen[i] = ValueAverage(v_mat)
#    
# print "eta_list=", eta_list
# print "act_1_rate_list[0]=", act_1_rate_list[0] #No penalty, action rate
# print "act_1_rate_list[1]=", act_1_rate_list[1] #Mid penalty, action rate
# print "act_1_rate_list[2]=", act_1_rate_list[2] #High penalty, action rate
# print "total_cost_list[0]=", total_cost_list[0] #No penalty, total cost
# print "total_cost_list[1]=", total_cost_list[1] #Mid penalty, total cost
# print "total_cost_list[2]=", total_cost_list[2] #High penalty, total cost
# print "total_cost_list_alllocal_nopen=", total_cost_list_alllocal_nopen #COMPARE, All LOCAL total cost
# print "total_cost_list_allremote_nopen=", total_cost_list_allremote_nopen #COMPARE, All REMOTE total cost
# print "total_cost_list_random_nopen=", total_cost_list_random_nopen #COMPARE, RANDOM total cost
# print "total_cost_list_myopic_nopen=", total_cost_list_myopic_nopen #COMPARE, MYOPIC total cost
# print "total_cost_list_alllocal_highpen=", total_cost_list_alllocal_highpen #COMPARE, All LOCAL total cost
# print "total_cost_list_allremote_highpen=", total_cost_list_allremote_highpen #COMPARE, All REMOTE total cost
# print "total_cost_list_random_highpen=", total_cost_list_random_highpen #COMPARE, RANDOM total cost
# print "total_cost_list_myopic_highpen=", total_cost_list_myopic_highpen #COMPARE, MYOPIC total cost  


eta_list= [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
act_1_rate_list[0]= [0.6388888888888888, 0.6388888888888888, 0.6388888888888888, 0.6388888888888888, 0.6388888888888888, 0.6388888888888888, 0.6388888888888888, 0.6388888888888888, 0.6388888888888888, 0.6666666666666666]
act_1_rate_list[1]= [0.4722222222222222, 0.4722222222222222, 0.4722222222222222, 0.5555555555555556, 0.5555555555555556, 0.625, 0.6388888888888888, 0.6388888888888888, 0.6388888888888888, 0.6666666666666666]
act_1_rate_list[2]= [0.4722222222222222, 0.4722222222222222, 0.4722222222222222, 0.4722222222222222, 0.5555555555555556, 0.5555555555555556, 0.5972222222222222, 0.6388888888888888, 0.6388888888888888, 0.6666666666666666]
total_cost_list[0]= [100.38220109999523, 99.857350398502263, 99.367435800408998, 98.912494659725041, 98.492563400672609, 98.107681759706068, 97.757886021843277, 97.443213736101882, 97.163701312850861, 96.91934108412535]
total_cost_list[1]= [107.03157852956643, 108.30403716209271, 109.48901570608633, 109.33704983994181, 108.27807438877045, 106.7616921240035, 103.92255864627963, 101.29384096383116, 98.95959400213539, 96.91934108412535]
total_cost_list[2]= [107.39062027805772, 108.60885151706485, 109.74320580732321, 110.79403307692374, 110.53470009524017, 108.97253624433297, 107.74222266849782, 103.8609257823171, 100.15685504920452, 96.91934108412535]
total_cost_list_alllocal_nopen= [115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932]
total_cost_list_allremote_nopen= [100.62655567759458, 100.06297630761426, 99.537271457767275, 99.049458948028629, 98.599555772856405, 98.18758235160729, 97.813555759911736, 97.477494454213527, 97.179415870103085, 96.91934108412535]
total_cost_list_random_nopen= [109.61768286145798, 106.85492055802938, 106.03977991471801, 109.05981115741305, 109.44153555851183, 104.60724893199296, 103.21338929988266, 103.50749487184481, 107.68766055954956, 108.67759300278522]
total_cost_list_myopic_nopen= [100.62655567759458, 100.06297630761426, 99.537271457767275, 99.049458948028629, 98.599555772856405, 98.18758235160729, 97.813555759911736, 97.477494454213527, 97.179415870103085, 96.91934108412535]
total_cost_list_alllocal_highpen= [115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932, 115.42788762929932]
total_cost_list_allremote_highpen= [143.18483392526051, 136.14953444939366, 129.58988110503668, 123.50502117625307, 117.89410650455082, 112.75629261295593, 108.09074224949627, 103.89661972688506, 100.17309488140523, 96.91934108412535]
total_cost_list_random_highpen= [119.69236794124419, 129.65637573770493, 125.2989527492841, 117.94577925744021, 116.78419469820246, 114.07131252702818, 112.58946656196957, 109.17924972297959, 106.86344592989046, 105.78650135050555]
total_cost_list_myopic_highpen= [115.42788762929932, 115.42788762929932, 115.42788762929932, 117.1891405867284, 114.19884520938783, 111.75240278279176, 110.01050482221505, 104.951418381422, 100.6995924145365, 96.91934108412535]


figa = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(eta_list,act_1_rate_list[0],color='black',marker='o',label="$c_{pen}$=0")
plot(eta_list,act_1_rate_list[1],color='blue',marker='s', label="$c_{pen}$=15")
plot(eta_list,act_1_rate_list[2],color='red',marker='^', label="$c_{pen}$=25")
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
xlabel('Cloudlet availability $\\eta_a$', fontsize=16)
ylabel('Offloading rate', fontsize=16)
legend(loc='lower right')
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)
# xlim([-0.01,1.01])
ylim([0.46,0.70])
 
figb = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(eta_list,total_cost_list[0],color='black',marker='o', label="$c_{pen}$=0")
plot(eta_list,total_cost_list[1],color='blue',marker='s', label="$c_{pen}$=15")
plot(eta_list,total_cost_list[2],color='red',marker='^', label="$c_{pen}$=25")
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
legend(loc='best')
xlabel('Cloudlet availability $\\eta_a$', fontsize=16)
ylabel('User\'s avg. cost', fontsize=16)
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)
ylim([97, 112])

figbextra = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
p1,= plot(eta_list,total_cost_list[0],color='black',marker='o', label="MDP, $c_{pen}$=0")
p2,= plot(eta_list,total_cost_list[1],color='blue',marker='s', label="MDP, $c_{pen}$=15")
p3,= plot(eta_list,total_cost_list[2],color='red',marker='^', label="MDP, $c_{pen}$=25")
p4,= plot(eta_list,total_cost_list_alllocal_highpen,color='black',marker='s', fillstyle='none',linestyle='--',label="LOC,$c_{pen}$=25")
p5,= plot(eta_list,total_cost_list_allremote_highpen,color='blue',marker='x', fillstyle='none',linestyle='--',label="OFF,$c_{pen}$=25")
#p6,= plot(eta_list,total_cost_list_random_highpen,color='cyan',marker='v', fillstyle='none',linestyle='--',label="RND,$c_{pen}$=25")
p7,= plot(eta_list,total_cost_list_myopic_highpen,color='green',marker='^', fillstyle='none',linestyle='--',label="MYO,$c_{pen}$=25")
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
legend(loc='best',prop={'size':11})
# l1 = legend([p1,p2,p3],["MDP, $c_{pen}$=0","MDP, $c_{pen}$=15","MDP, $c_{pen}$=25"],loc='upper right',prop={'size':11})
# l2 = legend([p4,p5,p7],["LOC, $c_{pen}$=25","OFF, $c_{pen}$=25","MYO, $c_{pen}$=25"],loc='center right',prop={'size':11})
# gca().add_artist(l1)
xlabel('Cloudlet availability $\\eta_a$', fontsize=16)
ylabel('User\'s avg. cost', fontsize=16)
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)
ylim([95, 145])
 
figc = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(eta_list,total_cost_list[0],color='black',marker='o', fillstyle='none',label="MDP")
plot(eta_list,total_cost_list_alllocal_nopen,color='black',marker='s', fillstyle='none',linestyle='--',label="LOC")
plot(eta_list,total_cost_list_allremote_nopen,color='blue',marker='x', fillstyle='none',linestyle='--',label="OFF")
# plot(eta_list,total_cost_list_random_nopen,color='cyan',marker='v', fillstyle='none',linestyle='--',label="RND")
plot(eta_list,total_cost_list_myopic_nopen,color='green',marker='^', fillstyle='none',linestyle='--',label="MYO")
# xlim([-0.01,1.01])
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
legend(loc='best')
xlabel('Cloudlet availability $\\eta_a$', fontsize=16)
ylabel('User\'s avg. cost', fontsize=16)
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)

figd = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(eta_list,total_cost_list[2],color='red',marker='^', fillstyle='none',label="MDP")
plot(eta_list,total_cost_list_alllocal_highpen,color='black',marker='s', fillstyle='none',linestyle='--',label="LOC")
plot(eta_list,total_cost_list_allremote_highpen,color='blue',marker='x', fillstyle='none',linestyle='--',label="OFF")
# plot(eta_list,total_cost_list_random_highpen,color='cyan',marker='v', fillstyle='none',linestyle='--',label="RND")
plot(eta_list,total_cost_list_myopic_highpen,color='green',marker='^', fillstyle='none',linestyle='--',label="MYO")
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
legend(loc='best')
xlabel('Cloudlet availability $\\eta_a$', fontsize=16)
ylabel('User\'s avg. cost', fontsize=16)
ylim([95,145])
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)

show()
print "TERMINATED."