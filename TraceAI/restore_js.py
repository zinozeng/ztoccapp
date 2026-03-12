#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 openReportModal 函数的位置
marker = '''        // 打开上报拦截件弹窗
        function openReportModal() {
            const modal = document.getElementById('reportModal');
            modal.classList.add('active');
        }'''

# 新的 JavaScript 代码
new_js = '''        // 生成操作按钮
        function generateActionButtons(row) {
            const currentOrg = row.dataset.currentOrg;
            const status = row.dataset.status;
            const interceptStatus = row.dataset.interceptStatus;
            const processStatus = row.dataset.processStatus;
            
            const actionCell = row.querySelector('.action-buttons');
            if (!actionCell) return;
            
            let buttons = [];
            const orderNo = row.cells[0].textContent;
            
            if (status === 'intercept-negotiate') {
                if (currentOrg === '发布网点') {
                    if (processStatus === '待处理') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">改单</span>`);
                    }
                } else {
                    if (processStatus === '待处理') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                    } else {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                }
            } else if (status === 'intercept-return') {
                if (currentOrg === '发布网点') {
                    if (interceptStatus === '拦截中') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else {
                        if (processStatus === '待处理') {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                        } else {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        }
                    }
                } else {
                    if (interceptStatus === '拦截中') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">拦截</span>`);
                    } else {
                        if (processStatus === '待处理') {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">退货</span>`);
                        } else {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        }
                    }
                }
            } else if (status === 'intercept-wait') {
                if (currentOrg === '发布网点') {
                    if (interceptStatus === '拦截中') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else {
                        if (processStatus === '待处理') {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">放货</span>`);
                        } else {
                            buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        }
                    }
                } else {
                    if (interceptStatus === '拦截中') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">拦截</span>`);
                    } else {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                }
            } else if (status === 'address-warning') {
                if (currentOrg === '发布网点') {
                    if (processStatus === '待处理') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                } else {
                    if (processStatus === '待处理') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                    } else {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                }
            }
            
            actionCell.innerHTML = buttons.join('');
        }
        
        // 初始化所有行的操作按钮
        function initActionButtons() {
            document.querySelectorAll('tbody tr').forEach(row => {
                generateActionButtons(row);
            });
        }
        
        // 查询按钮
        const queryBtn = document.querySelector('.filter-section .btn-primary');
        if (queryBtn) {
            queryBtn.addEventListener('click', function() {
                const inputs = document.querySelectorAll('.filter-section .filter-input');
                const selects = document.querySelectorAll('.filter-section .filter-select');
                
                const orderNo = inputs[0].value.trim();
                const processBranch = inputs[1].value.trim();
                const publishBranch = inputs[2].value.trim();
                const exceptionType = selects[0].value;
                const processStatus = selects[1].value;
                
                filterByConditions(orderNo, processBranch, publishBranch, exceptionType, processStatus);
            });
        }
        
        // 根据筛选条件过滤表格
        function filterByConditions(orderNo, processBranch, publishBranch, exceptionType, processStatus) {
            const rows = document.querySelectorAll('tbody tr');
            rows.forEach(row => {
                const rowOrderNo = row.cells[0].textContent.trim();
                const rowProcessBranch = row.cells[2].textContent.trim();
                const rowPublishBranch = row.cells[3].textContent.trim();
                const rowStatus = row.dataset.status;
                const rowProcessStatus = row.dataset.processStatus;
                
                const orderNoMatch = !orderNo || rowOrderNo.includes(orderNo);
                const processBranchMatch = !processBranch || rowProcessBranch.includes(processBranch);
                const publishBranchMatch = !publishBranch || rowPublishBranch.includes(publishBranch);
                const exceptionTypeMatch = !exceptionType || rowStatus === exceptionType;
                const processStatusMatch = !processStatus || rowProcessStatus === processStatus;
                
                if (orderNoMatch && processBranchMatch && publishBranchMatch && exceptionTypeMatch && processStatusMatch) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
            
            showNotification('查询成功', 'success');
        }
        
        // 重置按钮
        const resetBtn = document.querySelector('.filter-section .btn-default');
        if (resetBtn) {
            resetBtn.addEventListener('click', function() {
                const inputs = document.querySelectorAll('.filter-section .filter-input');
                const selects = document.querySelectorAll('.filter-section .filter-select');
                
                inputs.forEach(input => input.value = '');
                selects.forEach(select => select.value = '');
                
                const rows = document.querySelectorAll('tbody tr');
                rows.forEach(row => {
                    row.style.display = '';
                });
                
                showNotification('已重置', 'info');
            });
        }
        
        // 关闭详情页
        function closeDetailModal() {
            const modal = document.getElementById('detailModal');
            if (modal) {
                modal.classList.remove('active');
            }
        }
        
''' + marker

content = content.replace(marker, new_js)

# 在页面加载完成后初始化按钮
old_load = '''        // 页面加载完成后初始化
        window.addEventListener('DOMContentLoaded', function() {
            initActionButtons();
        });'''

new_load = '''        // 页面加载完成后初始化
        window.addEventListener('DOMContentLoaded', function() {
            initActionButtons();
        });'''

if old_load not in content:
    # 在 openReportModal 之前添加初始化代码
    content = content.replace(
        '        // 打开上报拦截件弹窗',
        '''        // 页面加载完成后初始化
        window.addEventListener('DOMContentLoaded', function() {
            initActionButtons();
        });
        
        // 打开上报拦截件弹窗'''
    )

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('已恢复 JavaScript 代码')
