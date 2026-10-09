# -*- coding: utf-8 -*-
"""HTML 内嵌 JS 语法校验（可复用）：提取 <script> 内容 -> node --check 校验。
用法: python _check_js.py <html路径>
返回 0 = 语法通过；非 0 = 有语法错误（含 node 不可用）。
"""
import io, re, subprocess, sys, tempfile, os

path = sys.argv[1] if len(sys.argv) > 1 else r'D:\学习\一年级\index.html'
s = io.open(path, encoding='utf-8').read()

if path.lower().endswith('.js'):
    # 纯 JS 数据文件：直接整体校验
    js = s
else:
    # HTML：提取所有 <script> ... </script>（忽略 src 外链的）
    blocks = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', s, re.S | re.I)
    if not blocks:
        print('NO_INLINE_SCRIPTS')
        sys.exit(1)
    js = '\n;\n'.join(blocks)
tmp = os.path.join(tempfile.gettempdir(), '_check_html_js.js')
io.open(tmp, 'w', encoding='utf-8', newline='').write(js)

r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True, encoding='utf-8')
if r.returncode == 0:
    print('JS_SYNTAX_OK')
    sys.exit(0)
else:
    print('JS_SYNTAX_ERROR:')
    print(r.stderr[:2000])
    sys.exit(1)
