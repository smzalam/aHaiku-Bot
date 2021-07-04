from site import execusercustomize

from cogs.poems import (poemslistbasho,  # pylint: disable=E0401
                        poemslistbuson, poemslistissa)

#DATABASE FUNCTIONS

#SETUP FUNCTIONS
def setupdb(cursor, conn):

    cursor.execute("""CREATE TABLE rules (
        position integer,
        rule text
    )""")

    cursor.execute("""CREATE TABLE gamechannel (
        serverid integer,
        channelid integer,
        channelname text
    )""")

    cursor.execute("""CREATE TABLE syllablecount (
        lineone integer,
        linetwo integer,
        linethree integer
    )""")

    cursor.execute("INSERT INTO rules(position, rule) VALUES (?, ?)", (1, "The same person can't go twice in a row."))
    cursor.execute("INSERT INTO rules(position, rule) VALUES (?, ?)", (2, "The haiku verses should be written on new lines. Check an example to see the format of writing a haiku."))
    cursor.execute("INSERT INTO syllablecount(lineone, linetwo, linethree) VALUES (?, ?, ?)", (5, 7, 5))

    conn.commit()
    conn.close()
    
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
