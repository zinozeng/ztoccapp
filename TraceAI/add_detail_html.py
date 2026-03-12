#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 在关闭 modal 函数后添加 viewDetail 函数
old_view_detail = '''        // 打开详情页
        function viewDetail(orderNo) {
            const modal = document.getElementById('detailModal');
            modal.classList.add('active');
        }'''

new_view_detail = '''        // 打开详情页
        function viewDetail(orderNo) {
            const modal = document.getElementById('detailModal');
            modal.classList.add('active');
        }
        
        // 关闭详情页
        function closeDetailModal() {
            const modal = document.getElementById('detailModal');
            modal.classList.remove('active');
        }'''

content = content.replace(old_view_detail, new_view_detail)

# 添加详情弹窗 HTML
old_report_modal = '''    <!-- 上报拦截件弹窗 -->
    <div class="modal-overlay" id="reportModal">'''

new_detail_html = '''    <!-- 异常运单详情弹窗 -->
    <div class="detail-modal-overlay" id="detailModal">
        <div class="detail-modal">
            <!-- 头部 -->
            <div class="detail-header">
                <div class="detail-header-left">
                    <div class="detail-title-row">
                        <h2 class="detail-title">异常运单详情</h2>
                        <div class="detail-tags">
                            <span class="detail-tag">试单管理</span>
                            <span class="detail-tag">异常运单</span>
                            <span class="detail-tag">协商派送</span>
                        </div>
                    </div>
                    <div class="detail-info">
                        <span class="detail-info-item">运单编号：ZT20240301001</span>
                        <span class="detail-info-item">异常类型：协商派送</span>
                        <span class="detail-info-item">当前状态：已拦截</span>
                    </div>
                </div>
                <button class="detail-close" onclick="closeDetailModal()">&times;</button>
            </div>
            
            <!-- 内容区 -->
            <div class="detail-content">
                <!-- 左侧信息 -->
                <div class="detail-left">
                    <!-- 运单基础信息 -->
                    <div class="detail-card">
                        <div class="card-header">
                            <div>
                                <h3 class="card-title">运单基础信息</h3>
                                <p class="card-subtitle">展示寄件及收件信息和货物信息</p>
                            </div>
                        </div>
                        <div class="info-grid">
                            <div class="info-block">
                                <span class="label">寄件人</span>
                                <span class="value">王先生 / 138xxxx0001</span>
                            </div>
                            <div class="info-block">
                                <span class="label">收件人</span>
                                <span class="value">李先生 / 139xxxx0002</span>
                            </div>
                            <div class="info-block">
                                <span class="label">货物信息</span>
                                <span class="value">冷链样品 / 2 件 / 10KG</span>
                            </div>
                            <div class="info-block-full">
                                <span class="label">寄件地址</span>
                                <span class="value">上海市浦东新区锦绣东路 1088 号</span>
                            </div>
                            <div class="info-block-full">
                                <span class="label">收件地址</span>
                                <span class="value">杭州市余杭区五常街道文一西路 969 号</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 异常信息 -->
                    <div class="detail-card">
                        <div class="card-header">
                            <div>
                                <h3 class="card-title">异常信息</h3>
                                <p class="card-subtitle">寄件网点发起协商申请，派件网点查看并审核</p>
                            </div>
                        </div>
                        <div class="info-grid">
                            <div class="info-block">
                                <span class="label">异常原因</span>
                                <span class="value">客户临时变更派送要求</span>
                            </div>
                            <div class="info-block">
                                <span class="label">期望处理方式</span>
                                <span class="value">电话协商后再派送</span>
                            </div>
                            <div class="info-block-full">
                                <span class="label">异常情况说明</span>
                                <span class="value">收件人要求更改派送时间，需派件网点先电话确认具体时间，再次投递前需安排当日送达。</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 审核处理区 -->
                    <div class="detail-card">
                        <div class="card-header">
                            <h3 class="card-title">审核处理区</h3>
                        </div>
                        <div class="alert-box">
                            <span class="alert-icon">●</span>
                            <div class="alert-content">
                                <span class="alert-text">当前您是角色：派件网点，仅可审核，不可修改发起内容</span>
                            </div>
                        </div>
                        <div class="audit-options">
                            <div class="radio-group">
                                <input type="radio" name="audit" id="audit-pass" checked>
                                <label for="audit-pass">审核通过</label>
                            </div>
                            <div class="radio-group">
                                <input type="radio" name="audit" id="audit-reject">
                                <label for="audit-reject">审核驳回</label>
                            </div>
                        </div>
                        <div class="audit-comment-box">
                            <div class="comment-label">审核意见：</div>
                            <div class="comment-text">建议先联系客户确认签收时间。</div>
                        </div>
                    </div>
                </div>
                
                <!-- 右侧流程 -->
                <div class="detail-right">
                    <!-- 流程状态 -->
                    <div class="detail-card">
                        <div class="card-header">
                            <h3 class="card-title">流程状态</h3>
                        </div>
                        <div class="process-section">
                            <p class="process-subtitle">异常运单处理节点与当前执行动作</p>
                            <div class="timeline">
                                <div class="timeline-node completed">
                                    <div class="node-dot"></div>
                                    <span class="node-label">寄件网点发起</span>
                                </div>
                                <div class="timeline-connector active"></div>
                                <div class="timeline-node current">
                                    <div class="node-dot"></div>
                                    <span class="node-label">派件网点审核</span>
                                </div>
                                <div class="timeline-connector"></div>
                                <div class="timeline-node">
                                    <div class="node-dot"></div>
                                    <span class="node-label">寄件网点处理</span>
                                </div>
                            </div>
                            <div class="current-node-box">
                                <div class="current-node-label">当前节点</div>
                                <div class="current-node-title">派件网点审核</div>
                                <p class="current-node-desc">寄件网点发起协商网点可发起：改件网点审核通过或驳回后，流转至寄件网点处理结果。</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 权限说明 -->
                    <div class="detail-card">
                        <div class="card-header">
                            <h3 class="card-title">权限说明</h3>
                        </div>
                        <div class="permission-table">
                            <div class="permission-row">
                                <span class="perm-label">当前登录角色</span>
                                <span class="perm-value">派件网点</span>
                            </div>
                            <div class="permission-row">
                                <span class="perm-label">当前可发起</span>
                                <span class="perm-value">寄件网点、派件网点</span>
                            </div>
                            <div class="permission-row">
                                <span class="perm-label">当前可执行动作</span>
                                <span class="perm-value">审核通过 / 审核驳回</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 处理记录 -->
                    <div class="detail-card">
                        <div class="card-header">
                            <h3 class="card-title">处理记录</h3>
                        </div>
                        <div class="record-list">
                            <div class="record-item">
                                <span class="record-time">2024-03-01 14:30</span>
                                <div class="record-content">
                                    <div class="record-user">寄件网点 张三</div>
                                    <div class="record-action">发起协商派送</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 底部 -->
            <div class="detail-footer">
                <div class="footer-note">
                    统一规范说明：● 表示必，红色框定展示范围和权限，便于快速查看邮件。
                </div>
                <div class="footer-buttons">
                    <button class="detail-btn detail-btn-default" onclick="closeDetailModal()">审核驳回</button>
                    <button class="detail-btn detail-btn-primary" onclick="closeDetailModal()">审核通过</button>
                </div>
            </div>
        </div>
    </div>
    
    <!-- 上报拦截件弹窗 -->
    <div class="modal-overlay" id="reportModal">'''

content = content.replace(old_report_modal, new_detail_html)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('已添加详情弹窗 HTML')
