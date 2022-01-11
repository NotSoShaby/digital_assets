import wikipedia


class Wiki():

    def __init__(self, search_phrase):
        search_res = wikipedia.search(search_phrase)
        self.obj = wikipedia.page(search_res[0], auto_suggest=False)
