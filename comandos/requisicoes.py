import requests
from util.PreProcessamento import PreProcesso


class Requisicoes(object):
    def __init__(self):
        self.url_base = 'https://api.github.com'
        self.processamento = PreProcesso()

    def get_pulls(self, usuario, projeto):
        pulls = []
        prox = True

        path = '/repos/' + usuario + '/' + projeto + '/pulls?state=all'
        response = requests.get(self.url_base + path)
        pulls.append(self.processamento.get_list_pulls(response))

        while prox:
            link_prox = self.processamento.link_prox_pulls(response.headers['Link'].split(","))

            if link_prox != '':
                response = requests.get(link_prox)
                pulls.extend(self.processamento.get_list_pulls(response))
            else:
                prox = False

        return pulls
