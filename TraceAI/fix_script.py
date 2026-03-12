#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到错误的位置
wrong_marker = '    </script>\n    <!-- 异常运单详情弹窗 -->'
correct_marker = '''        // 打开上报拦截件弹窗
        function openReportModal() {
            const modal = document.getElementById('reportModal');
            modal.classList.add('active');
        }
    </script>
    <!-- 异常运单详情弹窗 -->'''

# 找到详情弹窗 HTML 的结束位置
detail_modal_end = content.find('    <!-- 上报拦截件弹窗 -->')
if detail_modal_end == -1:
    print('未找到上报拦截件弹窗')
    exit(1)

# 提取详情弹窗 HTML
detail_modal_start = content.find('    <!-- 异常运单详情弹窗 -->')
if detail_modal_start == -1:
    print('未找到详情弹窗')
    exit(1)

detail_modal_html = content[detail_modal_start:detail_modal_end]

# 删除错误的详情弹窗 HTML（在 script 标签后的）
content = content.replace('    </script>\n    <!-- 异常运单详情弹窗 -->' + detail_modal_html + '\n    <!-- 上报拦截件弹窗 -->', 
                         '    </script>\n    <!-- 上报拦截件弹窗 -->')

# 找到应该插入详情弹窗的位置（在上报拦截件弹窗之前）
report_modal_marker = '    <!-- 上报拦截件弹窗 -->'
report_modal_pos = content.find(report_modal_marker)

if report_modal_pos != -1:
    # 在上报拦截件弹窗之前插入详情弹窗
    content = content[:report_modal_pos] + detail_modal_html + '\n' + content[report_modal_pos:]
    print('已修复详情弹窗位置')
else:
    print('未找到上报拦截件弹窗位置')

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('完成修复')
