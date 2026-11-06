# render_corporate_banner.py
import os
from PIL import Image, ImageDraw, ImageFont

def draw_star(draw, x, y, r, fill):
    import math
    points = []
    for i in range(10):
        angle = i * math.pi / 5 - math.pi / 2
        radius = r if i % 2 == 0 else r * 0.45
        points.append((x + radius * math.cos(angle), y + radius * math.sin(angle)))
    draw.polygon(points, fill=fill)

def create_corporate_banner():
    # 2x supersampling for razor-sharp antialiasing
    # Final target: 2400 x 480
    W, H = 4800, 960
    img = Image.new("RGBA", (W, H), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Fonts
    font_bold_path = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg_path = "assets/fonts/PlusJakartaSans.ttf"
    
    font_top_bar = ImageFont.truetype(font_reg_path, 34)
    font_top_bar_bold = ImageFont.truetype(font_bold_path, 36)
    font_brand_title = ImageFont.truetype(font_bold_path, 175)
    font_pvt_ltd = ImageFont.truetype(font_bold_path, 60)
    font_tagline = ImageFont.truetype(font_bold_path, 48)
    font_sub_tagline = ImageFont.truetype(font_reg_path, 38)
    font_spec_badge_title = ImageFont.truetype(font_bold_path, 32)
    font_spec_badge_val = ImageFont.truetype(font_bold_path, 100)
    font_spec_badge_sub = ImageFont.truetype(font_bold_path, 34)
    font_bottom_label = ImageFont.truetype(font_bold_path, 30)
    font_bottom_val = ImageFont.truetype(font_bold_path, 42)
    font_bottom_address = ImageFont.truetype(font_reg_path, 34)

    # Corporate Palette
    NAVY_DARK = (7, 16, 30, 255)       # #07101e
    NAVY_BRAND = (11, 25, 44, 255)     # #0b192c
    NAVY_BLUE = (30, 62, 98, 255)      # #1e3e62
    AMBER_GOLD = (245, 158, 11, 255)   # #f59e0b
    WHITE = (255, 255, 255, 255)
    LIGHT_BG = (248, 250, 252, 255)    # #f8fafc
    SLATE_TEXT = (71, 85, 105, 255)    # #475569
    SLATE_MUTED = (148, 163, 184, 255) # #94a3b8
    BORDER_COLOR = (203, 213, 225, 255)# #cbd5e1

    # 1. Background Fill
    draw.rectangle([0, 0, W, H], fill=WHITE)

    # 2. TOP ACCREDITATION & REGISTRATION BAR (0 to 130)
    draw.rectangle([0, 0, W, 130], fill=NAVY_DARK)
    draw.line([0, 130, W, 130], fill=AMBER_GOLD, width=8)

    # Gold Star
    draw_star(draw, 110, 68, 18, AMBER_GOLD)

    # Top Bar Text Elements
    draw.text((145, 46), "GOVT. APPROVED BUILDING CONTRACTOR", fill=AMBER_GOLD, font=font_top_bar_bold)
    draw.text((1200, 48), "CIN: U43299GJ2025PTC159486", fill=WHITE, font=font_top_bar_bold)
    draw.text((1920, 48), "|", fill=NAVY_BLUE, font=font_top_bar_bold)

    draw.text((2000, 46), "GSTIN: 24ABCCA2752K1ZS", fill=AMBER_GOLD, font=font_top_bar_bold)
    draw.text((2720, 48), "|", fill=NAVY_BLUE, font=font_top_bar_bold)

    draw.text((2800, 48), "PAN: ABCCA2752K   •   TAN: AHMA32297G", fill=WHITE, font=font_top_bar_bold)
    draw.text((3700, 48), "|", fill=NAVY_BLUE, font=font_top_bar_bold)

    draw.text((3780, 48), "IS 383:2016 CERTIFIED QUALITY", fill=(147, 197, 253, 255), font=font_top_bar_bold)

    # 3. MIDDLE BRAND CORE (138 to 680)
    draw.rectangle([0, 138, W, 680], fill=LIGHT_BG)
    
    # Left corporate vertical color-bars
    draw.rectangle([0, 138, 30, 680], fill=NAVY_BRAND)
    draw.rectangle([30, 138, 48, 680], fill=AMBER_GOLD)

    # Place Logo
    logo_path = "assets/images/logo.png"
    if os.path.exists(logo_path):
        logo_img = Image.open(logo_path).convert("RGBA")
        logo_target_h = 420
        aspect = logo_img.width / logo_img.height
        logo_target_w = int(logo_target_h * aspect)
        logo_resized = logo_img.resize((logo_target_w, logo_target_h), Image.LANCZOS)
        
        card_x, card_y = 120, 190
        card_w, card_h = logo_target_w + 60, logo_target_h + 40
        draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=28, fill=WHITE, outline=BORDER_COLOR, width=4)
        img.paste(logo_resized, (card_x + 30, card_y + 20), logo_resized)
        brand_text_x = card_x + card_w + 70
    else:
        brand_text_x = 120

    # Main Brand Name: ASHUTOSH BUILD STONE
    title_y = 195
    draw.text((brand_text_x, title_y), "ASHUTOSH BUILD STONE", fill=NAVY_BRAND, font=font_brand_title, stroke_width=4, stroke_fill=NAVY_BRAND)

    # PVT. LTD. badge
    bbox = draw.textbbox((brand_text_x, title_y), "ASHUTOSH BUILD STONE", font=font_brand_title)
    pvt_badge_x = bbox[2] + 45
    pvt_badge_y = title_y + 40
    pvt_badge_w = 340
    pvt_badge_h = 100
    
    draw.rounded_rectangle([pvt_badge_x, pvt_badge_y, pvt_badge_x + pvt_badge_w, pvt_badge_y + pvt_badge_h], radius=20, fill=NAVY_BRAND, outline=AMBER_GOLD, width=5)
    draw.text((pvt_badge_x + 30, pvt_badge_y + 16), "PVT. LTD.", fill=AMBER_GOLD, font=font_pvt_ltd, stroke_width=2, stroke_fill=AMBER_GOLD)

    # Core Tagline
    tagline_y = title_y + 215
    draw.text((brand_text_x, tagline_y), "AGGREGATE   •   BLACK TRAP   •   WASHED M-SAND   •   PLASTER SAND   •   GSB   •   RMC", fill=NAVY_BLUE, font=font_tagline)

    # Secondary Tagline / Description
    sub_tag_y = tagline_y + 80
    draw.text((brand_text_x, sub_tag_y), "Govt. Approved Building Contractor  |  High-Capacity Commercial Aggregate & Sand Infrastructure", fill=SLATE_TEXT, font=font_sub_tagline)

    # Right Side: 250 TPH High-Capacity Badge Box
    badge_box_w = 880
    badge_box_h = 440
    badge_box_x = W - badge_box_w - 100
    badge_box_y = 190

    draw.rounded_rectangle([badge_box_x, badge_box_y, badge_box_x + badge_box_w, badge_box_y + badge_box_h], radius=28, fill=NAVY_BRAND, outline=AMBER_GOLD, width=6)
    
    draw.text((badge_box_x + 40, badge_box_y + 36), "PLANT PRODUCTION CAPACITY", fill=WHITE, font=font_spec_badge_title)
    draw.line([badge_box_x + 40, badge_box_y + 85, badge_box_x + badge_box_w - 40, badge_box_y + 85], fill=AMBER_GOLD, width=3)
    
    # 250 TPH Big Text
    draw.text((badge_box_x + 40, badge_box_y + 110), "250 TPH", fill=AMBER_GOLD, font=font_spec_badge_val, stroke_width=3, stroke_fill=AMBER_GOLD)
    draw.text((badge_box_x + 500, badge_box_y + 125), "TONS PER\nHOUR SETUP", fill=WHITE, font=font_spec_badge_sub)

    # Bottom sub-badge
    draw.rounded_rectangle([badge_box_x + 40, badge_box_y + 280, badge_box_x + badge_box_w - 40, badge_box_y + 380], radius=16, fill=NAVY_BLUE)
    draw.text((badge_box_x + 65, badge_box_y + 305), "HIGH OUTPUT: 2,500+ MT / DAY DISPATCH", fill=WHITE, font=font_top_bar_bold)

    # 4. BOTTOM CONTACT & LOCATION STRIP (680 to 960)
    draw.rectangle([0, 680, W, H], fill=NAVY_DARK)
    draw.line([0, 680, W, 680], fill=AMBER_GOLD, width=8)

    # Section 1: Contacts (Left)
    c_x1 = 100
    draw.text((c_x1, 715), "DIRECT PLANT & OPERATIONS DESK", fill=AMBER_GOLD, font=font_bottom_label)
    draw.text((c_x1, 765), "Mr. Bhagirath Sinh Sarviya: +91 78789 99033", fill=WHITE, font=font_bottom_val, stroke_width=1, stroke_fill=WHITE)
    draw.text((c_x1, 835), "Alpesh Chauhan (Sales & Billing): +91 76239 98398", fill=(226, 232, 240, 255), font=font_bottom_val, stroke_width=1, stroke_fill=(226, 232, 240, 255))

    # Divider line 1
    draw.line([1650, 710, 1650, 920], fill=NAVY_BLUE, width=4)

    # Section 2: Email Desk (Center)
    c_x2 = 1720
    draw.text((c_x2, 715), "OFFICIAL EMAIL COMMUNICATIONS", fill=AMBER_GOLD, font=font_bottom_label)
    draw.text((c_x2, 775), "ashutoshbuild@rediffmail.com", fill=WHITE, font=font_bottom_val, stroke_width=1, stroke_fill=WHITE)
    draw.text((c_x2, 845), "GSTIN: 24ABCCA2752K1ZS", fill=AMBER_GOLD, font=font_top_bar_bold)

    # Divider line 2
    draw.line([2700, 710, 2700, 920], fill=NAVY_BLUE, width=4)

    # Section 3: Registered Plant Address (Right)
    c_x3 = 2770
    draw.text((c_x3, 715), "MANUFACTURING PLANT & REGISTERED OFFICE LOCATION", fill=AMBER_GOLD, font=font_bottom_label)
    draw.text((c_x3, 770), "Gopnath Road, At. Borda, Tal. Talaja, Dist. Bhavnagar, Gujarat - 364130, India", fill=WHITE, font=font_bottom_address)
    draw.text((c_x3, 840), "Near Talaja (~12 km)  •  Near Alang Shipyard (~25 km)  •  Bhavnagar (~65 km)", fill=SLATE_MUTED, font=font_bottom_address)

    # Outer border around entire banner
    draw.rectangle([0, 0, W - 1, H - 1], outline=NAVY_BRAND, width=8)

    # Downsample with Lanczos for super-smooth vector-like anti-aliasing
    final_w, final_h = 2400, 480
    final_banner = img.resize((final_w, final_h), Image.LANCZOS)
    
    # Save as PNG and JPEG
    final_banner.save("assets/images/corporate-board-banner.png", "PNG", optimize=True)
    final_banner.convert("RGB").save("assets/images/company-banner.jpeg", "JPEG", quality=98)
    print("Perfect vector-clean corporate banner re-generated successfully!")

create_corporate_banner()
