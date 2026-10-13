import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, "fonts")
TEMPLATE_PATH = os.path.join(BASE_DIR, "template.jpg")

def get_font(size, bold=True):
    font_filename = "segoeuib.ttf" if bold else "segoeui.ttf"
    bundled_font = os.path.join(FONTS_DIR, font_filename)
    if os.path.exists(bundled_font):
        return ImageFont.truetype(bundled_font, size)
    return ImageFont.load_default()

def render_trivia_card(body_text, source_text, output_path="rendered_trivia.jpg"):
    img = Image.open(TEMPLATE_PATH).convert("RGBA")
    draw = ImageDraw.Draw(img)
    W, H = img.size

    font_header = get_font(34, bold=True)
    font_body = get_font(24, bold=True)
    font_source = get_font(16, bold=True)

    header_text = "DID YOU KNOW?"
    blines = textwrap.wrap(body_text, width=29)
    slines = textwrap.wrap(source_text, width=38)

    # Vertical distribution
    header_h = 46
    gap_after_header = 34
    body_line_h = 37
    body_h = len(blines) * body_line_h
    gap_after_body = 36
    source_line_h = 24
    source_h = len(slines) * source_line_h

    total_h = header_h + gap_after_header + body_h + gap_after_body + source_h
    start_y = (H - total_h) // 2 - 15

    # 1. Header: DID YOU KNOW?
    hbbox = draw.textbbox((0, 0), header_text, font=font_header)
    hw = hbbox[2] - hbbox[0]
    draw.text(((W - hw) // 2, start_y), header_text, font=font_header, fill=(147, 197, 253))

    # Accent underline
    line_w = 90
    line_y = start_y + header_h + 8
    draw.line([((W - line_w) // 2, line_y), ((W + line_w) // 2, line_y)], fill=(147, 197, 253), width=3)

    # 2. Fact Body
    by = start_y + header_h + gap_after_header
    for line in blines:
        bbox = draw.textbbox((0, 0), line, font=font_body)
        w = bbox[2] - bbox[0]
        draw.text(((W - w) // 2, by), line, font=font_body, fill=(255, 255, 255))
        by += body_line_h

    # 3. Verified Source Footer
    sy = by + gap_after_body
    for line in slines:
        bbox = draw.textbbox((0, 0), line, font=font_source)
        w = bbox[2] - bbox[0]
        draw.text(((W - w) // 2, sy), line, font=font_source, fill=(191, 219, 254))
        sy += source_line_h

    img.convert("RGB").save(output_path, "JPEG", quality=95)
    return output_path
