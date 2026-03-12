#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 删除旧的详情弹窗 HTML 和 CSS
import re

# 删除旧的 detail-modal CSS
css_pattern = r'/\* 详情页弹窗样式 \*/.*?\.modal-footer \{'
content = re.sub(css_pattern, '        .modal-footer {', content, flags=re.DOTALL)

# 删除旧的详情弹窗 HTML
html_pattern = r'    <!-- 异常运单详情页弹窗 -->.*?    <!-- 上报拦截件弹窗 -->'
content = re.sub(html_pattern, '    <!-- 上报拦截件弹窗 -->', content, flags=re.DOTALL)

# 添加新的详情弹窗 CSS
old_modal_footer = '''        .modal-footer {'''

new_detail_css = '''        /* 详情弹窗样式 */
        .detail-modal-overlay {
            background: rgba(0, 0, 0, 0.45);
            display: none;
        }
        
        .detail-modal-overlay.active {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .detail-modal {
            background: #f0f2f5;
            border-radius: 8px;
            width: 1180px;
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
        }
        
        .detail-header {
            background: linear-gradient(135deg, #005f6b 0%, #008c8c 100%);
            color: white;
            padding: 16px 24px;
            border-radius: 8px 8px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .detail-header-left {
            display: flex;
            flex-direction: column;
            gap: 8px;
            flex: 1;
        }
        
        .detail-title-row {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .detail-title {
            font-size: 18px;
            font-weight: 600;
            margin: 0;
        }
        
        .detail-tags {
            display: flex;
            gap: 8px;
        }
        
        .detail-tag {
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
            background: rgba(255, 255, 255, 0.2);
        }
        
        .detail-info {
            display: flex;
            align-items: center;
            gap: 16px;
            font-size: 13px;
            opacity: 0.9;
        }
        
        .detail-info-item {
            display: flex;
            align-items: center;
            gap: 4px;
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
            grid-template-columns: 1fr 380px;
            gap: 16px;
            padding: 16px;
            flex: 1;
            overflow-y: auto;
            min-height: 500px;
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
        
        .detail-card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        }
        
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid #e8f0f0;
        }
        
        .card-title {
            font-size: 15px;
            font-weight: 600;
            color: #005f6b;
            margin: 0;
        }
        
        .card-subtitle {
            font-size: 12px;
            color: #8b9bb4;
            margin-top: 4px;
        }
        
        .info-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px 24px;
        }
        
        .info-block {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        
        .info-block-full {
            grid-column: 1 / -1;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        
        .label {
            font-size: 13px;
            color: #8b9bb4;
            font-weight: 500;
        }
        
        .value {
            font-size: 14px;
            color: #333;
            line-height: 1.6;
        }
        
        .address-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
            margin-top: 8px;
        }
        
        .address-item {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        
        .alert-box {
            background: #fff7e6;
            border: 1px solid #ffd591;
            border-radius: 4px;
            padding: 12px 16px;
            display: flex;
            align-items: flex-start;
            gap: 10px;
            margin-bottom: 16px;
        }
        
        .alert-icon {
            color: #fa8c16;
            font-size: 16px;
            line-height: 1;
        }
        
        .alert-content {
            flex: 1;
        }
        
        .alert-text {
            font-size: 14px;
            color: #666;
            line-height: 1.5;
        }
        
        .audit-options {
            display: flex;
            gap: 24px;
            margin-bottom: 16px;
        }
        
        .radio-group {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 12px 16px;
            background: #f5f7fa;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .radio-group:hover {
            background: #e8f0f0;
        }
        
        .radio-group input[type="radio"] {
            margin: 0;
            cursor: pointer;
        }
        
        .radio-group label {
            font-size: 14px;
            color: #333;
            cursor: pointer;
            margin: 0;
        }
        
        .audit-comment-box {
            background: #f5f7fa;
            border-radius: 4px;
            padding: 12px 16px;
        }
        
        .comment-label {
            font-size: 13px;
            color: #8b9bb4;
            font-weight: 500;
            margin-bottom: 4px;
        }
        
        .comment-text {
            font-size: 14px;
            color: #333;
            line-height: 1.5;
        }
        
        /* 流程时间轴 */
        .process-section {
            padding: 10px 0;
        }
        
        .process-subtitle {
            font-size: 13px;
            color: #8b9bb4;
            margin-bottom: 20px;
        }
        
        .timeline {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 20px;
        }
        
        .timeline-node {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            min-width: 80px;
        }
        
        .node-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #d9d9d9;
            border: 2px solid white;
            box-shadow: 0 0 0 2px #d9d9d9;
            transition: all 0.3s;
        }
        
        .timeline-node.completed .node-dot {
            background: #008c8c;
            box-shadow: 0 0 0 2px #008c8c;
        }
        
        .timeline-node.current .node-dot {
            background: #008c8c;
            box-shadow: 0 0 0 2px #008c8c;
            animation: nodePulse 2s infinite;
        }
        
        @keyframes nodePulse {
            0%, 100% {
                box-shadow: 0 0 0 0 rgba(0, 140, 140, 0.4);
            }
            50% {
                box-shadow: 0 0 0 8px rgba(0, 140, 140, 0);
            }
        }
        
        .node-label {
            font-size: 13px;
            color: #333;
            text-align: center;
            white-space: nowrap;
        }
        
        .timeline-node.completed .node-label {
            color: #008c8c;
            font-weight: 500;
        }
        
        .timeline-node.current .node-label {
            color: #008c8c;
            font-weight: 600;
        }
        
        .timeline-connector {
            width: 50px;
            height: 2px;
            background: #d9d9d9;
            margin-top: -16px;
        }
        
        .timeline-connector.active {
            background: #008c8c;
        }
        
        .current-node-box {
            background: #fff7e6;
            border: 1px solid #ffd591;
            border-radius: 4px;
            padding: 16px;
        }
        
        .current-node-label {
            font-size: 13px;
            color: #8b9bb4;
            margin-bottom: 8px;
        }
        
        .current-node-title {
            font-size: 14px;
            font-weight: 600;
            color: #333;
            margin-bottom: 6px;
        }
        
        .current-node-desc {
            font-size: 13px;
            color: #666;
            line-height: 1.5;
            margin: 0;
        }
        
        /* 权限说明 */
        .permission-table {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .permission-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid #f0f0f0;
        }
        
        .permission-row:last-child {
            border-bottom: none;
        }
        
        .perm-label {
            font-size: 13px;
            color: #8b9bb4;
        }
        
        .perm-value {
            font-size: 14px;
            color: #333;
            text-align: right;
        }
        
        /* 处理记录 */
        .record-list {
            display: flex;
            flex-direction: column;
            gap: 16px;
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
            line-height: 1.5;
        }
        
        .record-content {
            flex: 1;
        }
        
        .record-user {
            font-size: 14px;
            color: #333;
            font-weight: 500;
            margin-bottom: 2px;
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
        
        .footer-note {
            font-size: 13px;
            color: #8b9bb4;
            line-height: 1.5;
        }
        
        .footer-buttons {
            display: flex;
            gap: 12px;
        }
        
        .detail-btn {
            padding: 10px 24px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s;
            border: 1px solid #d9d9d9;
        }
        
        .detail-btn-default {
            background: white;
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
            box-shadow: 0 4px 12px rgba(0, 140, 140, 0.3);
        }
        
        .modal-footer {'''

content = content.replace(old_modal_footer, new_detail_css)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('已更新详情弹窗 CSS')
