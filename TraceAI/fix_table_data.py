#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取文件
with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换处理状态的值：pending -> 待处理，processing/completed -> 已处理
# 协商派送 - 发布网点 - 待处理
content = content.replace(
    'data-status="intercept-negotiate" data-process-status="pending" data-intercept-status="intercepted" data-current-org="publish"',
    'data-status="intercept-negotiate" data-process-status="待处理" data-intercept-status="已拦截" data-current-org="发布网点"'
)

# 协商派送 - 发布网点 - 已处理
content = content.replace(
    'data-status="intercept-negotiate" data-process-status="processing" data-intercept-status="intercepted" data-current-org="publish"',
    'data-status="intercept-negotiate" data-process-status="已处理" data-intercept-status="已拦截" data-current-org="发布网点"'
)

content = content.replace(
    'data-status="intercept-negotiate" data-process-status="completed" data-intercept-status="intercepted" data-current-org="publish"',
    'data-status="intercept-negotiate" data-process-status="已处理" data-intercept-status="已拦截" data-current-org="发布网点"'
)

# 协商派送 - 处理网点 - 待处理
content = content.replace(
    'data-status="intercept-negotiate" data-process-status="pending" data-intercept-status="intercepted" data-current-org="process"',
    'data-status="intercept-negotiate" data-process-status="待处理" data-intercept-status="已拦截" data-current-org="处理网点"'
)

# 协商派送 - 处理网点 - 已处理
content = content.replace(
    'data-status="intercept-negotiate" data-process-status="processing" data-intercept-status="intercepted" data-current-org="process"',
    'data-status="intercept-negotiate" data-process-status="已处理" data-intercept-status="已拦截" data-current-org="处理网点"'
)

# 退货 - 发布网点 - 拦截中
content = content.replace(
    'data-status="intercept-return" data-process-status="processing" data-intercept-status="intercepting" data-current-org="publish"',
    'data-status="intercept-return" data-process-status="待处理" data-intercept-status="拦截中" data-current-org="发布网点"'
)

# 退货 - 发布网点 - 已拦截 - 待处理
content = content.replace(
    'data-status="intercept-return" data-process-status="completed" data-intercept-status="intercepted" data-current-org="publish"',
    'data-status="intercept-return" data-process-status="待处理" data-intercept-status="已拦截" data-current-org="发布网点"'
)

# 退货 - 处理网点 - 拦截中
content = content.replace(
    'data-status="intercept-return" data-process-status="processing" data-intercept-status="intercepting" data-current-org="process"',
    'data-status="intercept-return" data-process-status="待处理" data-intercept-status="拦截中" data-current-org="处理网点"'
)

# 退货 - 处理网点 - 已拦截 - 待处理
content = content.replace(
    'data-status="intercept-return" data-process-status="completed" data-intercept-status="intercepted" data-current-org="process"',
    'data-status="intercept-return" data-process-status="待处理" data-intercept-status="已拦截" data-current-org="处理网点"'
)

# 等放货通知 - 发布网点 - 拦截中
content = content.replace(
    'data-status="intercept-wait" data-process-status="processing" data-intercept-status="intercepting" data-current-org="publish"',
    'data-status="intercept-wait" data-process-status="待处理" data-intercept-status="拦截中" data-current-org="发布网点"'
)

# 等放货通知 - 发布网点 - 已拦截 - 待处理
content = content.replace(
    'data-status="intercept-wait" data-process-status="completed" data-intercept-status="intercepted" data-current-org="publish"',
    'data-status="intercept-wait" data-process-status="待处理" data-intercept-status="已拦截" data-current-org="发布网点"'
)

# 等放货通知 - 处理网点 - 拦截中
content = content.replace(
    'data-status="intercept-wait" data-process-status="processing" data-intercept-status="intercepting" data-current-org="process"',
    'data-status="intercept-wait" data-process-status="待处理" data-intercept-status="拦截中" data-current-org="处理网点"'
)

# 等放货通知 - 处理网点 - 已拦截
content = content.replace(
    'data-status="intercept-wait" data-process-status="completed" data-intercept-status="intercepted" data-current-org="process"',
    'data-status="intercept-wait" data-process-status="待处理" data-intercept-status="已拦截" data-current-org="处理网点"'
)

# 地址预警 - 发布网点 - 待处理
content = content.replace(
    'data-status="address-warning" data-process-status="pending" data-intercept-status="intercepted" data-current-org="publish"',
    'data-status="address-warning" data-process-status="待处理" data-intercept-status="已拦截" data-current-org="发布网点"'
)

# 地址预警 - 发布网点 - 已处理
content = content.replace(
    'data-status="address-warning" data-process-status="completed" data-intercept-status="intercepted" data-current-org="publish"',
    'data-status="address-warning" data-process-status="已处理" data-intercept-status="已拦截" data-current-org="发布网点"'
)

# 地址预警 - 处理网点 - 待处理
content = content.replace(
    'data-status="address-warning" data-process-status="pending" data-intercept-status="intercepted" data-current-org="process"',
    'data-status="address-warning" data-process-status="待处理" data-intercept-status="已拦截" data-current-org="处理网点"'
)

# 地址预警 - 处理网点 - 已处理
content = content.replace(
    'data-status="address-warning" data-process-status="completed" data-intercept-status="intercepted" data-current-org="process"',
    'data-status="address-warning" data-process-status="已处理" data-intercept-status="已拦截" data-current-org="处理网点"'
)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('表格数据已更新为中文值')
