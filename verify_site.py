import os, re

files = [f for f in sorted(os.listdir('.')) if f.endswith(('.html', '.xml', '.txt'))]

print(f"{'FILENAME':20} | {'SIZE':10} | {'IMAGES':6} | {'SCHEMA':6} | {'AEO FAQS':8} | {'GEO BLOCK':9}")
print("-" * 75)

for f in files:
    if f.endswith('.html'):
        c = open(f, encoding='utf-8').read()
        imgs = set(re.findall(r'assets/images/[a-zA-Z0-9_\-\.]+', c))
        missing = [img for img in imgs if not os.path.exists(img)]
        has_schema = "application/ld+json" in c
        has_faq = 'id="faqs"' in c
        has_geo = "geo-factsheet" in c
        status = "OK" if not missing else f"MISSING {len(missing)}"
        print(f"{f:20} | {len(c):6} chars | {len(imgs):2} ({status}) | {'YES' if has_schema else 'NO':6} | {'YES' if has_faq else 'NO':8} | {'YES' if has_geo else 'NO':9}")
    else:
        print(f"{f:20} | {os.path.getsize(f):6} bytes | {'-':6} | {'-':6} | {'-':8} | {'-':9}")
