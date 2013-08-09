'''
Created on Aug 5, 2013

@author: yzhang28
'''
from Headers import *

def WriteMat(mat,num):
        f = open('e:\\bbbb.txt', 'a')
        f.write('Case:%d'%num)
        for i_g,dim1 in enumerate(mat):
            if i_g!=0:
                f.write('State G=%d\n'%(i_g))
            for i_q,dim2 in enumerate(dim1):
                for i_n,elem in enumerate(dim2):
                    if i_g!=0 and i_q!=0:
                        f.write('Q=%d,N=%d, A=%d   ' %(i_q,i_n,elem))
                f.write('\n')
            if i_g!=0:
                f.write('\n')
        f.write('\n')
        f.close()
        
################################################################################
#                             THE 4th EXP - "EXTRA"
#                            Different lambda of Queue
#                                    Just TRY
################################################################################
lam_q = [0.5, 0.6]
act_1_rate_list = [-1 for _ in range(len(lam_q))]
total_cost_list = [-1 for _ in range(len(lam_q))]
total_cost_list_alllocal = [-1 for _ in range(len(lam_q))]
total_cost_list_allremote = [-1 for _ in range(len(lam_q))]

for i in range(len(lam_q)):
    print "Alive~"
    lam = lam_q[i]
    v_mat, a_mat = MDPOptimization(lam_q_inp=lam,penalty_input=50.0,gamm_inp=1.0)
    total_cost_list[i] = ValueAverage(v_mat)
    act_1_rate_list[i] = OffloadingRate(a_mat)
    # v_mat, a_mat = MDPOptimization(lam_q_inp=lam,penalty_input=50.0,actionflag_inp='AlwaysLocal')
    # total_cost_list_alllocal[i] = ValueAverage(v_mat)
    # v_mat, a_mat = MDPOptimization(lam_q_inp=lam,penalty_input=50.0,actionflag_inp='AlwaysRemote')
    # total_cost_list_allremote[i] = ValueAverage(v_mat)
    ShowActionMatrix(a_mat)
 
print "lam_q=", lam_q
print "act_1_rate_list=", act_1_rate_list
print "total_cost_list=", total_cost_list
 
figa = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(lam_q,act_1_rate_list,color='red',marker='o')
xlabel('lam q')
ylabel('Offloading rate')
subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
 
 
figb = plt.figure(figsize=(4.5,4.5))
grid(True, which="both")
plot(lam_q,total_cost_list,color='red',marker='o')
# plot(lam_q,total_cost_list_alllocal,color='black',marker='^')
# plot(lam_q,total_cost_list_allremote,color='blue',marker='^')
xlabel('Lam q')
ylabel('User\'s avg. cost')
subplots_adjust(top=0.93,bottom=0.16,left=0.15, right=0.95)
 
show()
