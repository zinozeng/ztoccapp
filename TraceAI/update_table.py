#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取文件
with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换表格数据，添加处理网点的数据行
# 首先替换协商派送的处理网点行
content = content.replace(
    '''                            <tr data-status="intercept-negotiate" data-process-status="pending" data-intercept-status="intercepted" data-current-org="publish">
                                <td>ZT20240301001</td>
                                <td><span class="status-tag status-intercept-negotiate">协商派送</span></td>
                                <td>派件网点 B</td>
                                <td>寄件网点 A</td>
                                <td>张三</td>
                                <td>2024-03-01 14:30</td>
                                <td><span class="status-tag status-intercepted">已拦截</span></td>
                                <td><span class="status-tag status-pending-audit">待处理</span></td>
                                <td>-</td>
                                <td>-</td>
                                <td class="action-buttons"></td>
                            </tr>''',
    '''                            <tr data-status="intercept-negotiate" data-process-status="pending" data-intercept-status="intercepted" data-current-org="process">
                                <td>ZT20240301001</td>
                                <td><span class="status-tag status-intercept-negotiate">协商派送</span></td>
                                <td>派件网点 B</td>
                                <td>寄件网点 A</td>
                                <td>张三</td>
                                <td>2024-03-01 14:30</td>
                                <td><span class="status-tag status-intercepted">已拦截</span></td>
                                <td><span class="status-tag status-pending-audit">待处理</span></td>
                                <td>-</td>
                                <td>-</td>
                                <td class="action-buttons"></td>
                            </tr>'''
)

# 添加新的处理网点的协商派送行
content = content.replace(
    '''                            <tr data-status="intercept-negotiate" data-process-status="processing" data-intercept-status="intercepted" data-current-org="publish">
                                <td>ZT20240301002</td>
                                <td><span class="status-tag status-intercept-negotiate">协商派送</span></td>
                                <td>寄件网点 A</td>
                                <td>寄件网点 A</td>
                                <td>李四</td>
                                <td>2024-03-01 15:15</td>
                                <td><span class="status-tag status-intercepted">已拦截</span></td>
                                <td><span class="status-tag status-processing">处理中</span></td>
                                <td>王五</td>
                                <td>2024-03-01 15:45</td>
                                <td class="action-buttons"></td>
                            </tr>''',
    '''                            <tr data-status="intercept-negotiate" data-process-status="processing" data-intercept-status="intercepted" data-current-org="publish">
                                <td>ZT20240301002</td>
                                <td><span class="status-tag status-intercept-negotiate">协商派送</span></td>
                                <td>寄件网点 A</td>
                                <td>寄件网点 A</td>
                                <td>李四</td>
                                <td>2024-03-01 15:15</td>
                                <td><span class="status-tag status-intercepted">已拦截</span></td>
                                <td><span class="status-tag status-processing">处理中</span></td>
                                <td>王五</td>
                                <td>2024-03-01 15:45</td>
                                <td class="action-buttons"></td>
                            </tr>
                            <tr data-status="intercept-negotiate" data-process-status="processing" data-intercept-status="intercepted" data-current-org="process">
                                <td>ZT20240301002</td>
                                <td><span class="status-tag status-intercept-negotiate">协商派送</span></td>
                                <td>寄件网点 A</td>
                                <td>寄件网点 A</td>
                                <td>李四</td>
                                <td>2024-03-01 15:15</td>
                                <td><span class="status-tag status-intercepted">已拦截</span></td>
                                <td><span class="status-tag status-processing">处理中</span></td>
                                <td>王五</td>
                                <td>2024-03-01 15:45</td>
                                <td class="action-buttons"></td>
                            </tr>'''
)

# 更新退货处理网点行
content = content.replace(
    '''                            <tr data-status="intercept-return" data-process-status="processing" data-intercept-status="intercepting" data-current-org="publish">
                                <td>ZT20240301004</td>
                                <td><span class="status-tag status-intercept-return">退货</span></td>
                                <td>派件网点 C</td>
                                <td>派件网点 C</td>
                                <td>孙八</td>
                                <td>2024-03-01 09:15</td>
                                <td><span class="status-tag status-intercepting">拦截中</span></td>
                                <td><span class="status-tag status-processing">退货中</span></td>
                                <td>-</td>
                                <td>-</td>
                                <td class="action-buttons"></td>
                            </tr>''',
    '''                            <tr data-status="intercept-return" data-process-status="processing" data-intercept-status="intercepting" data-current-org="publish">
                                <td>ZT20240301004</td>
                                <td><span class="status-tag status-intercept-return">退货</span></td>
                                <td>派件网点 C</td>
                                <td>派件网点 C</td>
                                <td>孙八</td>
                                <td>2024-03-01 09:15</td>
                                <td><span class="status-tag status-intercepting">拦截中</span></td>
                                <td><span class="status-tag status-processing">退货中</span></td>
                                <td>-</td>
                                <td>-</td>
                                <td class="action-buttons"></td>
                            </tr>
                            <tr data-status="intercept-return" data-process-status="processing" data-intercept-status="intercepting" data-current-org="process">
                                <td>ZT20240301004</td>
                                <td><span class="status-tag status-intercept-return">退货</span></td>
                                <td>派件网点 C</td>
                                <td>派件网点 C</td>
                                <td>孙八</td>
                                <td>2024-03-01 09:15</td>
                                <td><span class="status-tag status-intercepting">拦截中</span></td>
                                <td><span class="status-tag status-processing">退货中</span></td>
                                <td>-</td>
                                <td>-</td>
                                <td class="action-buttons"></td>
                            </tr>'''
)

