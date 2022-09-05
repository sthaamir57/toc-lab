import re

a = "We are learning toc and this is toc_lab"

## findall

print(re.findall("toc",a))
# >>> ['toc', 'toc']

print(re.findall("dbms",a))
# >>> []

## sub
print(re.sub("toc", "dsa", a))
# >>> We are learning dsa and this is dsa_lab

print(re.sub("\s", "-", a))
# >>> We-are-learning-toc-and-this-is-toc_lab

## split
print(re.split("\s", a))                
# >>> ['We', 'are', 'learning', 'toc', 'and', 'this', 'is', 'toc_lab']

print(re.split("and", a))               
# >>> ['We are learning toc ', ' this is toc_lab']

## search
print(re.search("toc_lab", a))          
# >>> <re.Match object; span=(32, 39), match='toc_lab'>

print(re.search("os_lab", a))           
# >>> None

## email validation
pattern = "^([a-z 0-9]{1,12})+[@]+([a-z]{1,8})+[.]+(com|net|org)$"

def isValid(pattern, email):
    x = re.search(pattern, email)
    if(x):
        print("Valid email")
    else:
        print("Invalid email")

isValid(pattern, "asmt@gmail.com")      
# >>> Valid email

isValid(pattern, "abc123@email.met")    
# >>> Invalid email