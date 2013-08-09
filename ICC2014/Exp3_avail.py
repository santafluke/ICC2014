'''
Created on Aug 5, 2013

@author: yzhang28
'''

from Solver.Exps.Headers import *

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
total_cost_list_alllocal_highpen = [-1 for _ in range(len(eta_list))]
total_cost_list_allremote_highpen = [-1 for _ in range(len(eta_list))]
total_cost_list_random_highpen = [-1 for _ in range(len(eta_list))]
# 
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
# print "total_cost_list_alllocal_highpen=", total_cost_list_alllocal_highpen #COMPARE, All LOCAL total cost
# print "total_cost_list_allremote_highpen=", total_cost_list_allremote_highpen #COMPARE, All REMOTE total cost
# print "total_cost_list_random_highpen=", total_cost_list_random_highpen #COMPARE, RANDOM total cost  

# Original data
# eta_list= [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# act_1_rate_list[0]= [0.0, 0.71875, 0.71875, 0.71875, 0.71875, 0.71875, 0.71875, 0.71875, 0.7291666666666666, 0.7395833333333334, 0.75]
# act_1_rate_list[1]= [0.0, 0.53125, 0.53125, 0.59375, 0.65625, 0.65625, 0.7083333333333334, 0.71875, 0.7291666666666666, 0.7291666666666666, 0.75]
# act_1_rate_list[2]= [0.0, 0.53125, 0.53125, 0.53125, 0.59375, 0.65625, 0.65625, 0.6875, 0.7291666666666666, 0.7291666666666666, 0.75]
# total_cost_list[0]= [116.50464823423852, 91.177599143105908, 90.41156415921769, 89.722989127451555, 89.105310134486544, 88.55201039622473, 88.056478374755386, 87.6120850726155, 87.211950000322716, 86.849076502522038, 86.515517220400298]
# total_cost_list[1]= [116.50464823423852, 102.42237339286179, 104.77204147003498, 105.68755868446637, 104.68149144106792, 103.27078046681896, 101.15989286394684, 96.963419093068623, 93.113982767736559, 89.654185587573906, 86.515517220400298]
# total_cost_list[2]= [116.50464823423852, 103.04258431140171, 105.28972921149114, 107.28430986891469, 107.43748601757869, 106.09776418274259, 104.1524608115832, 102.77967520564631, 97.048671272840522, 91.524244474461696, 86.515517220400298]
# total_cost_list_alllocal_nopen= [116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852]
# total_cost_list_allremote_nopen= [116.50464823423852, 91.451200008308277, 90.630324506995748, 89.894721072940911, 89.237020461104649, 88.649925478133511, 88.12606914828929, 87.658092988717854, 87.238617556422341, 86.860237336235073, 86.515517220400298]
# total_cost_list_random_nopen= [116.50464823423852, 103.4020627152662, 102.58529986180103, 100.46977285340738, 100.65116440915136, 104.45428802289807, 104.39673812521114, 98.678833198749956, 102.95013051270126, 98.054655998983506, 110.93197082862609]
# total_cost_list_alllocal_highpen= [116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852]
# total_cost_list_allremote_highpen= [116.50464823423852, 159.77733347268273, 147.46549226361313, 136.46432849735768, 126.65697662507988, 117.92803796447178, 110.16349442359949, 103.25073310086644, 97.078365491579504, 91.536268362595308, 86.515517220400298]
# total_cost_list_random_highpen= [116.50464823423852, 141.01365308606154, 135.87733263505012, 122.00802482711039, 125.13121440569427, 114.8918577389432, 113.22580437159299, 112.7204627485326, 106.20748536103851, 100.68471298160118, 105.12643041266824]
# Original data ends