# 更新等放货通知处理网点行
content = content.replace(
    '''                            <tr data-status="intercept-wait" data-process-status="processing" data-intercept-status="intercepting" data-current-org="publish">
                                <td>ZT20240301006</td>
                                <td><span class="status-tag status-intercept-wait">等放货通知</span></td>
                                <td>中转仓 A</td>
                                <td>中转仓 A</td>
                                <td>郑十一</td>
                                <td>2024-03-01 11:00</td>
                                <td><span class="status-tag status-intercepting">拦截中</span></td>
                                <td><span class="status-tag status-processing">等待通知</span></td>
                                <td>-</td>
                                <td>-</td>
                                <td class="action-buttons"></td>
                            </tr>''',
    '''                            <tr data-status="intercept-wait" data-process-status="processing" data-intercept-status="intercepting" data-current-org="publish">
                                <td>ZT20240301006</td>
                                <td><span class="status-tag status-intercept-wait">等放货通知</span></td>
                                <td>中转仓 A</td>
                                <td>中转仓 A</td>
                                <td>郑十一</td>
                                <td>2024-03-01 11:00</td>
                                <td><span class="status-tag status-intercepting">拦截中</span></td>
                                <td><span class="status-tag status-processing">等待通知</span></td>
                                <td>-</td>
                                <td>-</td>
                                <td class="action-buttons"></td>
                            </tr>
                            <tr data-status="intercept-wait" data-process-status="processing" data-intercept-status="intercepting" data-current-org="process">
                                <td>ZT20240301006</td>
                                <td><span class="status-tag status-intercept-wait">等放货通知</span></td>
                                <td>中转仓 A</td>
                                <td>中转仓 A</td>
                                <td>郑十一</td>
                                <td>2024-03-01 11:00</td>
                                <td><span class="status-tag status-intercepting">拦截中</span></td>
                                <td><span class="status-tag status-processing">等待通知</span></td>
                                <td>-</td>
                                <td>-</td>
                                <td class="action-buttons"></td>
                            </tr>'''
)

# 更新地址预警处理网点行
content = content.replace(
    '''                            <tr data-status="address-warning" data-process-status="pending" data-intercept-status="intercepted" data-current-org="publish">
                                <td>ZT20240301008</td>
                                <td><span class="status-tag status-address-warning">地址预警</span></td>
                                <td>寄件网点 A</td>
                                <td>系统自动</td>
                                <td>系统</td>
                                <td>2024-03-01 16:20</td>
                                <td><span class="status-tag status-intercepted">已拦截</span></td>
                                <td><span class="status-tag status-processing">待处理</span></td>
                                <td>-</td>
                                <td>-</td>
                                <td class="action-buttons"></td>
                            </tr>''',
    '''                            <tr data-status="address-warning" data-process-status="pending" data-intercept-status="intercepted" data-current-org="publish">
                                <td>ZT20240301008</td>
                                <td><span class="status-tag status-address-warning">地址预警</span></td>
                                <td>寄件网点 A</td>
                                <td>系统自动</td>
                                <td>系统</td>
                                <td>2024-03-01 16:20</td>
                                <td><span class="status-tag status-intercepted">已拦截</span></td>
                                <td><span class="status-tag status-processing">待处理</span></td>
                                <td>-</td>
                                <td>-</td>
                                <td class="action-buttons"></td>
                            </tr>
                            <tr data-status="address-warning" data-process-status="pending" data-intercept-status="intercepted" data-current-org="process">
                                <td>ZT20240301008</td>
                                <td><span class="status-tag status-address-warning">地址预警</span></td>
                                <td>寄件网点 A</td>
                                <td>系统自动</td>
                                <td>系统</td>
                                <td>2024-03-01 16:20</td>
                                <td><span class="status-tag status-intercepted">已拦截</span></td>
                                <td><span class="status-tag status-processing">待处理</span></td>
                                <td>-</td>
                                <td>-</td>
                                <td class="action-buttons"></td>
                            </tr>'''
)

# 更新统计数量
content = content.replace('共 12 条', '共 17 条')
content = content.replace('class="tab-count">12</span>', 'class="tab-count">17</span>')
content = content.replace('class="tab-count">3</span>', 'class="tab-count">6</span>')  # 协商派送现在有6条（3个网点×2种类型）
content = content.replace('class="tab-count">2</span>', 'class="tab-count">4</span>')  # 退货现在有4条（2个网点×2种类型）
content = content.replace('class="tab-count">2</span>', 'class="tab-count">4</span>')  # 等放货通知现在有4条（2个网点×2种类型）
content = content.replace('class="tab-count">2</span>', 'class="tab-count">4</span>')  # 地址预警现在有4条（2个网点×2种类型）

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('表格数据已更新')
