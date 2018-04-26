from comandos.requisicoes import Requisicoes
import pandas as pd
requisicoes = Requisicoes()

#pulls = requisicoes.get_pulls('octocat','Hello-World')
commits = requisicoes.get_commits('npi-ufc-qxd','contest')

list_commits = pd.DataFrame({
    "frase": commits,
})

list_commits.to_csv('commits.csv',index=False)