alphabets = ["0", "1"]
states = ["S0", "S1", "S2"]
start_state = "S0"
final_state = ["S2"]
transition = {
    ("S0", "0") : "S1",
    ("S0", "1") : "S0",
    ("S1", "0") : "S2",
    ("S1", "1") : "S0",
    ("S2", "0") : "S2",
    ("S2", "1") : "S2",
}

def FA(str):

    #SET START STATE
    curr_state = start_state

    #ACCETPED OR REJECTED
    for s in str:
        curr_state = transition[(curr_state, s)]
        if(curr_state == None):
            return "REJECTED"
            break
    
    if(curr_state in final_state):
        return "ACCEPTED"
    else:
        return "REJECTED"

inputs=['110101', '1001', '10101', '1010100', '1', '00', '0', '01']
for i in inputs:
    print(i + "\t=\t" +FA(i))