
class setting(object):
    def __init__(self):
        # 白名单列表
        self.whiteList = {"douban.com","image.so.com","baidu.com"}

    # 设置白名单 能爬为True, 不能爬为False
    def WhiteList(self,url):
        for w in self.whiteList:
            # print(w)
            # 如果待爬取的url在白名单下返回True，否则返回False;
            if w in url:
                return True
        return False

class test(object):
    def fun(self):
        return "test fun"

if __name__ == "__main__":
    setting = setting()
    url = 'http://baidu.com/'
    b = setting.WhiteList(url)
    print(b)