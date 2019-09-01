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
print(M[maxU][0])
print(M[maxI][1])
cosphi=math.cos(phi/180*math.pi)
FacPui=[]
FacPui.append(cosphi)
print(math.cos(phi/180*math.pi))
Puissance=(1/2)*(M[maxU][0]*M[maxI][1]*cosphi)
P=[]
P.append(Puissance)
print(Puissance)
#for i in range (1,N):
#    if(M[i][0])>(M[maxU][0]):
#        t1=M[i][2]
#        maxU=i
#    if(M[i][1])>(M[maxI][1]):
#        t2=M[i][2]
#        maxI=i
    #cur.execute("alter table test2 add pui float")
    #for i in range(0,N):
    #    puissance= M[i][0]*M[i][1]*cosphi
    #    M[i].append(puissance)
    #    query1=("update test1 set pui=%s where id_mesure=%s")
    #    valeur=(puissance,i+1)
    #    cur.execute(query1,valeur)
    #    cnx.commit()
#c=0
#for k in range (0,N):
#    c+=cmath.exp(1j*(-2*math.pi*k*1/N))
#    print(cmath.exp(1j*(-2*math.pi*k*1/N)))   this was developped to check the sum of exp() :) turn out to be zero !
#    print(c)
#print(cmath.exp(1j*(-2*math.pi*(N-1)*1/N)))
#W=[]
#r=3 #l'ordre+1 de la transformée de fourier pour le calcul de thd
#for k  in range (0,r):
#    x=0
#    for i in range(0,N):
        #o=complex(0,-2*math.pi*k*i/N)
#        x+=(1/N)*(M[i][0])*cmath.exp(1j*(-2*math.pi*k*i/N))
#    W.append(x) # W[k]=x ;
#print(W)
#f=g=0
#for k in range (0,r):
#    if k==0 :
#        f+=W[k]*W[k]
        #print(f)
#    else:
#        #print(W[k]*W[k])
#        f+=W[k]*W[k]
#        g+=W[k]*W[k]
#        #print(f)
        #print(g)
#f=cmath.sqrt(f)
#print(f)
#print(g)
#g=cmath.sqrt(g)
#THD=(g/f)
#print(THD)
#print(THD.real)
#print(THD.imag)
#cur.close()
#cnx.close()
