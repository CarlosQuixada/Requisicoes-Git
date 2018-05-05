import requests
import json
'''def link_prox_commit(header):
        for link in header:
            info = link.split(";")
            next = info[1].replace("rel", "").replace("=", "").replace('"', "").replace(" ", "")
            link_prox = info[0].replace("<", "").replace(">", "").replace(" ", "")

            if next == 'next':
                return link_prox

        return ''
'''
#hearders = {'Content-Type': 'application/vnd.github.v3+json',}
resp = requests.get('https://api.github.com/repos/npi-ufc-qxd/contest/commits',auth=('CarlosQuixada', 'C@rlos95'))
print(resp.text)
commits = resp.json()
urls = []
for commit in commits:
    author_commit = commit['author']
    url_author = author_commit['url']
    #print(author_commit)
    print(url_author)
    if url_author not in urls:
        urls.append(url_author)

print(urls)


















'''header = resp.headers
prox_commit=link_prox_commit(header['Link'].split(","))
print(prox_commit)
#dados = json.loads(str(resp.text['commit']))
print(resp.json())
#for commit in dados:
#    print(str(commit).split(','))

from comandos.requisicoes import Requisicoes
import requests
import json
token ='250deea8eefcdc749be5be834d358c6bf2d227e1'
#token =''
#requisicoes = Requisicoes()
#headers = {'Accept': 'application/vnd.github.hellcat-preview+json'}
#resp = requests.get('https://api.github.com/repos/npi-ufc-qxd/contest/collaborators', auth=('CarlosQuixada', 'C@rlos95'))
#resp = requests.get('https://api.github.com/authorizations', auth=('CarlosQuixada', 'C@rlos95'))
#pulls = requisicoes.get_pulls('octocat','Hello-World')

#resp = requests.get('https://api.github.com/authorizations',auth=('CarlosQuixada', 'C@rlos95'))
headers = { 'Content-Type' : 'application/json',
            'Authorization':'token '+token}

#resp = requests.get('https://api.github.com/authorizations/36932275',auth=('CarlosQuixada', 'C@rlos95'))
#resp = requests.get('https://api.github.com/repos/npi-ufc-qxd/contest/collaborators',headers=headers)
#resp = requests.get('https://api.github.com/repos/npi-ufc-qxd/contest/commits/18f856d13e9b4db2e8efae623a245c7020fe8a00')
resp = requests.get('https://api.github.com/search/users?q=Jacques Nier+in:jacquesnier@hotmail.com')
print(resp.text)

#print(len(pulls))'''