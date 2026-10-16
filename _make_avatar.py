from PIL import Image
from pathlib import Path
src = Path(r"C:\Users\Administrator\Documents\xwechat_files\hanzhengame_4686\temp\RWTemp\2026-10\9e20f478899dc29eb19741386f9343c8\bdc9833a82ef08a216e917b4b0672732.jpg")
out_dir = Path(r"D:\学习\一年级\images\profile")
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / "avatar.jpg"
img = Image.open(src).convert("RGB")
w, h = img.size
# 以脸部为中心裁切方形头像
cx, cy = w * 0.39, h * 0.28
size = min(w, h) * 0.34
left = max(0, cx - size / 2)
top = max(0, cy - size / 2)
right = min(w, left + size)
bottom = min(h, top + size)
left = max(0, right - size)
top = max(0, bottom - size)
img.crop((int(left), int(top), int(right), int(bottom))).save(out, quality=88)
print(out)
