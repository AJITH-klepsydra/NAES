import base64

def enum(a):
    b=[None]*len(a)
    for i in range(0,len(a)):
        if(a[i]=='a'):
            b[i]=1
            continue
        if(a[i]=='b'):
            b[i]=2
            continue
        if(a[i]=='c'):
            b[i]=3
            continue
        if(a[i]=='d'):
            b[i]=4
            continue
        if(a[i]=='e'):
            b[i]=5
            continue
        if(a[i]=='f'):
            b[i]=6
            continue
        if(a[i]=='g'):
            b[i]=7
            continue
        if(a[i]=='h'):
            b[i]=8
            continue
        if(a[i]=='i'):
            b[i]=9
            continue
        if(a[i]=='j'):
            b[i]=10
            continue
        if(a[i]=='k'):
            b[i]=11
            continue
        if(a[i]=='l'):
            b[i]=12
            continue
        if(a[i]=='m'):
            b[i]=13
            continue
        if(a[i]=='n'):
            b[i]=14
            continue
        if(a[i]=='o'):
            b[i]=15
            continue
        if(a[i]=='p'):
            b[i]=16
            continue
        if(a[i]=='q'):
            b[i]=17
            continue
        if(a[i]=='r'):
            b[i]=18
            continue
        if(a[i]=='s'):
            b[i]=19
            continue
        if(a[i]=='t'):
            b[i]=20
            continue
        if(a[i]=='u'):
            b[i]=21
            continue
        if(a[i]=='v'):
            b[i]=22
            continue
        if(a[i]=='w'):
            b[i]=23
            continue
        if(a[i]=='x'):
            b[i]=24
            continue
        if(a[i]=='y'):
            b[i]=25
            continue
        if(a[i]=='z'):
            b[i]=26
            continue
    return b


def denum(a):
    b=[None]*len(a)
    for i in range(0,len(a)):
        if(a[i]==1):
            b[i]='a'
            continue
        if(a[i]==2):
            b[i]='b'
            continue
        if(a[i]==3):
            b[i]='c'
            continue
        if(a[i]==4):
            b[i]='d'
            continue
        if(a[i]==5):
            b[i]='e'
            continue
        if(a[i]==6):
            b[i]='f'
            continue
        if(a[i]==7):
            b[i]='g'
            continue
        if(a[i]==8):
            b[i]='h'
            continue
        if(a[i]==9):
            b[i]='i'
            continue
        if(a[i]==10):
            b[i]='j'
            continue
        if(a[i]==11):
            b[i]='k'
            continue
        if(a[i]==12):
            b[i]='l'
            continue
        if(a[i]==13):
            b[i]='m'
            continue
        if(a[i]==14):
            b[i]='n'
            continue
        if(a[i]==15):
            b[i]='o'
            continue
        if(a[i]==16):
            b[i]='p'
            continue
        if(a[i]==17):
            b[i]='q'
            continue
        if(a[i]==18):
            b[i]='r'
            continue
        if(a[i]==19):
            b[i]='s'
            continue
        if(a[i]==20):
            b[i]='t'
            continue
        if(a[i]==21):
            b[i]='u'
            continue
        if(a[i]==22):
            b[i]='v'
            continue
        if(a[i]==23):
            b[i]='w'
            continue
        if(a[i]==24):
            b[i]='x'
            continue
        if(a[i]==25):
            b[i]='y'
            continue
        if(a[i]==26):
            b[i]='z'
            continue
    return b

def fact(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact











def encryption():
    msg=input("enter the message to be encrypted:\t")
    en_msg=enum(msg)
    rem_list=[None]*len(en_msg)
    qt_list=[None]*len(en_msg)
    tc_list=[None]*len(en_msg)

    for i in range(0,len(en_msg)):
        tc_list[i]=int(en_msg[i])*fact(i+3)
        rem_list[i]=int(int(tc_list[i])%sec_key)
        qt_list[i]=int(int(tc_list[i])/sec_key)

    for i in range(0,len(qt_list)):
        qt_list[i]=str(qt_list[i])+'$'

    encr_msg=denum(rem_list)
    encr_msg="".join(encr_msg)
    qt_list ="".join(qt_list)
    encr_msg=encr_msg+ '+' + qt_list
    print(encr_msg)
    return encr_msg

def decryption():
    encr_msg=input("Enter the message to be decrypted:\t")
    lim=encr_msg.find('+')
    msg=[None]*int((len(encr_msg)))
    qt_list=[None]*int((len(encr_msg)))
    qt_list_n=[None]*lim
    for i in range(0,lim):
        msg[i]=encr_msg[i]
    for i in range(lim+1,len(encr_msg)):
             qt_list[i]=encr_msg[i]
    qt_list_n[1:lim+1]=qt_list[lim:len(encr_msg)]
    dec_msg=[None]*lim
    for i in range(0,lim):
        dec_msg[i]= enum(msg[i])
    for i in range(1,lim+1):
                    tc=int(qt_list_n[i+1])*sec_key+int(str(dec_msg[i-1])[1:-1])
                    a=(int(tc/fact(i+2)))
                    if(a==1):
                         c='a'
                    if(a==2):
                         c='b'
                    if(a==3):
                        c='c'

                    if(a==4):
                        c='d'

                    if(a==5):
                        c='e'

                    if(a==6):
                        c='f'

                    if(a==7):
                        c='g'

                    if(a==8):
                        c='h'

                    if(a==9):
                        c='i'

                    if(a==10):
                        c='j'

                    if(a==11):
                        c='k'

                    if(a==12):
                        c='l'

                    if(a==13):
                        c='m'

                    if(a==14):
                        c='n'

                    if(a==15):
                        c='o'

                    if(a==16):
                        c='p'

                    if(a==17):
                        c='q'

                    if(a==18):
                        c='r'

                    if(a==19):
                        c='s'

                    if(a==20):
                        c='t'

                    if(a==21):
                        c='u'

                    if(a==22):
                        c='v'

                    if(a==23):
                        c='w'

                    if(a==24):
                        c='x'

                    if(a==25):
                        c='y'

                    if(a==26):
                        c='z'
                    print(c)







print("\t::welcome to ANES::\t                                         -prof and klep")
print("Options: ")
print("1. Encryption \n2. Decryption")
choice=int(input(":"))
sec_key=int(input("\n3.Security key: "))



if(choice==1):
    encryption()
elif(choice==2):
        decryption()




