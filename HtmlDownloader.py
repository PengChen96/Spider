
import urllib.request

class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            print("HtmlDownloader url is None")
            return None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
        }
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        if response.getcode() != 200:
            print("HtmlDownloader download error："+response.getcode())
            return None
        data = response.read()
        # data = data.decode("utf-8")
        return data