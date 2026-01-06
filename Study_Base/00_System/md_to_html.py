import re
import os
import sys

def convert_md_to_html(md_path, html_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Basic Markdown to HTML conversion
    html_content = md_content

    # Headers
    html_content = re.sub(r'^# (.*)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.*)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^### (.*)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)

    # Bold
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_content)

    # Links (Add target="_blank" for PDF links)
    def link_repl(match):
        text = match.group(1)
        url = match.group(2)
        if url.lower().endswith('.pdf'):
            return f'<a href="{url}" target="_blank" class="pdf-link">{text}</a>'
        return f'<a href="{url}">{text}</a>'
    
    html_content = re.sub(r'\[(.*?)\]\((.*?)\)', link_repl, html_content)

    # Lists
    lines = html_content.split('\n')
    new_lines = []
    in_list = False
    
    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                new_lines.append('<ul>')
                in_list = True
            content = line.strip()[2:]
            new_lines.append(f'<li>{content}</li>')
        else:
            if in_list:
                new_lines.append('</ul>')
                in_list = False
            new_lines.append(line)
    if in_list:
        new_lines.append('</ul>')
    
    html_content = '\n'.join(new_lines)

    # Line breaks for paragraphs (simple heuristic)
    # Wrap text lines that aren't tags in <p> ? 
    # Or just replace newlines with <br> for simple formatting?
    # Let's simple replace double newlines with <p> equivalent logic if needed, 
    # but for now, the headers and lists handle most structure.
    # We will wrap plain text blocks in <p>.
    
    # Actually, let's keep it simple. The current regex replacement leaves text floating.
    # We'll wrap lines that don't start with < in <p>.
    
    final_lines = []
    for line in html_content.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('<') and not line.startswith('<strong'): # strong can be start of line
             final_lines.append(line)
        elif line == '---':
            final_lines.append('<hr>')
        else:
             final_lines.append(f'<p>{line}</p>')

    body_content = '\n'.join(final_lines)

    # CSS Styles
    css = """
    <style>
        :root {
            --primary-color: #2563eb;
            --text-color: #1f2937;
            --bg-color: #f3f4f6;
            --card-bg: #ffffff;
            --link-color: #3b82f6;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Sans", "Noto Sans JP", "Yu Gothic", sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.75;
            margin: 0;
            padding: 20px;
            font-size: 16px;
            -webkit-text-size-adjust: 100%;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: var(--card-bg);
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        h1 {
            color: #111827;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 10px;
            margin-top: 0;
            font-size: 1.8rem;
        }
        h2 {
            color: #1e40af;
            margin-top: 40px;
            font-size: 1.5rem;
            border-left: 5px solid #3b82f6;
            padding-left: 15px;
            background: #eff6ff;
            padding-top: 5px;
            padding-bottom: 5px;
        }
        h3 {
            color: #374151;
            font-size: 1.25rem;
            margin-top: 30px;
            font-weight: 600;
        }
        a.pdf-link {
            display: inline-block;
            background-color: #edf5ff;
            color: var(--primary-color);
            padding: 4px 10px;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 500;
            transition: background-color 0.2s;
            font-size: 0.9em;
        }
        a.pdf-link:hover {
            background-color: #dbeafe;
            text-decoration: underline;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
        hr {
            border: 0;
            height: 1px;
            background: #e5e7eb;
            margin: 40px 0;
        }
        p {
            margin-bottom: 1.2em;
        }
        strong {
            color: #111827;
            background: linear-gradient(transparent 70%, #bfdbfe 70%);
        }

        /* Smartphone Optimization */
        @media (max-width: 600px) {
            body {
                padding: 0;
                font-size: 18px; /* Larger font for mobile */
                background-color: #fff;
            }
            .container {
                padding: 20px;
                border-radius: 0;
                box-shadow: none;
            }
            h1 {
                font-size: 1.6rem;
            }
            h2 {
                font-size: 1.4rem;
                margin-top: 30px;
            }
            h3 {
                font-size: 1.2rem;
            }
        }
    </style>
    """

    full_html = f"""
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>経済学特講 資料要約</title>
        {css}
    </head>
    <body>
        <div class="container">
            {body_content}
        </div>
    </body>
    </html>
    """

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Successfully converted {md_path} to {html_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python md_to_html.py <input_md> <output_html>")
        sys.exit(1)
    
    convert_md_to_html(sys.argv[1], sys.argv[2])
