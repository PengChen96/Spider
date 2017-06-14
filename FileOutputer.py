
from bs4 import BeautifulSoup
import urllib.request,os,re

class FileOutputer(object):
    # 下载进度
    def process(self,a, b, c):
        # a: 已经下载的数据块
        # b:数据块的大小
        # c:远程文件的大小
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        print('%.2f%%' % per)

    def savefile(self,path):
        filepath = "C:\\Users\\pc\\Desktop\\spider"
        if not os.path.isdir(filepath):
            os.mkdir(filepath)
        # '/'最后出现的位置
        pos = path.rindex('/')
        t = os.path.join(filepath, path[pos + 1:])
        # print(t)
        return t

    def file_output(self, html_data):
        file_count = 0
        soup = BeautifulSoup(html_data, 'html.parser', from_encoding='utf-8')
        links = soup.find_all('img')
        for link in links:
            try:
                img_src = link['src']
                # print("src:"+str(img_src))
                img_data_origin = link.get('data-origin')
                # img_data_origin是否为None，是：img_url = img_src;
                img_url = (img_src if img_data_origin is None else img_data_origin)
                urllib.request.urlretrieve(img_url, self.savefile(img_url),self.process)  # 下载到本地
                print(str(img_url)+"下载成功\n")
                file_count +=1
            except Exception as error:
                # print(str(link))
                print(str(img_url) + "下载失败",error)
        return file_count

    # def file_output(self,html_data):
    #     file_count = 0
    #     for link, t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(html_data))):
    #         print(str(link) + '---' + str(t))
    #         try:
    #             urllib.request.urlretrieve(link, self.savefile(link),self.process)  # 下载到本地
    #             file_count +=1
    #         except Exception as error:
    #             print(str(link) + "下载失败",error)
    #     return file_count

