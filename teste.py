from comandos.requisicoes import Requisicoes

requisicoes = Requisicoes()

pulls = requisicoes.get_pulls('octocat','Hello-World')

print(len(pulls))