

def getInput():
    x = str(input())
    y=""
    for index, char in enumerate(x):
        if char=="!":
            y+="3"
        elif char=="@":
            y+="v"
        elif char=="&":
            y+="·"
        elif char=="=":
            y+="≡"
        elif char==">":
            y+=">"
        else:
            y+=char
    return y


def ad_n(arr,a):
    b=""
    if a[0]=="~":
        b=a[1:]
    else:
        b="~"+a
    check=False
    for prem in arr:
        if prem[0]!="[":
            if strip(prem)==b:
                check=True
                break
    if check==False:
        arr.append(b)

def ad_s(arr,b):
    check=False
    for prem in arr:
        if prem[0]!="[":
            if strip(prem)==b:
                check=True
                break
    if check==False:
        arr.append(b)
        return True
    return False

def ad(arr,b):
    check=False
    for prem in arr:
        if prem[0]!="[":
            if strip(prem)==b:
                check=True
                break
    if check==False:
        arr.append(b)

def negate(a):
    if a[0]=="~":
        return a[1:]
    else:
        return "~"+a

def refute(a,arr):
    if a=="invalid":
        for i,prem in enumerate(arr):
            print (str(i+1)+". "+prem)
        print("refute")
    else:
        #print(premises)
        b=""
        for i,prem in enumerate(arr):
            if "conc:" in prem:
                b=prem[1:]
                print(str(i+1)+". "+prem)
            else:
                print(str(i+1)+". "+prem)
        print(b)


def strip(a):
    b=a
    if a[:3]=="***":
        b=a[3:]
    elif a[:2]=="**":
        b=a[2:]
    elif a[0]=="*":
        b=a[1:]
    if b[:5]=="asm: ":
        b= b[5:]
    
    return b

def checkContradiction(arr):
    o_count=0
    while o_count<len(arr):
        i_count=o_count+1
        while i_count<len(arr):
            elem1=arr[o_count]
            elem2=arr[i_count]
            if elem1[0]!="[" and elem2[0]!="[":
                if strip(elem1)==negate(strip(elem2)):
                    return True
            i_count+=1
        o_count+=1
    return False

def propositional(arr):
    global asmcount
    global blockoff
    while True:
        SIcheck=0
        candidates=[]
        for i,prem in enumerate(premises):
            b=False
            if prem[0]!="[" and prem[0]!="*" and prem[:2]!="**" and prem[:3]!="***" and prem[0]!="%":
                a=0
                if prem[:5]=="asm: ":
                    a=5
                if prem[a+0]=="~" and prem[a+1]=="(":
                    obraccount=1
                    cbraccount=0
                    prev="("
                    for index, char in enumerate(prem[a+2:]):
                        if char=="(":
                            obraccount+=1
                        if char!="(":
                            prev=0
                        if char==")":
                            cbraccount+=1
                        if char=="v" and cbraccount+1==obraccount:
                            p1=prem[a+2:a+index+2]
                            p2=prem[a+index+3:len(prem)-1]
                            ad_n(premises,p1)
                            if checkContradiction(premises)==True:
                                b=True
                                break
                            ad_n(premises,p2)
                            premises[i]=("*"*asmcount)+prem #
                            SIcheck=1
                            b=True
                            break
                        elif char==">" and cbraccount+1==obraccount:
                            p1=prem[a+2:a+index+2]
                            p2=prem[a+index+3:len(prem)-1]
                            ad(premises,p1)
                            if checkContradiction(premises)==True:
                                b=True
                                break
                            ad_n(premises,p2)
                            premises[i]=("*"*asmcount)+prem #
                            SIcheck=1
                            b=True
                            break
                        elif char=="≡" and cbraccount+1==obraccount:
                            p1=prem[a+2:a+index+2]
                            p2=prem[a+index+3:len(prem)-1]
                            ad(premises,"("+p1+"V"+p2+")")
                            if checkContradiction(premises)==True:
                                b=True
                                break
                            ad(premises,"~("+p1+"·"+p2+")")
                            premises[i]=("*"*asmcount)+prem #
                            SIcheck=1
                            b=True
                            break
                        elif char=="·" and cbraccount+1==obraccount:
                            p1=prem[a+2:a+index+2]
                            p2=prem[a+index+3:len(prem)-1]
                            candidates.append([p1,p2])
                            c=False
                            for prem1 in premises:
                            
                                if prem1[0]!="[" and prem1[0]!="*" and prem1[:2]!="**" and prem1[:3]!="***":
                                    if prem1[:5]=="asm: ":
                                        prem1=prem1[5:]
                                    if prem1==p1:
                                        ad_n(premises, p2)
                                        premises[i]=("*"*asmcount)+prem #
                                        SIcheck=1
                                        c=True
                                        b=True
                                        break
                                    elif prem1==p2:
                                        ad_n(premises, p1)
                                        premises[i]=("*"*asmcount)+prem #
                                        SIcheck=1
                                        b=True
                                        c=True
                                        break
                            if c==True:
                                break
                if b==True:
                    break



                if prem[a+0]=="(":
                    obraccount=1
                    cbraccount=0
                    prev="("
                    for index, char in enumerate(prem[a+1:]):
                        if char=="(":
                            obraccount+=1
                        if char!="(":
                            prev=0
                        if char==")":
                            cbraccount+=1
                        if char=="·" and cbraccount+1==obraccount:
                            p1=prem[a+1:a+index+1]
                            p2=prem[a+index+2:len(prem)-1]
                            ad(premises,p1)
                            if checkContradiction(premises)==True:
                                b=True
                                break
                            ad(premises,p2)
                            premises[i]=("*"*asmcount)+prem #
                            SIcheck=1
                            b=True
                            break
                        elif char=="≡" and cbraccount+1==obraccount:
                            p1=prem[a+1:a+index+1]
                            p2=prem[a+index+2:len(prem)-1]
                            ad(premises,"("+p1+">"+p2+")")
                            if checkContradiction(premises)==True:
                                b=True
                                break
                            ad(premises,"("+p2+">"+p1+")")
                            premises[i]=("*"*asmcount)+prem #
                            SIcheck=1
                            b=True
                            break
                        elif char=="v" and cbraccount+1==obraccount:
                            p1=prem[a+1:a+index+1]
                            p2=prem[a+index+2:len(prem)-1]
                            candidates.append([p1,p2])
                            c=False
                            for prem1 in premises:
                            
                                if prem1[0]!="[" and prem1[0]!="*" and prem1[:2]!="**" and prem1[:3]!="***":
                                    if prem1[:5]=="asm: ":
                                        prem1=prem1[5:]
                                    if prem1==negate(p1):
                                        ad(premises,p2)
                                        premises[i]=("*"*asmcount)+prem #
                                        SIcheck=1
                                        b=True
                                        c=True
                                        break
                                    elif prem1==negate(p2):
                                        ad(premises,p1)
                                        premises[i]=("*"*asmcount)+prem #
                                        SIcheck=1
                                        b=True
                                        c=True
                                        break
                        elif char==">" and cbraccount+1==obraccount:
                            p1=prem[a+1:a+index+1]
                            p2=prem[a+index+2:len(prem)-1]
                            candidates.append([p1,p2])
                            c=False
                            for prem1 in premises:
                            
                                if prem1[0]!="[" and prem1[0]!="*" and prem1[:2]!="**" and prem1[:3]!="***":
                                    if prem1[:5]=="asm: ":
                                        prem1=prem1[5:]
                                    if prem1==p1:
                                        ad(premises,p2)
                                        premises[i]=("*"*asmcount)+prem #
                                        SIcheck=1
                                        b=True
                                        c=True
                                        break
                                    elif prem1==negate(p2):
                                        ad_n(premises,p1)
                                        premises[i]=("*"*asmcount)+prem #
                                        SIcheck=1
                                        b=True
                                        c=True
                                        break
                            if c==True:
                                break
                if b==True:
                    break

        #print(premises)

        if checkContradiction(premises)==True:
            if asmcount==1:
                #refute("valid",premises)
                return 1
            elif asmcount>1:
                ward=""
                for index,prem in enumerate(premises[::-1]):
                    if "asm: " not in prem:
                        premises[len(premises)-index-1]="["+prem
                    else:
                        ward=strip(prem)
                        premises[len(premises)-index-1]="["+prem
                        break
                for index, prem in enumerate(premises):
                    if prem[:asmcount]=="*"*asmcount:
                        premises[index]=prem[asmcount:]
                asmcount-=1
                premises.append(negate(ward))
                blockoff=1


        elif SIcheck==0:
            end=True
            for cand in candidates:
                possible=True
                for prem in premises:
                    if prem[0]!="[":
                        if strip(prem)==cand[0] or strip(prem)==negate(cand[0]) or strip(prem)==cand[1] or strip(prem)==negate(cand[1]):
                            possible=False
                            break
                if possible==True:
                    premises.append("asm: "+cand[0])
                    asmcount+=1
                    end=False
                    break
            if end==True:
                #refute("invalid",premises)
                return 0


