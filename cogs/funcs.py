from cogs.poems import poemslistissa, poemslistbasho, poemslistbuson # pylint: disable=E0401

#DATABASE FUNCTIONS

#SETUP FUNCTIONS

#SEARCH COMMANDS FUNCTIONS

def haiku(author, poemnum):
    if author == 1:
        poemdraft = poemslistissa[poemnum]
        poemdraft1 = poemdraft.split("\\n")
        poem = f'{poemdraft1[0]} \n {poemdraft1[1]} \n {poemdraft1[2]}"'
        return poem
    elif author == 2:
        poemdraft = poemslistbasho[poemnum]
        poemdraft1 = poemdraft.split("\\n")
        poem = f'{poemdraft1[0]} \n {poemdraft1[1]} \n {poemdraft1[2]}"'
        return poem
    elif author == 3:
        poemdraft = poemslistbuson[poemnum]
        poemdraft1 = poemdraft.split("\\n")
        poem = f'{poemdraft1[0]} \n {poemdraft1[1]} \n {poemdraft1[2]}"'
        return poem

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