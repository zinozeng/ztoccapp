#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取文件
with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 在关闭 modal 函数后添加 viewDetail 函数
old_close_modal = '''        // 关闭弹窗
        function closeModal(modalId) {
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.classList.remove('active');
            }
        }'''

new_close_modal = '''        // 关闭弹窗
        function closeModal(modalId) {
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.classList.remove('active');
            }
        }
        
        // 打开详情页
        function viewDetail(orderNo) {
            const modal = document.getElementById('detailModal');
            modal.classList.add('active');
        }'''

content = content.replace(old_close_modal, new_close_modal)

# 在上报拦截件弹窗之前添加详情页弹窗
old_report_modal = '''    <!-- 上报拦截件弹窗 -->
    <div class="modal-overlay" id="reportModal">'''

new_detail_modal = '''    <!-- 异常运单详情页弹窗 -->
    <div class="modal-overlay" id="detailModal" style="background: rgba(0, 0, 0, 0.45);">
        <div class="detail-modal">
            <!-- 详情页头部 -->
            <div class="detail-header">
                <div class="detail-header-left">
                    <h2 class="detail-title">异常运单详情</h2>
                    <div class="detail-info">
                        <span class="detail-info-item">运单编号：ZT20240301001</span>
                        <span class="detail-info-divider">|</span>
                        <span class="detail-info-item">异常类型：协商派送</span>
                        <span class="detail-info-divider">|</span>
                        <span class="detail-info-item">当前状态：已拦截</span>
                    </div>
                </div>
                <button class="detail-close" onclick="closeModal('detailModal')">&times;</button>
            </div>
            
            <!-- 详情页内容 -->
            <div class="detail-content">
                <!-- 左侧信息区 -->
                <div class="detail-left">
                    <!-- 运单基础信息 -->
                    <div class="detail-section">
                        <h3 class="detail-section-title">运单基础信息</h3>
                        <div class="detail-section-content">
                            <div class="info-row">
                                <div class="info-item">
                                    <span class="info-label">寄件人</span>
                                    <span class="info-value">王先生 / 138xxxx0001</span>
                                </div>
                                <div class="info-item">
                                    <span class="info-label">收件人</span>
                                    <span class="info-value">李先生 / 139xxxx0002</span>
                                </div>
                                <div class="info-item">
                                    <span class="info-label">货物信息</span>
                                    <span class="info-value">冷链样品 / 2 件 / 10KG</span>
                                </div>
                            </div>
                            <div class="info-row">
                                <div class="info-item">
                                    <span class="info-label">寄件地址</span>
                                    <span class="info-value">上海市浦东新区锦绣东路 1088 号</span>
                                </div>
                                <div class="info-item">
                                    <span class="info-label">收件地址</span>
                                    <span class="info-value">杭州市余杭区五常街道文一西路 969 号</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 异常信息 -->
                    <div class="detail-section">
                        <h3 class="detail-section-title">异常信息</h3>
                        <div class="detail-section-content">
                            <div class="info-row">
                                <div class="info-item">
                                    <span class="info-label">异常原因</span>
                                    <span class="info-value">客户临时变更派送要求</span>
                                </div>
                                <div class="info-item">
                                    <span class="info-label">期望处理方式</span>
                                    <span class="info-value">电话协商后再派送</span>
                                </div>
                            </div>
                            <div class="info-row">
                                <div class="info-item-full">
                                    <span class="info-label">异常情况说明</span>
                                    <span class="info-value">收件人要求更改派送时间，需派件网点先电话确认具体时间，再次投递前需安排当日送达。</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 审核处理区 -->
                    <div class="detail-section">
                        <h3 class="detail-section-title">审核处理区</h3>
                        <div class="detail-section-content">
                            <div class="audit-notice">
                                <span class="audit-notice-icon">●</span>
                                <span class="audit-notice-text">当前您是角色：派件网点，仅可审核，不可修改发起内容</span>
                            </div>
                            <div class="audit-opinion">
                                <label class="radio-label">
                                    <input type="radio" name="audit" checked> 审核通过
                                </label>
                                <label class="radio-label">
                                    <input type="radio" name="audit"> 审核驳回
                                </label>
                            </div>
                            <div class="audit-comment">
                                <span class="comment-label">审核意见：</span>
                                <span class="comment-text">建议先联系客户确认签收时间。</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- 右侧流程区 -->
                <div class="detail-right">
                    <!-- 流程状态 -->
                    <div class="detail-section">
                        <h3 class="detail-section-title">流程状态</h3>
                        <div class="process-timeline">
                            <div class="timeline-title">异常运单处理节点与当前执行动作</div>
                            <div class="timeline-steps">
                                <div class="timeline-step completed">
                                    <div class="step-dot"></div>
                                    <div class="step-content">
                                        <div class="step-title">寄件网点发起</div>
                                    </div>
                                </div>
                                <div class="timeline-line active"></div>
                                <div class="timeline-step current">
                                    <div class="step-dot"></div>
                                    <div class="step-content">
                                        <div class="step-title">派件网点审核</div>
                                    </div>
                                </div>
                                <div class="timeline-line"></div>
                                <div class="timeline-step">
                                    <div class="step-dot"></div>
                                    <div class="step-content">
                                        <div class="step-title">寄件网点处理</div>
                                    </div>
                                </div>
                            </div>
                            <div class="current-node">
                                <div class="current-node-title">当前节点</div>
                                <div class="current-node-content">
                                    <strong>派件网点审核</strong>
                                    <p>寄件网点发起协商网点可发起：改件网点审核通过或驳回后，流转至寄件网点处理结果。</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 权限说明 -->
                    <div class="detail-section">
                        <h3 class="detail-section-title">权限说明</h3>
                        <div class="permission-list">
                            <div class="permission-item">
                                <span class="permission-label">当前登录角色</span>
                                <span class="permission-value">派件网点</span>
                            </div>
                            <div class="permission-item">
                                <span class="permission-label">当前可发起</span>
                                <span class="permission-value">寄件网点、派件网点</span>
                            </div>
                            <div class="permission-item">
                                <span class="permission-label">当前可执行动作</span>
                                <span class="permission-value">审核通过 / 审核驳回</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 处理记录 -->
                    <div class="detail-section">
                        <h3 class="detail-section-title">处理记录</h3>
                        <div class="process-record">
                            <div class="record-item">
                                <div class="record-time">2024-03-01 14:30</div>
                                <div class="record-content">
                                    <span class="record-user">寄件网点 张三</span>
                                    <span class="record-action">发起协商派送</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 详情页底部 -->
            <div class="detail-footer">
                <div class="footer-tip">
                    <span>统一规范说明：● 表示必，红色框定展示范围和权限，便于快速查看邮件。</span>
                </div>
                <div class="footer-actions">
                    <button class="detail-btn detail-btn-default" onclick="closeModal('detailModal')">审核驳回</button>
                    <button class="detail-btn detail-btn-primary" onclick="closeModal('detailModal')">审核通过</button>
                </div>
            </div>
        </div>
    </div>
    
    <!-- 上报拦截件弹窗 -->
    <div class="modal-overlay" id="reportModal">'''

