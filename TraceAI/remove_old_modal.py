#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 删除旧的详情弹窗（从 info-value id="detailOrderNo" 往上找到整个弹窗）
# 找到旧弹窗的位置
old_modal_start = content.find('<!-- 异常运单详情弹窗 -->')
old_modal_end = content.find('<!-- 上报拦截件弹窗 -->')

if old_modal_start != -1 and old_modal_end != -1:
    # 检查是否是我们新添加的弹窗
    content_after_start = content[old_modal_start:old_modal_start+500]
    if 'detail-modal-overlay' not in content_after_start:
        # 这是旧弹窗，删除它
        # 找到前一个 closing div
        prev_closing = content.rfind('</div>', 0, old_modal_start)
        if prev_closing != -1:
            # 找到旧弹窗的结束
            old_modal_content = content[old_modal_start:old_modal_end]
            # 计算有多少个 </div>
            content = content[:old_modal_start] + content[old_modal_end:]
            print('已删除旧弹窗')
        else:
            print('未找到旧弹窗起始位置')
    else:
        print('当前弹窗是新弹窗')
else:
    print('弹窗位置异常')

# 更新 viewDetail 函数，移除不存在的元素引用
old_view_detail = '''        function viewDetail(orderNo) {
            currentOrderNo = orderNo;
            const modal = document.getElementById('detailModal');
            
            // 模拟数据填充
            document.getElementById('detailOrderNo').textContent = orderNo;
            
            modal.classList.add('active');
        }'''

new_view_detail = '''        function viewDetail(orderNo) {
            const modal = document.getElementById('detailModal');
            if (modal) {
                modal.classList.add('active');
            }
        }'''

content = content.replace(old_view_detail, new_view_detail)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('已更新 viewDetail 函数')
