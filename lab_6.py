# input_cfg = '''S ::= xAc
# A ::= yBb
# B ::= za'''
# input_string = 'xyzabc$'

input_cfg ='''S ::= A|$
A ::= abB|abc
B ::= $|d'''
input_string = 'ab$'

# -------------------------------------------------------------------------------------
#
#   Class storing parse tree nodes.
#   It keeps symbol value - terminal or non-terminal and children.
#   In case the symbol is terminal - children array must be empty.
#   It is due to the fact that a terminal symbol does not have any production rules so it can be only a leaf.
#
# -------------------------------------------------------------------------------------

class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []

    def add_children(self, node):
        self.children.append(node)

    def remove_children(self):
        self.children = []

    def print_node(self):
        print("symbol: ", self.symbol)
        print("children: ", self.children)


def parser(CFG, input):
    print("\nProvided contex-free grammar:")
    print(CFG)
    print("\nProvided input string:", input)
    rules = CFG['S']

    if CFG != {}:
        out, parse_tree, match, input_iter = rec_parse(
            CFG, "S", input, 0, "", Node("S"), [], 0)
        print("\n\nEnd of input parsing")
        if match == True and (out == input or out == input[:-1]) and parse_tree != []:
            print("Input string accepted by the CFG\n")
            print_parse_tree(parse_tree)
        else:
            print("Input string not accepted by the CFG.\n")


def rec_parse(CFG, nonterminal, input, input_iter, out, node, parse_tree, matched):
    rules = CFG[nonterminal]
    match = False

    print("-----------------------------------")
    print("CFG: " + nonterminal)

    parse_tree.append(node)

    for rule in rules:
        match = False
        matched = 0
        for i in range(len(rule)):
            node.add_children(rule[i])
            print_parse_tree(parse_tree)

            print("Current production rule {} : {}".format(nonterminal, rule))
            print("Current input character " + input[input_iter])
            if rule[i].isupper() == True:
                out, parse_tree, match, input_iter = rec_parse(
                    CFG, rule[i], input, input_iter, out, Node(rule[i]), parse_tree, matched)
                if out == input[:-1] and match == True:
                    match = True
                    return out, parse_tree, match, input_iter
            else:
                if rule[i] == input[input_iter]:
                    out = out + rule[i]
                    input_iter += 1
                    matched += 1
                    match = True
                elif rule[i] == '$':
                    match = True
                    continue
                else:
                    print("\t\tBacktracking...")
                    for el in range(matched):
                        out = out.replace(out[el], "")
                        input_iter = input_iter - 1

                    node.remove_children()
                    match = False
                    matched = 0
                    break

        if (out == input[:-1] or out == input or input == '$') and match == True:
            match = True
            return out, parse_tree, match, input_iter

        if (out == input[:-1] or out == input or input == '$') and match == True:
            return out, parse_tree, match, input_iter

    return out, parse_tree, match, input_iter


def print_parse_tree(parse_tree):
    for el in parse_tree:
        if el.children == []:
            parse_tree.remove(el)

    if len(parse_tree) == 0:
        return

    print("\n-------------------------    PARSE TREE      -------------------------")
    for el in parse_tree:
        el.print_node()
    print("----------------------------------------------------------------------\n")




CFG_NON_TERMINAL_SEPARATOR = "::="
CFG_PRODUCTION_RULES_SEPARATOR = "|"
INPUT_STRING_END_SYMBOL = "$"

def parse_cfg(input_cfg):
    lines = input_cfg.split('\n')
    CFG = {}
    for line in lines:
        line = line.strip()
        line = line.split(CFG_NON_TERMINAL_SEPARATOR)

        non_terminal = line[0].strip()
        validate_non_terminal(non_terminal, CFG)
        line.pop(0)

        production_rules = []
        for el in line:
            if non_terminal in el:
                raise SyntaxError(
                    "Error in non-terminal symbol {}. Left recursion is not supported!".format(non_terminal))

            if '|' in el:
                el = el.split(CFG_PRODUCTION_RULES_SEPARATOR)
                el = (x.strip() for x in el)
                validate_production_rule(el, non_terminal)
                production_rules += el
            else:
                el = el.strip()
                validate_production_rule(el, non_terminal)
                production_rules.append(el)

        CFG[non_terminal] = production_rules

    validate_CFG(CFG)
    return CFG


def validate_production_rule(rule, non_terminal):
    if rule == "":
        raise SyntaxError(
            "Error in non-terminal symbol {}. Production rule can not be empty!".format(non_terminal))

# -------------------------------------------------------------------------------------
#
#   Method responsible for validating non-terminal symbol.
#   It raises error if:
#       * non-terminal is not upper case letter.
#       * such non-terminal already exists in the CFG.
#
# -------------------------------------------------------------------------------------


def validate_non_terminal(non_terminal, CFG):
    if not non_terminal.isupper():
        raise SyntaxError(
            "Error in non-terminal symbol {}. Production rules must start with non-terminal symbols.".format(non_terminal))

    if non_terminal in CFG:
        raise SyntaxError(
            "Non-terminal symbol {} already exists in CFG!".format(non_terminal))


# -------------------------------------------------------------------------------------
#
#   Method responsible for validating CFG.
#   It raises error if:
#       * any production rule uses non-terminal symbol which is not declared.
#
# -------------------------------------------------------------------------------------
def validate_CFG(CFG):
    for key in CFG:
        production_rules = CFG[key]
        for production in production_rules:
            for el in production:
                if el.isupper() and not (el in CFG):
                    raise SyntaxError("Error in {}. Invalid CFG".format(el))


# -------------------------------------------------------------------------------------
#
#   Method asks user for input string.
#
# -------------------------------------------------------------------------------------
def get_input_string():
    input_string = input("Enter input string: ")
    validate_input_string(input_string)
    return input_string


# -------------------------------------------------------------------------------------
#
#   Method responsible for validating input string.
#   It raises error if:
#       * input is an empty string.
#       * last element of input string is not equal to INPUT_STRING_END_SYMBOL
#
# -------------------------------------------------------------------------------------
def validate_input_string(input_string):
    if input_string == "" or input_string[-1] != INPUT_STRING_END_SYMBOL:
        raise SyntaxError("Invalid input string")
def main():
    CFG = parse_cfg(input_cfg)
    parser(CFG, input_string)


main()