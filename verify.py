#!/usr/bin/env python3
"""Kiểm tra nhanh tính toàn vẹn của site tĩnh trước khi deploy."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(ROOT, "index.html")

errors = []

with open(HTML, encoding="utf-8") as f:
    html = f.read()

# 1. Mọi đường dẫn tương đối src/href (ngoài anchor #) phải trỏ tới file tồn tại
refs = re.findall(r'(?:src|href)\s*=\s*"([^"]+)"', html)
for ref in refs:
    if ref.startswith(("#", "http", "data:")):
        continue
    target = os.path.normpath(os.path.join(ROOT, ref))
    if not os.path.isfile(target):
        errors.append(f"Missing file referenced from index.html: {ref}")

# 2. CSS background url() phải tồn tại
css_path = os.path.join(ROOT, "css", "styles.css")
with open(css_path, encoding="utf-8") as f:
    css = f.read()
for url in re.findall(r'url\(["\']?(\.\./[^)"\']+)', css):
    target = os.path.normpath(os.path.join(os.path.dirname(css_path), url))
    if not os.path.isfile(target):
        errors.append(f"Missing file referenced from styles.css: {url}")

# 3. URL đăng ký phải khớp tuyệt đối với yêu cầu
expected = {
    "https://m.tiktok.shop/s/ALwOPFFNfQsc",
    "https://m.tiktok.shop/s/ALwOMifNfG1Q",
}
found = set(re.findall(r"https://m\.tiktok\.shop/s/[A-Za-z0-9]+", html))
if found != expected:
    errors.append(f"Registration URL mismatch. Expected {expected}, got {found}")

# 4. Hai nút mở tab mới an toàn
for gate in ("gate-1", "gate-2"):
    m = re.search(r'id="%s"([^>]*)' % gate, html)
    if not m or 'target="_blank"' not in m.group(1) or 'rel="noopener noreferrer"' not in m.group(1):
        errors.append(f"{gate} missing target=_blank or rel safety attribute")

# 5. Không còn từ khóa feature bị cấm
for banned in ("tra cứu", "Tra cứu", "TRA CỨU", "<input", "<form", "countdown"):
    if banned in html:
        errors.append(f"Forbidden content found: {banned}")

# 6. config.js cũng chứa đúng URL
cfg_path = os.path.join(ROOT, "js", "config.js")
with open(cfg_path, encoding="utf-8") as f:
    cfg = f.read()
for url in expected:
    if url not in cfg:
        errors.append(f"config.js missing URL: {url}")

# 7. Liệt kê cây thư mục
print("Project tree:")
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = sorted(d for d in dirnames if d != ".git")
    depth = dirpath.replace(ROOT, "").count(os.sep)
    indent = "  " * depth
    print(f"{indent}{os.path.basename(dirpath) or '.'}/")
    for name in sorted(filenames):
        size = os.path.getsize(os.path.join(dirpath, name))
        print(f"{indent}  {name} ({size:,} bytes)")

if errors:
    print("\n❌ VERIFICATION FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("\n✅ All checks passed: asset paths, registration URLs, safe-link attributes, and content rules.")
