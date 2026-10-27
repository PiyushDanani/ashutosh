# build_ultimate_site.py
# Generates all 8 expanded pages + sitemap.xml + robots.txt for Ashutosh Build Stone Pvt. Ltd.

import os
from generate_ultimate_multipage import (
    BASE_URL, COMPANY_NAME, CIN, PAN, TAN,
    PHONE_BHAGIRATH, PHONE_BHAGIRATH_RAW, PHONE_ALPESH, PHONE_ALPESH_RAW,
    ADDRESS, LATITUDE, LONGITUDE,
    get_global_schema, get_header_nav, get_geo_ai_factsheet, get_aeo_faq_component
)
from build_pages import FOOTER_HTML

def write_html_file(filename, html_content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"[{filename}] generated successfully.")

# Head generator with full OpenGraph, Twitter Cards, Schema JSON-LD and SEO Meta
def build_head(title, description, keywords, canonical_url, schema_json):
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Ashutosh Build Stone Pvt. Ltd.</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="{COMPANY_NAME}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph / Facebook / WhatsApp Preview -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{title} | {COMPANY_NAME}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{BASE_URL}/assets/images/sand-washing-crusher-plant-hd.jpeg">
  <meta property="og:site_name" content="{COMPANY_NAME}">
  <meta property="og:locale" content="en_IN">

  <!-- Twitter Card Tags -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} | {COMPANY_NAME}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{BASE_URL}/assets/images/sand-washing-crusher-plant-hd.jpeg">

  <!-- Geo & Regional Meta Tags for Local SEO -->
  <meta name="geo.region" content="IN-GJ">
  <meta name="geo.placename" content="Borda, Talaja, Bhavnagar">
  <meta name="geo.position" content="{LATITUDE};{LONGITUDE}">
  <meta name="ICBM" content="{LATITUDE}, {LONGITUDE}">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Teko:wght@500;600;700&family=Noto+Sans+Devanagari:wght@600;700;800&display=swap" rel="stylesheet">

  <!-- Font Awesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              navy: '#0b192c',
              dark: '#07101e',
              deep: '#1e3e62',
              blue: '#0056b3',
              accent: '#f39c12',
              gold: '#e67e22',
              amber: '#ffb703',
              surface: '#f8fafc',
              border: '#e2e8f0',
              gray: '#64748b'
            }}
          }},
          fontFamily: {{
            outfit: ['Outfit', 'sans-serif'],
            teko: ['Teko', 'sans-serif'],
            hindi: ['Noto Sans Devanagari', 'Outfit', 'sans-serif']
          }}
        }}
      }}
    }}
  </script>

  <style>
    *, *::before, *::after {{
      box-sizing: border-box;
    }}
    html, body {{
      font-family: 'Outfit', sans-serif;
      background-color: #f8fafc;
      color: #1e293b;
      overflow-x: hidden !important;
      max-width: 100% !important;
      width: 100% !important;
      position: relative;
      touch-action: pan-y;
      -webkit-overflow-scrolling: touch;
    }}
    img, video, canvas, svg {{
      max-width: 100%;
      height: auto;
    }}
    .font-industrial {{
      font-family: 'Teko', sans-serif;
      letter-spacing: 0.05em;
    }}
    .font-hindi-motto {{
      font-family: 'Noto Sans Devanagari', sans-serif;
    }}
    .hero-gradient {{
      background: linear-gradient(135deg, rgba(7, 16, 30, 0.95) 0%, rgba(14, 34, 64, 0.88) 50%, rgba(7, 16, 30, 0.92) 100%);
    }}
    .card-hover {{
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .card-hover:hover {{
      transform: translateY(-6px);
      box-shadow: 0 20px 25px -5px rgba(11, 25, 44, 0.15), 0 8px 10px -6px rgba(11, 25, 44, 0.1);
    }}
    .pulse-call {{
      transition: transform 0.2s ease;
    }}
    ::-webkit-scrollbar {{
      width: 10px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0b192c;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #f59e0b;
      border-radius: 5px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #d97706;
    }}
  </style>

  <!-- Structured Data JSON-LD (Schema.org) -->
  <script type="application/ld+json">
{schema_json}
  </script>
</head>
<body class="antialiased">
"""

print("Base build helpers ready.")
