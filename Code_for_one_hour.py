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
FacPui=[]
P=[]
for (elt) in cur:
    N+=1
    L=[elt[1],elt[2],elt[3]]
    M.append(L)
for d in range(0,180000) # nombre de periode pendant une heure
    maxU=d*67
    maxI=d*67
    t1 = M[d*67][2]
    t2 = t1
    chngmt1U = 0
    chngmt2U = 0
    chngmt1I = 0
    chngmt2I = 0
    if chngmt2U + chngmt1U < 3:
        if M[d*67][0] <= M[(d*67)+1][0]:
            chngmt1U += 1
            maxU = (d*67)+1
            t1 = M[(d*67)+1][2]
            for i in range(2, 67):
                if M[(d*67)+i-1][0] <= M[(d*67)+i][0]:
                    maxU = d*67+i
                    t1 = M[d*67+i][2]
                if M[(d*67)+i-1][0] > M[(d*67)+i][0]:
                    chngmt2U = 2
                    break
        if M[d*67][0] > M[(d*67)+1][0]:
            chngmt2U += 1
            for i in range(2, 67):
                if M[(d*67)+i - 1][0] > M[(d*67)+i][0]:
                    if chngmt2U + chngmt1U == 2:
                        chngmt2U += 1
                        break
                if M[(d*67)+i - 1][0] <= M[(d*67)+i][0]:
                    chngmt1U = 1
                    if M[(d*67)+i][0] >= M[maxU][0]:
                        maxU = (d*67)+i
                        t1 = M[maxU][2]
        if chngmt2I + chngmt1I < 3:
            if M[d*67][1] <= M[(d*67)+1][1]:
                chngmt1I += 1
                maxI = (d*67)+1
                t2 = M[(d*67)+1][2]
                for i in range(2, 67):
                    if M[(d*67)+i - 1][1] <= M[(d*67)+i][1]:
                        maxI = (d*67)+i
                        t2 = M[(d*67)+i][2]
                    if M[(d*67)+i - 1][1] > M[(d*67)+i][1]:
                        chngmt2I = 2
                        break
        if M[(d*67)][1] > M[(d*67)+1][1]:
            chngmt2I += 1
            for i in range(2, 67):
                if M[(d*67)+i - 1][1] > M[(d*67)+i][1]:
                    if chngmt2I + chngmt1I == 2:
                        chngmt2I += 1
                        break
                if M[(d*67)+i - 1][1] <= M[(d*67)+i][1]:
                    chngmt1I = 1
                    if M[(d*67)+i][1] >= M[maxI][1]:
                        maxI = (d*67)+i
                        t2 = M[maxI][2]
    phi = (t1 - t2) * 360 * 50
    cosphi = math.cos(phi / 180 * math.pi)
    FacPui.append(cosphi)
    Puissance = (1 / 2) * (M[maxU][0] * M[maxI][1] * cosphi)
    P.append(Puissance)