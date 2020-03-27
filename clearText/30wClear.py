import os,re,time
from REdealText import textParse

class loadFolders(object):   # 迭代器
    def __init__(self, par_path):
        self.par_path = par_path
    def __iter__(self):
        for file in os.listdir(self.par_path):
            file_abspath = os.path.join(self.par_path, file)
            if os.path.isdir(file_abspath): # if file is a folder
                yield file_abspath

class loadFiles(object):
    def __init__(self, par_path):
        self.par_path = par_path
    def __iter__(self):
        folders = loadFolders(self.par_path)
        for folder in folders:              # level directory
            catg = folder.split(os.sep)[-1]
            for file in os.listdir(folder):     # secondary directory
                file_path = os.path.join(folder, file)
                if os.path.isfile(file_path):
                    this_file = open(file_path, 'rb') #rb读取方式更快
                    content = this_file.read().decode('utf8',"ignore")
                    yield catg, content
                    this_file.close()



if __name__=='__main__':
    start = time.time()

    filepath = os.path.abspath(r'./clearText/EnPapers')
    files = loadFiles(filepath)
    n = 5  # n 表示抽样率， n抽1
    for i, msg in enumerate(files):
        if i % n == 0:
            # catg = msg[0]    # 文章类别
            # content = msg[1] # 文章内容
            # content = textParse(content) # 正则清洗
            if int(i/n) % 1000 == 0:
                print('{t} *** {i} \t docs has been dealed'.format(i=i, t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))

    end = time.time()
    print('total spent times:%.2f' % (end-start)+ ' s')
