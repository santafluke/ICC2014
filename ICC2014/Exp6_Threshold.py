'''
Created on Aug 6, 2013

@author: yzhang28
'''

from Headers import *

def ShowActionMatrix(mat,G=-1):
        if -1==G: #default
            for i_g,dim1 in enumerate(mat):
                if i_g!=0:
                    print 'State G=', i_g
                for i_q,dim2 in enumerate(dim1):
                    for i_n,elem in enumerate(dim2):
                        if i_g!=0 and i_q!=0:
                            print elem,
                    print
                if i_g!=0:
                    print
            print
        else:
            # Print the threshold graph for given phase G
            print 'G =', G
            print 'Q in lines, N in rows:'
            for i_q,dim2 in enumerate(mat[G]):
                for i_n,elem in enumerate(dim2):
                    print elem,
                print

# v_mat, a_mat = MDPOptimization(Q_max_inp=7, R_clt_inp=25, penalty_input=35.0, setEtaDirectly=True, eta_inp=0.4)
# ShowActionMatrix(a_mat)

# A
# Q=1+6, R=25, pen=35, eta=0.4
#  G=3
# 0 0 0 0 1 1 1
# 0 0 0 1 1 1 1
# 0 0 0 1 1 1 1
# 0 0 0 1 1 1 1
# 0 0 0 1 1 1 1
# 0 0 0 1 1 1 1
# 

# B
# Q=1+6, R=25, pen=65, eta=0.7
# State G= 4
# 
# 0 0 0 0 1 1 1
# 0 1 1 1 1 1 1
# 0 1 1 1 1 1 1
# 0 1 1 1 1 1 1
# 0 1 1 1 1 1 1
# 0 1 1 1 1 1 1

A = [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1],
     [0, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]]

B = [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 1, 1]]

figa, axa = plt.subplots(figsize=(4.5,3.5))
xminorLocator = FixedLocator([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
yminorLocator = FixedLocator([1.5,2.5,3.5,4.5,5.5])
axa.xaxis.set_minor_locator(xminorLocator)  
axa.yaxis.set_minor_locator(yminorLocator)
axa.set_xlabel(r"Cloudlet #")
axa.set_ylabel("Queue length")
ylim([5.5,0.5])
grid(True,which='minor', color='gray',linestyle='--',linewidth=0.5)
# grid(True,which='major', color='black')
axa.imshow(A, cmap=cm.gist_yarg, interpolation='nearest')

figb, axb = plt.subplots(figsize=(4.5,3.5))
xminorLocator = FixedLocator([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5])
yminorLocator = FixedLocator([1.5,2.5,3.5,4.5,5.5])
axb.xaxis.set_minor_locator(xminorLocator)  
axb.yaxis.set_minor_locator(yminorLocator)
axb.set_xlabel(r"Cloudlet #")
axb.set_ylabel("Queue length")
ylim([5.5,0.5])
grid(True,which='minor', color='gray',linestyle='--',linewidth=0.5)
# grid(True,which='major', color='black')
axb.imshow(B, cmap=cm.gist_yarg, interpolation='nearest')

show()