premises=[]
while True:
    print("Enter premise. To end, enter 0.")
    p=getInput()
    if p!="0":
        premises.append(p)
    else:
        break
print("Enter conclusion.")
p=getInput()
premises.append("[conc:"+p)
if p[0]=="~":
    premises.append("asm: "+p[1:])
else:
    premises.append("asm: ~"+p)

if checkContradiction(premises)==True:
    refute("valid",premises)

asmcount=1
blockoff=0

mode=0
print("(P)ropositional or (Q)uantificational?")
mode=getInput()
if mode=="P":
    if propositional(premises)==1:
        refute("valid",premises)
    else:
        refute("invalid",premises)

elif mode=="Q":
    universals=[]
    letters=["a","b","c","d","e"]
    used=[]
    pos=[]
    b=False
    i=0
    while i<len(premises):
        prem=premises[i]
        if prem[0]!="[":
            a=0
            if prem[:5]=="asm: ":
                a=5
            if prem[a:a+4]=="~(x)":
                ad(premises, "(3x)" + negate(prem[a+4:]))
                premises[i]="*"+prem
                if checkContradiction(premises)==True:
                    b=True
                    break
            elif prem[a:a+5]=="~(3x)":
                ad(premises, "(x)" + negate(prem[a+5:]))
                premises[i]="*"+prem
                if checkContradiction(premises)==True:
                    b=True
                    break
            elif prem[a:a+4]=="(3x)":
                ad(premises, prem[a+4:].replace("x",letters[0]))
                used.append(letters[0])
                letters.remove(letters[0])
                premises[i]="*"+prem
                if checkContradiction(premises)==True:
                    b=True
                    break
            elif prem[a:a+3]=="(x)":
                pos.append(i)
        i+=1
    if b==True:
        refute("valid",premises)
    else:   
        for i in pos:
            univ=strip(premises[i])[3:]
            for letter in used:
                universals.append(univ.replace("x",letter))
            premises[i]="%"+premises[i]
        while True:

            if propositional(premises)==1:
                refute("valid",premises)
                break
            else:
                univadcheck=0
                for univ in universals:
                    if ad_s(premises,univ)==True:
                        univadcheck=1
                        break
                if univadcheck==0:
                    refute("invalid",premises)
                    break
     










