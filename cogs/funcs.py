import random
from urllib import response

import requests

from cogs.poems import poemslistbasho  # pylint: disable=E0401
from cogs.poems import authors, lcounts, poemslistbuson, poemslistissa, titles # pylint: disable=E0401

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
        'x-rapidapi-key': "e897edce51msh5e6201e36f8b427p144d41jsnea04e68ce1a5",
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

def db_clean(response):
    result = []
    for row in response.scalars():
        row_dict = row.__dict__
        result.append(row_dict.pop('_sa_instance_state', None).dict)
    return result