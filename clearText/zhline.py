from zhtools.langconv import *

# 转换繁体到简体
str1 = '琴棋書畫'
line1 = Converter('zh-hans').convert(str1)
print('繁体->简体:\n',line1)


# 转换简体到繁体
str2 =r'琴棋书画'
line2 = Converter('zh-hant').convert(str2)
print('简体->繁体:\n',line2)
