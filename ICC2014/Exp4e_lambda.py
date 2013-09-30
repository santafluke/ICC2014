'''
Created on Aug 5, 2013

@author: yzhang28
'''
from Headers import *

# def WriteMat(mat,num):
#         f = open('e:\\bbbb.txt', 'a')
#         f.write('Case:%d'%num)
#         for i_g,dim1 in enumerate(mat):
#             if i_g!=0:
#                 f.write('State G=%d\n'%(i_g))
#             for i_q,dim2 in enumerate(dim1):
#                 for i_n,elem in enumerate(dim2):
#                     if i_g!=0 and i_q!=0:
#                         f.write('Q=%d,N=%d, A=%d   ' %(i_q,i_n,elem))
#                 f.write('\n')
#             if i_g!=0:
#                 f.write('\n')
#         f.write('\n')
#         f.close()
        
################################################################################
#                             THE 4th EXP - "EXTRA"
#                            Different lambda of Queue
#                                    Just TRY
################################################################################
# lam_q = [0.01, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
# act_1_rate_list = [-1 for _ in range(len(lam_q))]
# total_cost_list = [-1 for _ in range(len(lam_q))]
# total_cost_list_alllocal = [-1 for _ in range(len(lam_q))]
# total_cost_list_allremote = [-1 for _ in range(len(lam_q))]
# total_cost_list_random = [-1 for _ in range(len(lam_q))]
# total_cost_list_myopic = [-1 for _ in range(len(lam_q))]
#  
# for i in range(len(lam_q)):
#     print "Alive~"
#     lam = lam_q[i]
#     v_mat, a_mat = MDPOptimization(lam_q_inp=lam,penalty_input=150.0,gamm_inp=0.7)
#     total_cost_list[i] = ValueAverage(v_mat)
#     act_1_rate_list[i] = OffloadingRate(a_mat)
#     v_mat, a_mat = MDPOptimization(lam_q_inp=lam,penalty_input=150.0,actionflag_inp='AlwaysLocal',gamm_inp=0.7)
#     total_cost_list_alllocal[i] = ValueAverage(v_mat)
#     v_mat, a_mat = MDPOptimization(lam_q_inp=lam,penalty_input=150.0,actionflag_inp='AlwaysRemote',gamm_inp=0.7)
#     total_cost_list_allremote[i] = ValueAverage(v_mat)
#     v_mat, a_mat = MDPOptimization(lam_q_inp=lam,penalty_input=150.0,actionflag_inp='Random',gamm_inp=0.7)
#     total_cost_list_random[i] = ValueAverage(v_mat)
#     v_mat, a_mat = MDPOptimization(lam_q_inp=lam,penalty_input=150.0,actionflag_inp='Myopic',gamm_inp=0.7)
#     total_cost_list_myopic[i] = ValueAverage(v_mat)
# #     ShowActionMatrix(a_mat)
#   
# print "lam_q=", lam_q
# print "act_1_rate_list=", act_1_rate_list
# print "total_cost_list=", total_cost_list
# print "total_cost_list_alllocal=", total_cost_list_alllocal
# print "total_cost_list_allremote=", total_cost_list_allremote
# print "total_cost_list_random=", total_cost_list_random
# print "total_cost_list_myopic=", total_cost_list_myopic

