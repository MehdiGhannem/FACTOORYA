import numpy as np
import scipy.fftpack
from scipy.fftpack import fft
import math
import cmath
import mysql.connector
cnx = mysql.connector.connect(host='localhost',
                            database='odhreb_bel_chwaya',
                            user='root',
                            port='3307',
                            password='Dorra@123')
cur = cnx.cursor()
query = ("SELECT * FROM test1")
cur.execute(query)
M=[]
N=0
for (elt) in cur:
    N+=1
    L=[elt[1],elt[2],elt[3]]
    M.append(L)
maxU=0
maxI=0
t1=M[0][2]
t2=t1
x=0
chngmt1U=0
chngmt2U=0
chngmt1I=0
chngmt2I=0
if chngmt2U+chngmt1U < 3 :
    if M[0][0]<= M[1][0]:
        chngmt1U+=1
        maxU=1
        t1=M[1][2]
        for i in range (2,N):
            if M[i-1][0] <= M[i][0] :
                maxU=i
                t1=M[i][2]
            if M[i-1][0] > M[i][0]:
                chngmt2U=2
                break


    if M[0][0] > M[1][0]:
        chngmt2U+=1
        for i in range(2,N):
            if M[i-1][0] > M[i][0]:
                if chngmt2U+chngmt1U == 2 :
                    chngmt2U+=1
                    break
            if M[i-1][0] <= M[i][0]:
                chngmt1U=1
                if M[i][0]>= M[maxU][0]:
                    maxU=i
                    t1=M[maxU][2]
if chngmt2I+chngmt1I < 3 :
    if M[0][1]<= M[1][1]:
        chngmt1I+=1
        maxI=1
        t2=M[1][2]
        for i in range (2,N):
            if M[i-1][1] <= M[i][1] :
                maxI=i
                t2=M[i][2]
            if M[i-1][1] > M[i][1]:
                chngmt2I=2
                break

    if M[0][1] > M[1][1]:
        chngmt2I+=1
        for i in range(2,N):
            if M[i-1][1] > M[i][1]:
                if chngmt2I+chngmt1I == 2 :
                    chngmt2I+=1
                    break
            if M[i-1][1] <= M[i][1]:
                chngmt1I=1
                if M[i][1]>= M[maxI][1]:
                    maxI=i
                    t2=M[maxI][2]
phi=(t1-t2)*360*50
print(N)
#print(t1)
#print(t2)
#print(M[maxU][0])
#print(M[maxI][1])
cosphi=math.cos(phi/180*math.pi)
print(math.cos(phi/180*math.pi))
W=[]
for i in range (0,N):
    W.append(M[i][0])
AFT=fft(W)
FT=np.abs(fft(W))
print(AFT[66])
print(FT[66])
def thd(abs_data):
    sq_sum=0.0
    for r in range( len(abs_data)):
       sq_sum = sq_sum + (abs_data[r])**2

    sq_harmonics = sq_sum -(max(abs_data))**2.0
    thd = 100*((sq_harmonics**0.5) /(sq_sum**0.5))
    #thd = 100 * ((sq_harmonics ** 0.5) / (max(abs_data)** 0.5))

    return thd
print(thd(W))

