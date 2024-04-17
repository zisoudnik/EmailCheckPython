email=input("Give me your email adress")


def checkemail(email):
    flag=0
    flag2=0
    flag3=0
    flag4=0
    thesipapaki=0
    thesitelia=0


    mikos=len(email)
    for i in range (0,len(email)):
        if email[i]=="@":
             flag=1
             thesipapaki=i
    for i in range (0,mikos):
        if email[i] ==".":
             flag2=1
             thesitelia=i
    if thesipapaki < thesitelia +1:
        flag3=1
    if thesipapaki < thesitelia:
        flag3=1
    if thesipapaki==0:
        flag4=0
    else:
        flag4=1


    if flag==1 and flag2==1 and flag3==1 and flag4==1:
        print("egkuro email")
        return True
    else:
        print("mh egkuro email")
        return False

while checkemail(email) == False:
    email = input ("give me your email adress")