# # Aug 10 2013
# lam_q= [0.01, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
# act_1_rate_list= [0.5277777777777778, 0.5277777777777778, 0.5416666666666666, 0.5416666666666666, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556]
# total_cost_list= [75.24214131700451, 77.038412240405435, 78.497170276948665, 79.559903157561436, 80.321598600066409, 80.871532527126845, 81.276870392970224, 81.581473725415876, 81.814577419408863, 81.995877690050776, 82.138895174421904]
# total_cost_list_alllocal= [78.241806773655981, 80.050445452812085, 81.526545166057332, 82.607221915943342, 83.386929879049532, 83.954088864217141, 84.373742670506402, 84.690157655649145, 84.933015494093937, 85.12240376873666, 85.2721616328556]
# total_cost_list_allremote= [97.512138785830899, 99.424049537207821, 100.9716111820876, 102.0956769122562, 102.90153024413878, 103.48492789488611, 103.91510905757883, 104.23863907552887, 104.48647802416082, 104.67945261771492, 104.83185002364445]
# total_cost_list_random= [87.968045208858257, 93.626394417160896, 91.304212186954402, 91.647863952361618, 88.694323392717251, 88.95424850869432, 89.427454680412751, 98.96953389169947, 91.819337734436658, 92.985384376457858, 87.002842120536201]
# total_cost_list_myopic= [75.780535205569151, 77.591241753072197, 79.069440612486858, 80.152069422966235, 80.933543644007855, 81.502274218954241, 81.923314033989385, 82.240946348771786, 82.484871951679921, 82.675197132678008, 82.825778238886045]

# Sep 10 2013
lam_q= [0.01, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
act_1_rate_list= [0.5277777777777778, 0.5277777777777778, 0.5416666666666666, 0.5416666666666666, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556, 0.5555555555555556]
total_cost_list= [75.275795550066491, 77.534298611902599, 79.137756797706814, 80.159769088698567, 80.826420970114896, 81.281285402038449, 81.605363105004031, 81.844303026446823, 82.025417652360076, 82.165819542188117, 82.276690074856717]
total_cost_list_alllocal= [78.276368388569111, 80.561544955318311, 82.189733805200888, 83.230803082420096, 83.914237450583414, 84.383224545016716, 84.718547380897292, 84.966586400299192, 85.155163406067246, 85.301752727490921, 85.417800230547684]
total_cost_list_allremote= [97.547204155303589, 99.937749197578839, 101.62972623697173, 102.70661424492745, 103.41219040635519, 103.89629756516828, 104.24269404923709, 104.49920455475289, 104.69443595604588, 104.84633775240015, 104.96666949223233]
total_cost_list_random= [88.663804919666745, 93.766160298931666, 95.514978343547412, 90.581764995176414, 95.814421385450672, 101.75681816593749, 97.273944705516328, 96.676234307112637, 93.235478440506824, 97.122861237266051, 97.155902075988791]
total_cost_list_myopic= [75.81504461069207, 78.101554560787804, 79.731525545547811, 80.774495284834856, 81.459757037907806, 81.930417092771506, 82.267236376609389, 82.516599325037475, 82.706342095133238, 82.853956538993629, 82.970905941247622]


figa = plt.figure(figsize=(4.5,4.5))
# grid(True, which="both")
plot(lam_q,act_1_rate_list,color='red',marker='o')
xlabel('Queue arrival rate $\\lambda_q$',fontsize=16)
ylabel('Offloading rate',fontsize=16)
subplots_adjust(top=0.93,bottom=0.16,left=0.20, right=0.95)
 
 
figb = plt.figure(figsize=(4.5,4.5))
# grid(True, which="both")
plot(lam_q,total_cost_list,color='red',marker='o',label='MDP')
plot(lam_q,total_cost_list_alllocal,color='black', linestyle='--', fillstyle='none',marker='s',label='LOC')
plot(lam_q,total_cost_list_allremote,color='blue', linestyle='--', fillstyle='none',marker='x',label='OFF')
# plot(lam_q,total_cost_list_random,color='green', linestyle='--', fillstyle='none',marker='^',label='RND')
plot(lam_q,total_cost_list_myopic,color='green', linestyle='--', fillstyle='none',marker='^',label='MYO')
xlabel('Queue arrival rate $\\lambda_q$',fontsize=16)
ylabel('User\'s avg. cost', fontsize=16)
subplots_adjust(top=0.93,bottom=0.16,left=0.12, right=0.95)
legend(loc='best')
locs, labels = plt.yticks()
plt.setp(labels, rotation=90)
ylim([74,106])
show()
