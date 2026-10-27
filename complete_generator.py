# complete_generator.py
# Full-fledged site builder for Ashutosh Build Stone Pvt. Ltd. with expanded pages, SEO, GEO, and AEO.

import os
from build_ultimate_site import build_head
from generate_ultimate_multipage import (
    BASE_URL, COMPANY_NAME, CIN, PAN, TAN,
    PHONE_BHAGIRATH, PHONE_BHAGIRATH_RAW, PHONE_ALPESH, PHONE_ALPESH_RAW,
    ADDRESS, LATITUDE, LONGITUDE,
    get_global_schema, get_header_nav, get_geo_ai_factsheet, get_aeo_faq_component
)
from build_pages import FOOTER_HTML, get_page_banner

def generate_sitemap_and_robots():
    pages = [
        ("index.html", "1.0", "daily"),
        ("about.html", "0.9", "weekly"),
        ("products.html", "0.95", "weekly"),
        ("plant.html", "0.85", "weekly"),
        ("contracting.html", "0.9", "weekly"),
        ("calculator.html", "0.85", "monthly"),
        ("gallery.html", "0.8", "weekly"),
        ("contact.html", "0.9", "monthly"),
    ]
    
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    for page, priority, freq in pages:
        xml += f"""  <url>
    <loc>{BASE_URL}/{page}</loc>
    <lastmod>2026-10-27</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>
"""
    xml += "</urlset>\n"

    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml)
    print("sitemap.xml generated.")

    robots = f"""# Robots.txt for Ashutosh Build Stone Pvt. Ltd.
User-agent: *
Allow: /

# Dedicated AI and Generative Engine Crawlers
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write(robots)
    print("robots.txt generated.")

generate_sitemap_and_robots()
