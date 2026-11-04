"""index.html → publish/focus-diary.html (claude.ai 아티팩트용: 문서 뼈대 태그 제거)"""
import re, pathlib
root = pathlib.Path(__file__).parent
s = (root / 'index.html').read_text()
for pat in [r'<!doctype html>\s*', r'<html[^>]*>\s*', r'<head>\s*', r'<meta charset="utf-8">\s*',
            r'<meta name="viewport"[^>]*>\s*', r'</head>\s*', r'<body>\s*', r'</body>\s*', r'</html>\s*']:
    s = re.sub(pat, '', s, count=1, flags=re.I)
# 아티팩트 화면에서는 파일 내려받기가 막혀 있으므로 그 버튼만 뺌 (백업은 '백업 복사하기'로)
btn = '<button class="btn" data-act="export">파일로 내려받기</button>'
assert s.count(btn) == 1
s = s.replace(btn, '')
out = root / 'publish' / 'focus-diary.html'
out.parent.mkdir(exist_ok=True)
out.write_text(s)
print('wrote', out, len(s), 'bytes')
