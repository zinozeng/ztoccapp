#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到两个详情弹窗的位置
first_modal_start = content.find('    <div class="detail-modal-overlay" id="detailModal">', 1900)
second_modal_start = content.find('    <div class="detail-modal-overlay" id="detailModal">', first_modal_start + 10)

if first_modal_start == -1 or second_modal_start == -1:
    print(f'未找到两个弹窗，first={first_modal_start}, second={second_modal_start}')
    exit(1)

# 找到上报拦截件弹窗的位置
report_modal_start = content.find('    <!-- 上报拦截件弹窗 -->')
if report_modal_start == -1:
    print('未找到上报拦截件弹窗')
    exit(1)

# 删除第二个详情弹窗（从 second_modal_start 到 report_modal_start）
second_modal_end = report_modal_start
content = content[:second_modal_start] + content[second_modal_end:]

print(f'已删除第二个详情弹窗 (位置：{second_modal_start} 到 {second_modal_end})')

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('完成')
