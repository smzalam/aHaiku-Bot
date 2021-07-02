#DATABSE FUNCTIONS

#SEARCH COMMANDS FUNCTIONS


#HAIKU COMMANDS FUNCTIONS

def getting_pos(db_rules):
    pos = []

    for i in db_rules:
        pos.append(i[0])

    return pos

def getting_rules(db_rules):
    rule = []

    for i in db_rules:
        rule.append(i[1])

    return rule

def writing_rules(pos, rules):
    val = ''
    for i in range(len(rules)):
        val += "`" + str(pos[i]) + '. ' + str(rules[i]) + "`" + '\n'

    return val