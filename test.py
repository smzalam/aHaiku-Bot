import discord
from discord.ext import commands
import requests
from cogs.funcs import haiku

# author = "shakespeare"
# title = "title"
# linecount = "linecount"
# title="summer"

# url = "https://haiku-json-db.herokuapp.com/issa"
# print(url)
# link1 = url.format(author)

# headers = {
#     'x-rapidapi-key': "948df7f86cmshc48caac45c16ba3p125b6cjsnfb525f1303f3",
#     'x-rapidapi-host': "thundercomb-poetry-db-v1.p.r1apidapi.com"
#     }

# response = requests.request("GET", url)

# #print(response.text)

# for i in range(len(response.text)):
#     if response.text[i:i+6] == "haikus":
#         print(response.text[i:i+6])
#         print(i)

# rstripped = response.text.split('",')
# print(rstripped[2])
# poemslist = rstripped[2:]
# print(poemslist[0])

hi = haiku(3, 8)
print(hi)