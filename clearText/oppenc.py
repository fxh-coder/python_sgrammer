# t2s - 繁体转简体（Traditional Chinese to Simplified Chinese）
# s2t - 简体转繁体（Simplified Chinese to Traditional Chinese）
# 用法可参考这个网址 https://pypi.org/project/opencc-python-reimplemented/

import opencc


c1 = opencc.OpenCC('t2s')
s1 = c1.convert('眾議長與李克強會談')
print(s1)

c2 = opencc.OpenCC('s2t')
s2 = c2.convert('琴棋书画')
print(s2)

c3 = opencc.OpenCC('s2hk')
s3 = c3.convert('琴棋书画')
print(s3)