eta_list= [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
act_1_rate_list[0]= [0.71875, 0.71875, 0.71875, 0.71875, 0.71875, 0.71875, 0.71875, 0.7291666666666666, 0.7395833333333334, 0.75]
act_1_rate_list[1]= [0.53125, 0.53125, 0.59375, 0.65625, 0.65625, 0.7083333333333334, 0.71875, 0.7291666666666666, 0.7291666666666666, 0.75]
act_1_rate_list[2]= [0.53125, 0.53125, 0.53125, 0.59375, 0.65625, 0.65625, 0.6875, 0.7291666666666666, 0.7291666666666666, 0.75]
total_cost_list[0]= [91.177599143105908, 90.41156415921769, 89.722989127451555, 89.105310134486544, 88.55201039622473, 88.056478374755386, 87.6120850726155, 87.211950000322716, 86.849076502522038, 86.515517220400298]
total_cost_list[1]= [102.42237339286179, 104.77204147003498, 105.68755868446637, 104.68149144106792, 103.27078046681896, 101.15989286394684, 96.963419093068623, 93.113982767736559, 89.654185587573906, 86.515517220400298]
total_cost_list[2]= [103.04258431140171, 105.28972921149114, 107.28430986891469, 107.43748601757869, 106.09776418274259, 104.1524608115832, 102.77967520564631, 97.048671272840522, 91.524244474461696, 86.515517220400298]
total_cost_list_alllocal_nopen= [116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852]
total_cost_list_allremote_nopen= [91.451200008308277, 90.630324506995748, 89.894721072940911, 89.237020461104649, 88.649925478133511, 88.12606914828929, 87.658092988717854, 87.238617556422341, 86.860237336235073, 86.515517220400298]
total_cost_list_random_nopen= [103.4020627152662, 102.58529986180103, 100.46977285340738, 100.65116440915136, 104.45428802289807, 104.39673812521114, 98.678833198749956, 102.95013051270126, 98.054655998983506, 110.93197082862609]
total_cost_list_alllocal_highpen= [116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852, 116.50464823423852]
total_cost_list_allremote_highpen= [159.77733347268273, 147.46549226361313, 136.46432849735768, 126.65697662507988, 117.92803796447178, 110.16349442359949, 103.25073310086644, 97.078365491579504, 91.536268362595308, 86.515517220400298]
total_cost_list_random_highpen= [141.01365308606154, 135.87733263505012, 122.00802482711039, 125.13121440569427, 114.8918577389432, 113.22580437159299, 112.7204627485326, 106.20748536103851, 100.68471298160118, 105.12643041266824]


figa = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(eta_list,act_1_rate_list[0],color='black',marker='o', fillstyle='none',label="No penalty")
plot(eta_list,act_1_rate_list[1],color='blue',marker='s', fillstyle='none', label="Mild penalty")
plot(eta_list,act_1_rate_list[2],color='red',marker='^', fillstyle='none', label="High penalty")
subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
xlabel('Cloudlet availability $\\eta_a$')
ylabel('Rate of offloading decisions')
legend(loc='lower right',prop={'size':10})
# xlim([-0.01,1.01])
# ylim([0.0,0.75])
 
figb = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(eta_list,total_cost_list[0],color='black',marker='o', fillstyle='none',label="No penalty")
plot(eta_list,total_cost_list[1],color='blue',marker='s', fillstyle='none', label="Mild penalty")
plot(eta_list,total_cost_list[2],color='red',marker='^', fillstyle='none', label="High penalty")
subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
legend(loc='best',prop={'size':10})
xlabel('Cloudlet availability $\\eta_a$')
ylabel('User\'s avg. cost')
# xlim([-0.01,1.01])
 
figc = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(eta_list,total_cost_list[0],color='black',marker='o', fillstyle='none',label="No penalty")
plot(eta_list,total_cost_list_alllocal_nopen,color='black',marker='v', fillstyle='none',linestyle='--',label="[Compare] LOC")
plot(eta_list,total_cost_list_allremote_nopen,color='blue',marker='v', fillstyle='none',linestyle='--',label="[Compare] OFF")
plot(eta_list,total_cost_list_random_nopen,color='green',marker='v', fillstyle='none',linestyle='--',label="[Compare] RND")
# xlim([-0.01,1.01])
subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
legend(loc='best',prop={'size':10})
xlabel('Cloudlet availability $\\eta_a$')
ylabel('User\'s avg. cost')

figd = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(eta_list,total_cost_list[2],color='red',marker='^', fillstyle='none',label="High penalty")
plot(eta_list,total_cost_list_alllocal_highpen,color='black',marker='v', fillstyle='none',linestyle='--',label="[Compare] LOC")
plot(eta_list,total_cost_list_allremote_highpen,color='blue',marker='v', fillstyle='none',linestyle='--',label="[Compare] OFF")
plot(eta_list,total_cost_list_random_highpen,color='green',marker='v', fillstyle='none',linestyle='--',label="[Compare] RND")
# xlim([-0.01,1.01])
subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
legend(loc='best',prop={'size':10})
xlabel('Cloudlet availability $\\eta_a$')
ylabel('User\'s avg. cost')

show()
print "TERMINATED."