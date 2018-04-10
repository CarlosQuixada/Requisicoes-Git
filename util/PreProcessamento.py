from googletrans import Translator


class PreProcesso(object):

    def __init__(self):
        self.translator = Translator()

    def link_prox_pulls(self, header):
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
