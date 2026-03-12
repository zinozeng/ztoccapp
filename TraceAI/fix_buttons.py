#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取文件
with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修改协商派送在发布网点、已处理状态下的按钮
old_code = '''            // 根据规则生成按钮（基于用户提供的表格）
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
                }'''

new_code = '''            // 根据规则生成按钮（基于用户提供的表格）
            if (status === 'intercept-negotiate') { // 协商派送 - 已拦截
                if (currentOrg === '发布网点') {
                    if (processStatus === '待处理') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">撤销</span>`);
                    } else { // 已处理
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">改单</span>`);
                    }
                } else { // 处理网点
                    if (processStatus === '待处理') {
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">处理</span>`);
                    } else { // 已处理
                        buttons.push(`<span class="action-link" onclick="viewDetail('${orderNo}')">查看</span>`);
                    }
                }'''

content = content.replace(old_code, new_code)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('已将协商派送发布网点已处理状态的按钮修改为"查看 改单"')
