#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取文件
with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 更新二级筛选标签的 data 属性
content = content.replace(
    'data-intercept-status="all"',
    'data-intercept-status="全部"'
)
content = content.replace(
    'data-intercept-status="intercepting"',
    'data-intercept-status="拦截中"'
)
content = content.replace(
    'data-intercept-status="intercepted"',
    'data-intercept-status="已拦截"'
)

# 更新筛选函数的调用
content = content.replace(
    "filterTable(status, null, document.querySelector('.sub-tab-item.active').dataset.interceptStatus);",
    "filterTable(status, null, document.querySelector('.sub-tab-item.active').dataset.interceptStatus || '全部');"
)

# 替换整个 generateActionButtons 函数
old_function = '''        // 生成操作按钮
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
            if (status === 'intercept-negotiate') { // 协商派送 - 已拦截
                if (currentOrg === 'publish') {
                    if (processStatus === 'pending') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">修改</span>`);
                    }
                } else {
                    if (processStatus === 'pending') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                    } else {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                }
            } else if (status === 'intercept-return') { // 退货
                if (currentOrg === 'publish') {
                    if (interceptStatus === 'intercepting') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else {
                        if (processStatus === 'pending') {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                        } else {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        }
                    }
                } else {
                    if (interceptStatus === 'intercepting') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">拦截</span>`);
                    } else {
                        if (processStatus === 'pending') {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">退货</span>`);
                        } else {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        }
                    }
                }
            } else if (status === 'intercept-wait') { // 等放货通知
                if (currentOrg === 'publish') {
                    if (interceptStatus === 'intercepting') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else {
                        if (processStatus === 'pending') {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">放货</span>`);
                        } else {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        }
                    }
                } else {
                    if (interceptStatus === 'intercepting') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">拦截</span>`);
                    } else {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                }
            } else if (status === 'address-warning') { // 地址预警 - 已拦截
                if (currentOrg === 'publish') {
                    if (processStatus === 'pending') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                } else {
                    if (processStatus === 'pending') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                    } else {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                }
            }
            
            actionCell.innerHTML = buttons.join('');
        }'''

new_function = '''        // 生成操作按钮
        function generateActionButtons(row) {
            const currentOrg = row.dataset.currentOrg; // 发布网点 或 处理网点
            const status = row.dataset.status; // intercept-negotiate, intercept-return, intercept-wait, address-warning
            const interceptStatus = row.dataset.interceptStatus; // 拦截中 或 已拦截
            const processStatus = row.dataset.processStatus; // 待处理 或 已处理
            
            const actionCell = row.querySelector('.action-buttons');
            if (!actionCell) return;
            
            let buttons = [];
            const orderNo = row.cells[0].textContent;
            
            // 根据规则生成按钮（基于用户提供的表格）
            if (status === 'intercept-negotiate') { // 协商派送 - 已拦截
                if (currentOrg === '发布网点') {
                    if (processStatus === '待处理') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else { // 已处理
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">修改</span>`);
                    }
                } else { // 处理网点
                    if (processStatus === '待处理') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                    } else { // 已处理
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                }
            } else if (status === 'intercept-return') { // 退货
                if (currentOrg === '发布网点') {
                    if (interceptStatus === '拦截中') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else { // 已拦截
                        if (processStatus === '待处理') {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                        } else {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        }
                    }
                } else { // 处理网点
                    if (interceptStatus === '拦截中') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">拦截</span>`);
                    } else { // 已拦截
                        if (processStatus === '待处理') {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">退货</span>`);
                        } else {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        }
                    }
                }
            } else if (status === 'intercept-wait') { // 等放货通知
                if (currentOrg === '发布网点') {
                    if (interceptStatus === '拦截中') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else { // 已拦截
                        if (processStatus === '待处理') {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">放货</span>`);
                        } else {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        }
                    }
                } else { // 处理网点
                    if (interceptStatus === '拦截中') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">拦截</span>`);
                    } else { // 已拦截
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                }
            } else if (status === 'address-warning') { // 地址预警 - 已拦截
                if (currentOrg === '发布网点') {
                    if (processStatus === '待处理') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else { // 已处理
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                } else { // 处理网点
                    if (processStatus === '待处理') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                    } else { // 已处理
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                }
            }
            
            actionCell.innerHTML = buttons.join('');
        }'''

content = content.replace(old_function, new_function)

# 更新 filterTable 函数使用中文值
old_filter = '''        // 表格筛选
        function filterTable(status = 'all', processStatus = null, interceptStatus = 'all') {
            const rows = document.querySelectorAll('tbody tr');
            rows.forEach(row => {
                const rowStatus = row.dataset.status;
                const rowProcessStatus = row.dataset.processStatus;
                const rowInterceptStatus = row.dataset.interceptStatus;
                
                const statusMatch = status === 'all' || rowStatus === status;
                const processStatusMatch = processStatus === null || rowProcessStatus === processStatus;
                const interceptStatusMatch = interceptStatus === 'all' || rowInterceptStatus === interceptStatus;
                
                if (statusMatch && processStatusMatch && interceptStatusMatch) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        }'''

new_filter = '''        // 表格筛选
        function filterTable(status = 'all', processStatus = null, interceptStatus = '全部') {
            const rows = document.querySelectorAll('tbody tr');
            rows.forEach(row => {
                const rowStatus = row.dataset.status;
                const rowProcessStatus = row.dataset.processStatus;
                const rowInterceptStatus = row.dataset.interceptStatus;
                
                const statusMatch = status === 'all' || rowStatus === status;
                const processStatusMatch = processStatus === null || rowProcessStatus === processStatus;
                const interceptStatusMatch = interceptStatus === '全部' || rowInterceptStatus === interceptStatus;
                
                if (statusMatch && processStatusMatch && interceptStatusMatch) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        }'''

content = content.replace(old_filter, new_filter)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('已更新筛选和按钮生成逻辑为中文值')
