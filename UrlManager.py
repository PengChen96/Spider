from setting import setting

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    def add_new_urls(self,urls):
        print("UrlManager urls:"+str(urls))
        if urls is None or len(urls)==0:
            print("UrlManager urls is None or len=0")
            return
        # print(type(urls))
        for url in urls:
            self.add_new_url(url)

    def add_new_url(self,url):
        # print("-----"+url)
        if url is None:
            print("UrlManager url is None")
            return
        sett = setting()
        # print(sett.WhiteList(url))
        # if url not in self.new_urls and url not in self.old_urls:
        if sett.WhiteList(url) and url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def has_new_urls(self):
        return len(self.new_urls) != 0
