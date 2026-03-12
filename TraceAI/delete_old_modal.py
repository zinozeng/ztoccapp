#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到旧弹窗的起始和结束
old_start_marker = '    <!-- 详情弹窗 -->\n    <div class="modal-overlay" id="detailModal">'
old_end_marker = '        // 打开上报拦截件弹窗'

old_start = content.find(old_start_marker)
old_end = content.find(old_end_marker)

if old_start != -1 and old_end != -1:
    # 删除旧弹窗
    content = content[:old_start] + content[old_end:]
    print(f'已删除旧弹窗 (位置：{old_start} 到 {old_end})')
else:
    print(f'未找到旧弹窗，start={old_start}, end={old_end}')

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('完成')
