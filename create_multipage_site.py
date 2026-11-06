# create_multipage_site.py
import os
import build_pages

# 1. Update index.html
def update_index_page():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Ensure all navigation links point to the separate pages
    nav_replacements = [
        ('href="#about"', 'href="about.html"'),
        ('href="#products"', 'href="products.html"'),
        ('href="#plant"', 'href="plant.html"'),
        ('href="#contracting"', 'href="contracting.html"'),
        ('href="#calculator"', 'href="calculator.html"'),
        ('href="#gallery"', 'href="gallery.html"'),
        ('href="#contact"', 'href="contact.html"'),
    ]
    for old, new in nav_replacements:
        content = content.replace(old, new)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated with multipage navigation links.")

update_index_page()
