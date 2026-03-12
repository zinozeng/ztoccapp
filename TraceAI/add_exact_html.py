#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 更新 viewDetail 函数
old_func = '''        // 打开详情页
        function viewDetail(orderNo) {
            const modal = document.getElementById('detailModal');
            modal.classList.add('active');
        }'''

new_func = '''        // 打开详情页
        function viewDetail(orderNo) {
            const modal = document.getElementById('detailModal');
            if (modal) {
                modal.classList.add('active');
            }
        }
        
        // 关闭详情页
        function closeDetailModal() {
            const modal = document.getElementById('detailModal');
            if (modal) {
                modal.classList.remove('active');
            }
        }'''

content = content.replace(old_func, new_func)

# 添加 HTML
old_report = '''    <!-- 上报拦截件弹窗 -->
    <div class="modal-overlay" id="reportModal">'''

new_html = '''    <!-- 异常运单详情弹窗 -->
    <div class="detail-modal-overlay" id="detailModal">
        <div class="detail-modal">
            <!-- 头部 -->
            <div class="detail-header">
                <div class="detail-header-left">
                    <h2 class="detail-title">异常运单详情</h2>
                    <div class="detail-tags-row">
                        <span class="detail-tag">试单管理</span>
                        <span class="detail-tag">异常运单</span>
                        <span class="detail-tag">协商派送</span>
                    </div>
                    <div class="detail-info-row">
                        <span class="detail-info-item">运单编号：ZT20240301001</span>
                        <span class="detail-info-item">异常类型：协商派送</span>
                        <span class="detail-info-item">当前状态：已拦截</span>
                    </div>
                </div>
                <button class="detail-close-btn" onclick="closeDetailModal()">&times;</button>
            </div>
            
            <!-- 主体内容 -->
            <div class="detail-body">
                <!-- 左侧主内容区 -->
                <div class="detail-main">
                    <!-- 运单基础信息 -->
                    <div class="detail-panel">
                        <div class="panel-header">
                            <h3 class="panel-title">运单基础信息</h3>
                            <p class="panel-subtitle">展示寄件及收件信息和货物信息</p>
                        </div>
                        <div class="info-section">
                            <div class="info-field">
                                <span class="field-label">寄件人</span>
                                <span class="field-value">王先生 / 138xxxx0001</span>
                            </div>
                            <div class="info-field">
                                <span class="field-label">收件人</span>
                                <span class="field-value">李先生 / 139xxxx0002</span>
                            </div>
                            <div class="info-field">
                                <span class="field-label">货物信息</span>
                                <span class="field-value">冷链样品 / 2 件 / 10KG</span>
                            </div>
                            <div class="info-field-full">
                                <span class="field-label">寄件地址</span>
                                <span class="field-value">上海市浦东新区锦绣东路 1088 号</span>
                            </div>
                            <div class="info-field-full">
                                <span class="field-label">收件地址</span>
                                <span class="field-value">杭州市余杭区五常街道文一西路 969 号</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 异常信息 -->
                    <div class="detail-panel">
                        <div class="panel-header">
                            <h3 class="panel-title">异常信息</h3>
                            <p class="panel-subtitle">寄件网点发起协商申请，派件网点查看并审核</p>
                        </div>
                        <div class="info-section">
                            <div class="info-field">
                                <span class="field-label">异常原因</span>
                                <span class="field-value">客户临时变更派送要求</span>
                            </div>
                            <div class="info-field">
                                <span class="field-label">期望处理方式</span>
                                <span class="field-value">电话协商后再派送</span>
                            </div>
                            <div class="info-field-full">
                                <span class="field-label">异常情况说明</span>
                                <span class="field-value">收件人要求更改派送时间，需派件网点先电话确认具体时间，再次投递前需安排当日送达。</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 审核处理区 -->
                    <div class="detail-panel">
                        <div class="panel-header">
                            <h3 class="panel-title">审核处理区</h3>
                        </div>
                        <div class="notice-box">
                            <span class="notice-dot">●</span>
                            <span class="notice-text">当前您是角色：派件网点，仅可审核，不可修改发起内容</span>
                        </div>
                        <div class="audit-options">
                            <div class="audit-option">
                                <input type="radio" name="audit" id="audit-pass" checked>
                                <label for="audit-pass">审核通过</label>
                            </div>
                            <div class="audit-option">
                                <input type="radio" name="audit" id="audit-reject">
                                <label for="audit-reject">审核驳回</label>
                            </div>
                        </div>
                        <div class="audit-comment">
                            <div class="comment-title">审核意见：</div>
                            <div class="comment-content">建议先联系客户确认签收时间。</div>
                        </div>
                    </div>
                </div>
                
                <!-- 右侧边栏 -->
                <div class="detail-side">
                    <!-- 流程状态 -->
                    <div class="detail-panel">
                        <div class="panel-header">
                            <h3 class="panel-title">流程状态</h3>
                        </div>
                        <div class="process-block">
                            <p class="process-desc">异常运单处理节点与当前执行动作</p>
                            <div class="process-steps">
                                <div class="process-step completed">
                                    <div class="step-circle"></div>
                                    <span class="step-text">寄件网点发起</span>
                                </div>
                                <div class="step-line active"></div>
                                <div class="process-step current">
                                    <div class="step-circle"></div>
                                    <span class="step-text">派件网点审核</span>
                                </div>
                                <div class="step-line"></div>
                                <div class="process-step">
                                    <div class="step-circle"></div>
                                    <span class="step-text">寄件网点处理</span>
                                </div>
                            </div>
                            <div class="current-step-box">
                                <div class="current-step-label">当前节点</div>
                                <div class="current-step-title">派件网点审核</div>
                                <p class="current-step-desc">寄件网点发起协商网点可发起：改件网点审核通过或驳回后，流转至寄件网点处理结果。</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 权限说明 -->
                    <div class="detail-panel">
                        <div class="panel-header">
                            <h3 class="panel-title">权限说明</h3>
                        </div>
                        <div class="permission-list">
                            <div class="permission-item">
                                <span class="perm-title">当前登录角色</span>
                                <span class="perm-content">派件网点</span>
                            </div>
                            <div class="permission-item">
                                <span class="perm-title">当前可发起</span>
                                <span class="perm-content">寄件网点、派件网点</span>
                            </div>
                            <div class="permission-item">
                                <span class="perm-title">当前可执行动作</span>
                                <span class="perm-content">审核通过 / 审核驳回</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 处理记录 -->
                    <div class="detail-panel">
                        <div class="panel-header">
                            <h3 class="panel-title">处理记录</h3>
                        </div>
                        <div class="record-timeline">
                            <div class="record-entry">
                                <span class="record-time">2024-03-01 14:30</span>
                                <div class="record-detail">
                                    <div class="record-person">寄件网点 张三</div>
                                    <div class="record-action">发起协商派送</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 底部操作栏 -->
            <div class="detail-footer-bar">
                <div class="footer-tip">
                    统一规范说明：● 表示必，红色框定展示范围和权限，便于快速查看邮件。
                </div>
                <div class="footer-action-btns">
                    <button class="detail-action-btn detail-btn-cancel" onclick="closeDetailModal()">审核驳回</button>
                    <button class="detail-action-btn detail-btn-confirm" onclick="closeDetailModal()">审核通过</button>
                </div>
            </div>
        </div>
    </div>
    
    <!-- 上报拦截件弹窗 -->
    <div class="modal-overlay" id="reportModal">'''

content = content.replace(old_report, new_html)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('HTML 已添加')
