#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('异常运单管理.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到错误的位置
old_marker = '''            </div>
        </div>
    </div>

        // 生成操作按钮'''

new_marker = '''            </div>
        </div>
    </div>

    <script>
        // 生成操作按钮'''

content = content.replace(old_marker, new_marker)

# 同时修复 closing script tag
old_close = '''        // 打开上报拦截件弹窗
        function openReportModal() {
            const modal = document.getElementById('reportModal');
            modal.classList.add('active');
        }
    </script>'''

new_close = '''        // 打开上报拦截件弹窗
        function openReportModal() {
            const modal = document.getElementById('reportModal');
            modal.classList.add('active');
        }
        </script>'''

content = content.replace(old_close, new_close)

with open('异常运单管理.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('已修复<script>标签')
