# inspect_festive_parent.py
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="festive-modal"')
print("Surrounding 300 chars before festive-modal:")
print(text[pos-300:pos])
