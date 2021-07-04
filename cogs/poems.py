import requests

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