# FA that does not contain 2 consecutive 0.

def FA(s):
    size = len(s)
    pos=0
    k=0

#check if only one aplhabet
    if size == 1:
        return "ACCEPTED"

    for i in s:
        if i=='1' or i=='0':
            pos+=1
        else:
            return "ACCEPTED"

    while k < size-1:
        if s[k]=='0' and s[k+1]=='0':
            return "REJECTED"
        else:
            k+=1
    return "ACCEPTED"

inputs=['11010', '1001', '10101', '1010100', '1', '00', '0', '01']
for i in inputs:
    print(i + "\t=\t" +FA(i))