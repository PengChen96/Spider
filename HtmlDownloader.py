
import urllib.request

class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            print("HtmlDownloader url is None")
            return None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            # 'Accept - Encoding': 'gzip, deflate, br',
            # 'Accept - Language':' zh - CN, zh;q = 0.8',
            # 'Connection':'keep-alive',
            # 'Host': 'erebor.douban.com',
            # 'Referer': 'https: // www.douban.com /'
        }
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        print( "状态码："+str(response.getcode()) )
        if response.getcode() != 200:
            print("HtmlDownloader download error："+response.getcode())
            return None
        data = response.read()
        # data = data.decode("utf-8")
        return data