def FA(s):
#if the length is less than 3 then it can't be accepted, Therefore end the process.
    if len(s)<3:
        return "Rejected"
#first three characters are fixed. Therefore checking them using index
    if s[0]=='1':
        if s[1]=='0':
            if s[2]=='1':
                # After index 2 only "1" can appear. Therefore break the process if any other character is detected
                for i in range(3,len(s)):
                    if s[i]!='1':
                        return "Refected"
                return "Accepted"
            return "Rejected"
        return "Rejected"
    return "Rejected"
inputs=['1','10101','101','10111','01010',""]
for i in inputs:
    print(FA(i))