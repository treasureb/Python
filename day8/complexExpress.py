# -*- coding: utf-8 -*-

#复杂表达式

d = {'Adam':95,'Lisa':85,'Bart':59}

#将其变成一个HTML表格
#字符串可以通过%进行格式化，用指定的参数替代%s
#字符串的join()方法可以把一个list拼接成一个字符串
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name,score) for name,socre in d.iteritems()]

print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
