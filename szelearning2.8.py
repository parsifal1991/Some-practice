szo1=input()
szo2=input()
kulonbseg = 0

szo1hossz=len(szo1)
szo2hossz=len(szo2)

if szo1hossz < szo2hossz :
    kulonbseg = szo2hossz-szo1hossz
    print("A ket szo kozul a",szo2,"a hosszabb"",",kulonbseg,"karakterrel.")
if szo2hossz < szo1hossz :
    kulonbseg = szo1hossz-szo2hossz
    print("A ket szo kozul a",szo1,"a hosszabb"",",kulonbseg,"karakterrel.")
if szo1hossz == szo2hossz :
    print("A ket szo egyforma hosszu.")