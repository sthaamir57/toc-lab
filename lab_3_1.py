def FA(s):
    size=0
    
    for i in s:
        if i=='1' or i=='0':
            size+=1
        else:
            return "Rejected"

    if s[len(s)-1]=='1':
        return "Rejected"
    else:
        return "Accepted"

inputs=['110', '1110', '111','1100', '0011','00110aa']
for i in inputs:
    print(i + "\t=\t" +FA(i))