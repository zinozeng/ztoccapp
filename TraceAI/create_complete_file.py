#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取当前文件
with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到</script>标签的位置
script_end = content.find('</script>')
if script_end == -1:
    print('未找到</script>标签')
    exit(1)

# 找到详情弹窗的开始位置
detail_modal_start = content.find('<!-- 异常运单详情弹窗 -->', script_end)
if detail_modal_start == -1:
    print('未找到详情弹窗')
    exit(1)

# 提取详情弹窗及之后的内容
detail_modal_and_after = content[detail_modal_start:]

# 提取</script>之前的内容（包括</script>）
before_script_end = content[:script_end + len('</script>')]

# 重新组合
new_content = before_script_end + '\n' + detail_modal_and_after

with open('异常运单管理_fixed.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('已创建修复后的文件')
print(f'原文件大小：{len(content)}')
print(f'新文件大小：{len(new_content)}')
