import random
from urllib import response

import requests

from cogs.poems import poemslistbasho  # pylint: disable=E0401
from cogs.poems import authors, lcounts, poemslistbuson, poemslistissa, titles # pylint: disable=E0401


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

counter = 0
error404 = ['{"status":404,"reason":"Not found"}']

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

# def poems():
    authornum = random.randint(0, len(authors))
    titlenum = random.randint(0, len(titles))
    linecountnum = random.randint(0, len(lcounts))

    author = authors[authornum]
    title = titles[titlenum]
    linecount = lcounts[linecountnum]

    return author, title, linecount

def poemsearch(author, title):
    headers = {
        'x-rapidapi-key': "948df7f86cmshc48caac45c16ba3p125b6cjsnfb525f1303f3",
        'x-rapidapi-host': "thundercomb-poetry-db-v1.p.rapidapi.com"
    }

    url = "https://thundercomb-poetry-db-v1.p.rapidapi.com/"

    if author != "none" and title == "none":
        try:
            url =  "https://thundercomb-poetry-db-v1.p.rapidapi.com/author/" + author
            response = requests.request("GET", url, headers=headers)
            responselst = response.text.split('},')
            if responselst == error404:
                return "Author not found."
            else:
                return responselst[random.randint(0, len(responselst))]
        except:
            return "Author not found."

    elif author == "none" and title != "none":
        try:
            url =  "https://thundercomb-poetry-db-v1.p.rapidapi.com/title/" + title
            response = requests.request("GET", url, headers=headers)
            responselst = response.text.split('},')
            print(responselst)
            if responselst == error404:
                return "Title not found."
            else:
                return responselst[random.randint(0, len(responselst))]
        except:
            return "Title not found."

    elif author == None and title == None:
        return "Error. Wrong parameters."

    elif author != "none" and title != "none":
        try:
            url =  "https://thundercomb-poetry-db-v1.p.rapidapi.com/author,title/" + author + ";" + title
            response = requests.request("GET", url, headers=headers)
            responselst = response.text.split('},')
            print(responselst)
            if responselst == error404:
                return "Author/Title not found."
            else:
                return responselst[random.randint(0, len(responselst))]
        except:
            return "Author/Title not found."

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