content = content.replace(old_report_modal, new_detail_modal)

# 添加详情页的 CSS 样式
old_css_end = '''        .modal-footer {'

new_css = '''        /* 详情页弹窗样式 */
        .detail-modal {
            background: #f5f7fa;
            border-radius: 8px;
            width: 1200px;
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
        }
        
        .detail-header {
            background: linear-gradient(135deg, #005f6b 0%, #008c8c 100%);
            color: white;
            padding: 20px 24px;
            border-radius: 8px 8px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .detail-header-left {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        
        .detail-title {
            font-size: 20px;
            font-weight: 600;
            margin: 0;
        }
        
        .detail-info {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 13px;
            opacity: 0.9;
        }
        
        .detail-info-divider {
            color: rgba(255, 255, 255, 0.5);
        }
        
        .detail-close {
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }
        
        .detail-close:hover {
            background: rgba(255, 255, 255, 0.3);
        }
        
        .detail-content {
            display: grid;
            grid-template-columns: 1fr 400px;
            gap: 16px;
            padding: 16px;
            flex: 1;
            overflow-y: auto;
        }
        
        .detail-left {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        
        .detail-right {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        
        .detail-section {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        }
        
        .detail-section-title {
            font-size: 16px;
            font-weight: 600;
            color: #005f6b;
            margin: 0 0 16px 0;
            padding-bottom: 12px;
            border-bottom: 1px solid #e8f0f0;
        }
        
        .detail-section-content {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .info-row {
            display: flex;
            gap: 24px;
        }
        
        .info-item {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        
        .info-item-full {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        
        .info-label {
            font-size: 13px;
            color: #8b9bb4;
            font-weight: 500;
        }
        
        .info-value {
            font-size: 14px;
            color: #333;
            line-height: 1.6;
        }
        
        .audit-notice {
            background: #fff7e6;
            border: 1px solid #ffd591;
            border-radius: 4px;
            padding: 12px 16px;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 16px;
        }
        
        .audit-notice-icon {
            color: #fa8c16;
            font-size: 16px;
        }
        
        .audit-notice-text {
            font-size: 14px;
            color: #666;
        }
        
        .audit-opinion {
            display: flex;
            gap: 24px;
            margin-bottom: 16px;
        }
        
        .radio-label {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
            color: #333;
            cursor: pointer;
        }
        
        .audit-comment {
            background: #f5f7fa;
            border-radius: 4px;
            padding: 12px 16px;
        }
        
        .comment-label {
            font-size: 13px;
            color: #8b9bb4;
            font-weight: 500;
        }
        
        .comment-text {
            font-size: 14px;
            color: #333;
            margin-left: 8px;
        }
        
        /* 流程时间轴 */
        .process-timeline {
            padding: 10px 0;
        }
        
        .timeline-title {
            font-size: 13px;
            color: #8b9bb4;
            margin-bottom: 20px;
        }
        
        .timeline-steps {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .timeline-step {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
        }
        
        .step-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #d9d9d9;
            border: 2px solid white;
            box-shadow: 0 0 0 2px #d9d9d9;
        }
        
        .timeline-step.completed .step-dot {
            background: #008c8c;
            box-shadow: 0 0 0 2px #008c8c;
        }
        
        .timeline-step.current .step-dot {
            background: #008c8c;
            box-shadow: 0 0 0 2px #008c8c;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% {
                box-shadow: 0 0 0 0 rgba(0, 140, 140, 0.4);
            }
            50% {
                box-shadow: 0 0 0 8px rgba(0, 140, 140, 0);
            }
        }
        
        .step-content {
            text-align: center;
        }
        
        .step-title {
            font-size: 13px;
            color: #333;
            white-space: nowrap;
        }
        
        .timeline-step.completed .step-title {
            color: #008c8c;
            font-weight: 500;
        }
        
        .timeline-step.current .step-title {
            color: #008c8c;
            font-weight: 600;
        }
        
        .timeline-line {
            width: 60px;
            height: 2px;
            background: #d9d9d9;
            margin-top: -18px;
        }
        
        .timeline-line.active {
            background: #008c8c;
        }
        
        .current-node {
            margin-top: 20px;
            background: #fff7e6;
            border: 1px solid #ffd591;
            border-radius: 4px;
            padding: 16px;
        }
        
        .current-node-title {
            font-size: 13px;
            color: #8b9bb4;
            margin-bottom: 8px;
        }
        
        .current-node-content {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        
        .current-node-content strong {
            font-size: 14px;
            color: #333;
        }
        
        .current-node-content p {
            font-size: 13px;
            color: #666;
            margin: 0;
            line-height: 1.5;
        }
        
        /* 权限说明 */
        .permission-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .permission-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 0;
            border-bottom: 1px solid #f0f0f0;
        }
        
        .permission-item:last-child {
            border-bottom: none;
        }
        
        .permission-label {
            font-size: 13px;
            color: #8b9bb4;
        }
        
        .permission-value {
            font-size: 14px;
            color: #333;
        }
        
        /* 处理记录 */
        .process-record {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .record-item {
            display: flex;
            gap: 12px;
            align-items: flex-start;
        }
        
        .record-time {
            font-size: 13px;
            color: #8b9bb4;
            min-width: 140px;
        }
        
        .record-content {
            display: flex;
            gap: 12px;
            align-items: center;
        }
        
        .record-user {
            font-size: 14px;
            color: #333;
            font-weight: 500;
        }
        
        .record-action {
            font-size: 14px;
            color: #008c8c;
        }
        
        /* 详情页底部 */
        .detail-footer {
            background: white;
            border-radius: 0 0 8px 8px;
            padding: 16px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #e8f0f0;
        }
        
        .footer-tip {
            font-size: 13px;
            color: #8b9bb4;
        }
        
        .footer-actions {
            display: flex;
            gap: 12px;
        }
        
        .detail-btn {
            padding: 10px 24px;
            border-radius: 4px;
            font-size: 14px;
            cursor: pointer;
            border: 1px solid #d9d9d9;
            background: white;
            transition: all 0.3s;
        }
        
        .detail-btn-default {
            color: #666;
        }
        
        .detail-btn-default:hover {
            border-color: #008c8c;
            color: #008c8c;
        }
        
        .detail-btn-primary {
            background: linear-gradient(135deg, #008c8c 0%, #005f6b 100%);
            color: white;
            border: none;
        }
        
        .detail-btn-primary:hover {
            opacity: 0.9;
            transform: translateY(-1px);
        }
        
        .modal-footer {'''

content = content.replace(old_css_end, new_css)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('已添加详情页弹窗')
