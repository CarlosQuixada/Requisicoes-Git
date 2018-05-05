from googletrans import Translator


class PreProcesso(object):

    def __init__(self):
        self.translator = Translator()

    def link_prox_(self, header):
        for link in header:
            info = link.split(";")
            next = info[1].replace("rel", "").replace("=", "").replace('"', "").replace(" ", "")
            link_prox = info[0].replace("<", "").replace(">", "").replace(" ", "")

            if next == 'next':
                return link_prox

        return ''

    def get_list_pulls(self, response_pulls):
        pulls = []

        for pull in response_pulls.json():
            traduzido = self.translator.translate(pull['title'], dest='pt')
            pulls.append(traduzido.text)

        return pulls

    def get_list_commits(self, response_commits,urls):
        for commit in response_commits:
            if commit != None:
                author_commit = commit['author']
                if author_commit != None:
                    url_author = author_commit['url']
                    if url_author != None and url_author not in urls:
                        urls.append(url_author)

        return urls
