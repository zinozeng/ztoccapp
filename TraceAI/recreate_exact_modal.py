#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 删除旧的详情弹窗 CSS
css_pattern = r'/\* 详情弹窗样式 \*/.*?\.modal-footer \{'
content = re.sub(css_pattern, '        .modal-footer {', content, flags=re.DOTALL)

# 删除旧的详情弹窗 HTML
html_pattern = r'    <!-- 异常运单详情弹窗 -->.*?    <!-- 上报拦截件弹窗 -->'
content = re.sub(html_pattern, '    <!-- 上报拦截件弹窗 -->', content, flags=re.DOTALL)

# 添加新的 CSS（严格按照截图）
old_modal_footer = '''        .modal-footer {'''

new_css = '''        /* 详情弹窗 - 严格按截图设计 */
        .detail-modal-overlay {
            background: rgba(0, 0, 0, 0.45);
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 9999;
            align-items: center;
            justify-content: center;
        }
        
        .detail-modal-overlay.active {
            display: flex;
        }
        
        .detail-modal {
            background: #f5f7fa;
            border-radius: 12px;
            width: 1200px;
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
        }
        
        .detail-header {
            background: linear-gradient(135deg, #00606b 0%, #008c8c 100%);
            color: white;
            padding: 20px 24px;
            border-radius: 12px 12px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }
        
        .detail-header-left {
            flex: 1;
        }
        
        .detail-title {
            font-size: 20px;
            font-weight: 600;
            margin: 0 0 12px 0;
        }
        
        .detail-tags-row {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }
        
        .detail-tag {
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 12px;
            background: rgba(255, 255, 255, 0.15);
            color: white;
        }
        
        .detail-info-row {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 13px;
            opacity: 0.95;
            flex-wrap: wrap;
        }
        
        .detail-info-item {
            display: flex;
            align-items: center;
            gap: 4px;
        }
        
        .detail-close-btn {
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 22px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
            flex-shrink: 0;
        }
        
        .detail-close-btn:hover {
            background: rgba(255, 255, 255, 0.3);
        }
        
        .detail-body {
            display: grid;
            grid-template-columns: 1fr 360px;
            gap: 16px;
            padding: 20px;
            flex: 1;
            overflow-y: auto;
            min-height: 550px;
        }
        
        .detail-main {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        
        .detail-side {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        
        .detail-panel {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
        }
        
        .panel-header {
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid #e8f0f0;
        }
        
        .panel-title {
            font-size: 16px;
            font-weight: 600;
            color: #00606b;
            margin: 0 0 4px 0;
        }
        
        .panel-subtitle {
            font-size: 12px;
            color: #8b9bb4;
            margin: 0;
        }
        
        .info-section {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px 20px;
        }
        
        .info-field {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        
        .info-field-full {
            grid-column: 1 / -1;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        
        .field-label {
            font-size: 13px;
            color: #8b9bb4;
            font-weight: 500;
        }
        
        .field-value {
            font-size: 14px;
            color: #333;
            line-height: 1.6;
        }
        
        .address-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 8px;
        }
        
        .address-block {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        
        .notice-box {
            background: #fff7e6;
            border: 1px solid #ffd591;
            border-radius: 4px;
            padding: 12px 16px;
            display: flex;
            align-items: flex-start;
            gap: 10px;
            margin-bottom: 16px;
        }
        
        .notice-dot {
            color: #fa8c16;
            font-size: 16px;
            line-height: 1;
            font-weight: bold;
        }
        
        .notice-text {
            font-size: 14px;
            color: #666;
            line-height: 1.5;
        }
        
        .audit-options {
            display: flex;
            gap: 20px;
            margin-bottom: 16px;
        }
        
        .audit-option {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 10px 16px;
            background: #f5f7fa;
            border-radius: 4px;
            cursor: pointer;
        }
        
        .audit-option:hover {
            background: #e8f0f0;
        }
        
        .audit-option input[type="radio"] {
            margin: 0;
            cursor: pointer;
        }
        
        .audit-option label {
            font-size: 14px;
            color: #333;
            cursor: pointer;
            margin: 0;
        }
        
        .audit-comment {
            background: #f5f7fa;
            border-radius: 4px;
            padding: 12px 16px;
        }
        
        .comment-title {
            font-size: 13px;
            color: #8b9bb4;
            font-weight: 500;
            margin-bottom: 6px;
        }
        
        .comment-content {
            font-size: 14px;
            color: #333;
            line-height: 1.5;
        }
        
        /* 流程时间轴 - 严格按截图 */
        .process-block {
            padding: 8px 0;
        }
        
        .process-desc {
            font-size: 13px;
            color: #8b9bb4;
            margin-bottom: 24px;
            line-height: 1.5;
        }
        
        .process-steps {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 24px;
        }
        
        .process-step {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            min-width: 70px;
        }
        
        .step-circle {
            width: 14px;
            height: 14px;
            border-radius: 50%;
            background: #d9d9d9;
            border: 2px solid white;
            box-shadow: 0 0 0 2px #d9d9d9;
            transition: all 0.3s;
        }
        
        .process-step.completed .step-circle {
            background: #ff9c38;
            box-shadow: 0 0 0 2px #ff9c38;
        }
        
        .process-step.current .step-circle {
            background: #ff9c38;
            box-shadow: 0 0 0 2px #ff9c38;
            animation: stepPulse 2s infinite;
        }
        
        @keyframes stepPulse {
            0%, 100% {
                box-shadow: 0 0 0 0 rgba(255, 156, 56, 0.4);
            }
            50% {
                box-shadow: 0 0 0 8px rgba(255, 156, 56, 0);
            }
        }
        
        .step-text {
            font-size: 13px;
            color: #333;
            text-align: center;
            white-space: nowrap;
        }
        
        .process-step.completed .step-text {
            color: #ff9c38;
            font-weight: 500;
        }
        
        .process-step.current .step-text {
            color: #ff9c38;
            font-weight: 600;
        }
        
        .step-line {
            width: 50px;
            height: 2px;
            background: #d9d9d9;
            margin-top: -18px;
        }
        
        .step-line.active {
            background: #ff9c38;
        }
        
        .current-step-box {
            background: #fff7e6;
            border: 1px solid #ffd591;
            border-radius: 6px;
            padding: 16px;
        }
        
        .current-step-label {
            font-size: 13px;
            color: #8b9bb4;
            margin-bottom: 8px;
        }
        
        .current-step-title {
            font-size: 14px;
            font-weight: 600;
            color: #ff9c38;
            margin-bottom: 8px;
        }
        
        .current-step-desc {
            font-size: 13px;
            color: #666;
            line-height: 1.6;
            margin: 0;
        }
        
        /* 权限说明 */
        .permission-list {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }
        
        .permission-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid #f0f0f0;
        }
        
        .permission-item:last-child {
            border-bottom: none;
        }
        
        .perm-title {
            font-size: 13px;
            color: #8b9bb4;
        }
        
        .perm-content {
            font-size: 14px;
            color: #333;
            text-align: right;
        }
        
        /* 处理记录 */
        .record-timeline {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        
        .record-entry {
            display: flex;
            gap: 12px;
            align-items: flex-start;
        }
        
        .record-time {
            font-size: 13px;
            color: #8b9bb4;
            min-width: 140px;
            line-height: 1.5;
        }
        
        .record-detail {
            flex: 1;
        }
        
        .record-person {
            font-size: 14px;
            color: #333;
            font-weight: 500;
            margin-bottom: 3px;
        }
        
        .record-action {
            font-size: 14px;
            color: #008c8c;
        }
        
        /* 详情页底部 */
        .detail-footer-bar {
            background: white;
            border-radius: 0 0 12px 12px;
            padding: 16px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #e8f0f0;
        }
        
        .footer-tip {
            font-size: 13px;
            color: #8b9bb4;
            line-height: 1.5;
        }
        
        .footer-action-btns {
            display: flex;
            gap: 12px;
        }
        
        .detail-action-btn {
            padding: 10px 28px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s;
            border: 1px solid #d9d9d9;
        }
        
        .detail-btn-cancel {
            background: white;
            color: #666;
        }
        
        .detail-btn-cancel:hover {
            border-color: #008c8c;
            color: #008c8c;
        }
        
        .detail-btn-confirm {
            background: linear-gradient(135deg, #ff9c38 0%, #ff6b36 100%);
            color: white;
            border: none;
        }
        
        .detail-btn-confirm:hover {
            opacity: 0.9;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(255, 156, 56, 0.35);
        }
        
        .modal-footer {'''

content = content.replace(old_modal_footer, new_css)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('CSS 已更新')
