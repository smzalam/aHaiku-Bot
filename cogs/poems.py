import requests

# --------------------    HAIKUDB ----------------------------------
urlissa = "https://haiku-json-db.herokuapp.com/issa"
responseissa = requests.request("GET", urlissa)
rstrippedissa = responseissa.text.split('",')
poemslistissa = rstrippedissa[2:]

urlbasho = "https://haiku-json-db.herokuapp.com/basho"
responsebasho = requests.request("GET", urlbasho)
rstrippedbasho = responsebasho.text.split('",')
poemslistbasho = rstrippedbasho[2:]

urlbuson = "https://haiku-json-db.herokuapp.com/buson"
responsebuson = requests.request("GET", urlbuson)
rstrippedbuson = responsebuson.text.split('",')
poemslistbuson = rstrippedbuson[2:]


# --------------------    POETRYDB ----------------------------------
headers = {
    'x-rapidapi-key': "948df7f86cmshc48caac45c16ba3p125b6cjsnfb525f1303f3",
    'x-rapidapi-host': "thundercomb-poetry-db-v1.p.rapidapi.com"
}

urlauthors =  "https://thundercomb-poetry-db-v1.p.rapidapi.com/author"
urltitles =  "https://thundercomb-poetry-db-v1.p.rapidapi.com/title"
urllinecounts =  "https://thundercomb-poetry-db-v1.p.rapidapi.com/linecount/14"

responseauthors = requests.request("GET", urlauthors, headers=headers)
authors1 = responseauthors.text.split('",')
authors = authors1[2:]

responsetitles = requests.request("GET", urltitles, headers=headers)
titles1 = responsetitles.text.split('",')
titles = titles1[2:]

responselcounts = requests.request("GET", urllinecounts, headers=headers)
lcounts1 = responselcounts.text.split('",')
lcounts = lcounts1[2:]
