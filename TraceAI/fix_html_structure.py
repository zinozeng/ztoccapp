#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 删除孤立的注释
old_str = '    </div>\n    \n    <!-- 异常运单详情弹窗 -->\n    <!-- 上报拦截件弹窗 -->'
new_str = '    </div>\n    \n    <!-- 上报拦截件弹窗 -->'

content = content.replace(old_str, new_str)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('已修复 HTML 结构')
