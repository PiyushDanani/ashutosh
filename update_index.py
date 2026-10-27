with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<a href="#home" class="hover:text-amber-600 transition-colors py-1">Home</a>', '<a href="index.html" class="text-amber-500 font-black border-b-2 border-amber-500 py-1">Home</a>')
text = text.replace('<a href="#home" class="flex items-center gap-2.5', '<a href="index.html" class="flex items-center gap-2.5')
text = text.replace('<a href="#home" class="py-2 border-b border-slate-100 hover:text-amber-600" onclick="closeMobileMenu()">Home</a>', '<a href="index.html" class="py-2 border-b border-slate-100 text-amber-600 font-extrabold" onclick="closeMobileMenu()">Home</a>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("index.html updated successfully")
