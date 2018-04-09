# -*- codind: utf-8 -*-

#动态加载模块
#如果加载模块出错，编译器报ImportError错误


#使用try来捕获异常
try:
    import json
except ImportError:
    import simplejson as json
print json.dumps({'python':2.7})
