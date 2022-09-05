rules_input = ['E -> E + T', 'E -> T', 'T -> T * F', 'T -> F', 'F -> (E)', 'F -> a', 'F -> b']
expression_data = 'a + a * b' # Accepted
# expression_data = 'c + a * b' # Rejected

#Expression is saved to exp in reverse order, removing whitespace.
i = 0
exp = []
chars = expression_data.split(" ")
for char in chars[::-1]:
    i = i + 1
    exp.append(char)

import copy

class Rule:
    def __init__(self , variable , productions):
        self.variable   = variable
        self.productions = [productions]

def divide_rules():  # split productions into the rules class by variable
    results = []
    for rule in rules_input:
        found = False
        var = rule.split(" -> ")
        for result in results:
            if result.variable == var[0]:
                result.productions.append(var[1])
                found = True
        if not found:
            results.append(Rule(var[0] , var[1]))
    return results

def print_reject():  #Prints Reject and exits program.
    print("\n\n")
    print("************************************")
    print("*             REJECT               *")
    print("************************************")
    exit()

def get_rule(symbol):
    global rules
    for rule in rules:
        if rule.variable == symbol:
            return rule
    return False

def operation(stack, exp):  #Performs the operations of a PDA.  Recursive.
    if len(stack) > len(exp) or (len(stack) == 0 and len(exp) > 0):
        return
    current_symbol = stack.pop()
    if current_symbol == exp[-1]:
        exp.pop()
        test(stack , exp)
        operation(copy.deepcopy(stack) , copy.deepcopy(exp))
    rule = get_rule(current_symbol)
    if rule == False:
        return
    for production in rule.productions:
        new_stack = copy.deepcopy(stack)
        for s in production.split(" ")[::-1]:
            new_stack.append(s)
        operation(new_stack, copy.deepcopy(exp))

def test(stack, exp):
    if len(stack) == 0 and len(exp) == 0:
        print("\n\n")
        print("************************************")
        print("*             ACCEPT               *")
        print("************************************")
        exit()
    else:
        return False

def main():
    global length, rules, var_test
    print("Rules:")
    print(rules_input)
    print("Expression:")
    print(expression_data)
    rules = divide_rules()
    for rule in rules:
        var_test.append(rule.variable)
    print("variables =", var_test)
    stack = []
    stack.append(rules[0].variable)
    operation(stack, exp)
    print_reject()

var_test = []
stack = []
var = []
final= []
main()
