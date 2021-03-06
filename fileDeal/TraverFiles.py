import os
import time

'''
功能描述：遍历目录处理子文件
参数描述： 1 rootDir 目标文件的根目录
'''

class TraversalFun():
    # 1 初始化
    def __init__(self, rootDir):
        self.rootDir = rootDir

    # 2 遍历目录文件
    def TraversalDir(self):
        TraversalFun.AllFiles(self, self.rootDir)

    # 3 递归遍历所有文件，并提供具体文件操作功能
    def AllFiles(self, rootDir):
        # 返回指定目录包含的文件或文件夹的名字的列表
        for lists in os.listdir(rootDir):
            # 待处理文件夹名字集合
            path = os.path.join(rootDir, lists)
            # 核心算法，对文件具体操作
            if os.path.isfile(path):
                print(os.path.abspath(path))
            # 递归遍历文件目录
            elif os.path.isdir(path):
                TraversalFun.AllFiles(self, path)


if __name__ == '__main__':
    time_start = time.time()

    # 根目录文件路径
    rootDir = r"../dataDeal/wordtotxt"
    tra = TraversalFun(rootDir)
    tra.TraversalDir()

    time_end = time.time()
    print('totally cost', time_end-time_start, 's')
