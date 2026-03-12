#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取文件
with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换查询按钮和重置按钮的事件监听器，使用更准确的选择器
old_code = '''        // 查询按钮
        document.querySelector('.filter-section .btn-primary').addEventListener('click', function() {
            const orderNo = document.querySelectorAll('.filter-input')[0].value.trim();
            const processBranch = document.querySelectorAll('.filter-input')[1].value.trim();
            const publishBranch = document.querySelectorAll('.filter-input')[2].value.trim();
            const exceptionType = document.querySelector('.filter-section select:nth-of-type(1)').value;
            const processStatus = document.querySelector('.filter-section select:nth-of-type(2)').value;
            
            filterByConditions(orderNo, processBranch, publishBranch, exceptionType, processStatus);
        });

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
        document.querySelector('.filter-section .btn-default:nth-of-type(2)').addEventListener('click', function() {
            document.querySelectorAll('.filter-input').forEach(input => input.value = '');
            document.querySelectorAll('.filter-select').forEach(select => select.value = '');
            
            const rows = document.querySelectorAll('tbody tr');
            rows.forEach(row => {
                row.style.display = '';
            });
            
            showNotification('已重置', 'info');
        });'''

new_code = '''        // 查询按钮
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
        }'''

content = content.replace(old_code, new_code)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('已修复查询和重置功能')
