'''
Created on Aug 5, 2013

@author: yzhang28
'''

from Headers import *

################################################################################
#                                THE 5th EXP
#                          Performance comparison
################################################################################
# print 'Alive!'
# v_mat_MDP, a_mat_MDP = MDPOptimization(penalty_input=0.0, setEtaDirectly=True, eta_inp=0.6)
# print 'Alive!'
# v_mat_Local, a_mat_Local = MDPOptimization(penalty_input=0.0, actionflag_inp='AlwaysLocal',setEtaDirectly=True, eta_inp=0.6)
# print 'Alive!'
# v_mat_Remote, a_mat_Local = MDPOptimization(penalty_input=0.0, actionflag_inp='AlwaysRemote',setEtaDirectly=True, eta_inp=0.6)
# print 'Alive!'
# v_mat_Rand, a_mat_Rand = MDPOptimization(penalty_input=0.0, actionflag_inp='Random',setEtaDirectly=True, eta_inp=0.6)
# perf_MDP = ValueAverage(v_mat_MDP)
# perf_Local = ValueAverage(v_mat_Local)
# perf_Remote = ValueAverage(v_mat_Remote)
# perf_Rand = ValueAverage(v_mat_Rand)
#  
# print "MDP:", perf_MDP
# print "Local:", perf_Local
# print "Remote:", perf_Remote
# print "Rand:", perf_Rand
# print 'val=', val
# val = [perf_MDP, perf_Local, perf_Remote, perf_Rand]    # the bar lengths


val= [88.056478374755386, 116.50464823423852, 88.12606914828929, 96.663929804567388]
pos = [0,0.6,1.2,1.8]    # the bar centers on the y axis
 
figure(figsize=(4.5,4.5))
subplots_adjust(top=0.93,bottom=0.12,left=0.12, right=0.95)
colors = ['r','b','b','b']
rects = barh(pos, val, height=0.35, align='center', color=colors)
yticks(pos, ('MDP', 'LOC', 'OFF', 'RND'))
xlabel('Performance')
#title('MDP versus other action schemes')
grid(True,axis='x')
mvalue = max(val)+3
xlim([0.0,mvalue])
ylim([-0.3,2.1])
for i,rect in enumerate(rects):
    width = rect.get_width()
    text(width-25, pos[i]-0.06, '%.2f'%float(val[i]),fontsize=16, color='w')
show()