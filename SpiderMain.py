
import UrlManager,HtmlDownloader,HtmlParser,FileOutputer

class SpiderMain(object):
    def __init__(self):
        self.urlManager = UrlManager.UrlManager()
        self.htmlDownloader = HtmlDownloader.HtmlDownloader()
        self.htmlParser = HtmlParser.HtmlParser()
        self.fileOutputer = FileOutputer.FileOutputer()
    def carry(self,root_url):
        count = 1
        # 添加爬取网页的根url
        self.urlManager.add_new_url(root_url)

        while self.urlManager.has_new_urls():
            try:
                url = self.urlManager.get_new_url()
                print("SpiderMain正在准备爬取："+url)
                # 获取网页数据html
                html_data = self.htmlDownloader.download(url)
                # print(str(html_data))
                new_urls = self.htmlParser.parser(html_data)        # set()
                self.urlManager.add_new_urls(new_urls)
                filecount = self.fileOutputer.file_output(html_data)
                print(url+"中爬取了"+str(filecount)+"张图片")
                if count ==1000:
                    break
                count +=1
            except Exception as error:
                print("SpiderMain Exception error:",error)
        print("爬虫爬取URL数:"+str(count))

if __name__ == "__main__":
    # http://www.bilibili.com/
    # https://www.douban.com/
    # http: //image.so.com /
    root_url = 'https://www.douban.com/'
    spider = SpiderMain()
    spider.carry(root_url)
    print("爬虫入口URL为:"+root_url)
else:
    print("正在执行其他模块")