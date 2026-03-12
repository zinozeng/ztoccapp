#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取文件
with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 要插入的代码
new_code = '''
        // 生成操作按钮
        function generateActionButtons(row) {
            const currentOrg = row.dataset.currentOrg;
            const status = row.dataset.status;
            const interceptStatus = row.dataset.interceptStatus;
            const processStatus = row.dataset.processStatus;
            
            const actionCell = row.querySelector('.action-buttons');
            if (!actionCell) return;
            
            let buttons = [];
            const orderNo = row.cells[0].textContent;
            
            // 根据规则生成按钮（基于用户提供的表格）
            if (status === 'intercept-negotiate'): // 协商派送 - 已拦截
                if (currentOrg === 'publish'):
                    if (processStatus === 'pending'):
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    else:
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">修改</span>`);
                else:
                    if (processStatus === 'pending'):
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                    else:
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
            else if (status === 'intercept-return'): // 退货
                if (currentOrg === 'publish'):
                    if (interceptStatus === 'intercepting'):
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    else:
                        if (processStatus === 'pending'):
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                        else:
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                else:
                    if (interceptStatus === 'intercepting'):
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">拦截</span>`);
                    else:
                        if (processStatus === 'pending'):
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">退货</span>`);
                        else:
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
            else if (status === 'intercept-wait'): // 等放货通知
                if (currentOrg === 'publish'):
                    if (interceptStatus === 'intercepting'):
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    else:
                        if (processStatus === 'pending'):
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">放货</span>`);
                        else:
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                else:
                    if (interceptStatus === 'intercepting'):
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">拦截</span>`);
                    else:
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
            else if (status === 'address-warning'): // 地址预警 - 已拦截
                if (currentOrg === 'publish'):
                    if (processStatus === 'pending'):
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    else:
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                else:
                    if (processStatus === 'pending'):
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                    else:
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
            
            actionCell.innerHTML = buttons.join('');
        }

        // 初始化所有行的操作按钮
        function initActionButtons() {
            document.querySelectorAll('tbody tr').forEach(row => {
                generateActionButtons(row);
            });
        }

        // 页面加载完成后初始化
        window.addEventListener('DOMContentLoaded', function() {
            initActionButtons();
        });
'''

# 找到插入位置（在 filterTable 函数结束后）
lines = content.split('\n')
insert_index = None

for i, line in enumerate(lines):
    if 'function filterTable(status' in line:
        # 找到函数结束的大括号
        brace_count = 0
        for j in range(i, len(lines)):
            if '{' in lines[j]:
                brace_count += lines[j].count('{')
            if '}' in lines[j]:
                brace_count -= lines[j].count('}')
                if brace_count == 0:
                    insert_index = j + 1
                    break
        break

if insert_index:
    lines.insert(insert_index, new_code)
    with open('异常运单管理.html', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'成功在{insert_index}行后插入代码')
else:
    print('未找到插入位置')
