from comandos.requisicoes import Requisicoes
import pandas as pd
requisicoes = Requisicoes()

#pulls = requisicoes.get_pulls('octocat','Hello-World')
urls = requisicoes.get_urls_author('npi-ufc-qxd','contest')


print(urls)
'''list_commits = pd.DataFrame({
    "frase": commits,
})'''

#list_commits.to_csv('commits.csv',index=False)