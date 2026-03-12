#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取文件
with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 更新处理状态下拉框的值
content = content.replace(
    '''<option value="pending">待处理</option>
                            <option value="completed">已处理</option>''',
    '''<option value="待处理">待处理</option>
                            <option value="已处理">已处理</option>'''
)

# 替换查询按钮的事件监听器
old_query = '''        // 查询按钮
        document.querySelector('.filter-section .btn-primary').addEventListener('click', function() {
            showNotification('查询成功', 'info');
        });'''

new_query = '''        // 查询按钮
        document.querySelector('.filter-section .btn-primary').addEventListener('click', function() {
            const orderNo = document.querySelectorAll('.filter-input')[0].value.trim();
            const processBranch = document.querySelectorAll('.filter-input')[1].value.trim();
            const publishBranch = document.querySelectorAll('.filter-input')[2].value.trim();
            const exceptionType = document.querySelector('.filter-section select:nth-of-type(1)').value;
            const processStatus = document.querySelector('.filter-section select:nth-of-type(2)').value;
            
            filterByConditions(orderNo, processBranch, publishBranch, exceptionType, processStatus);
        });'''

content = content.replace(old_query, new_query)

# 添加新的筛选函数
old_script_end = '''        // 打开上报拦截件弹窗
        function openReportModal() {
            const modal = document.getElementById('reportModal');
            modal.classList.add('active');
        }'''

new_script_end = '''        // 根据筛选条件过滤表格
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
        });
        
        // 打开上报拦截件弹窗
        function openReportModal() {
            const modal = document.getElementById('reportModal');
            modal.classList.add('active');
        }'''

content = content.replace(old_script_end, new_script_end)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('已修复查询功能')
