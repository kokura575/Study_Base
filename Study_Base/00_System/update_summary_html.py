
import markdown
import os

# Paths
base_dir = r"c:\Users\rikus\onedrive.kokurahunter\OneDrive\antigravity\Study_Base\01_Active_Courses\Schooling\2025_Autumn\Public_Finance_B"
md_path = os.path.join(base_dir, "summary_narrative.md")
html_path = os.path.join(base_dir, "summary.html")

# CSS and HTML Template (based on existing summary.html)
html_template = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>財政学B 資料要約</title>
    
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
        font-size: 18px; /* PC default 18px */
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
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 20px auto;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    /* Smartphone Optimization */
    @media (max-width: 600px) {
        body {
            padding: 0;
            font-size: 22px; /* Mobile 22px */
            background-color: #fff;
        }
        .container {
            padding: 15px; /* Adjusted padding */
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

</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>
"""

def update_html():
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Pre-process markdown to handle specific link classes if needed
    # The original HTML had class="pdf-link" for PDF links.
    # We can try to replicate that using regex or just generate standard HTML.
    # Since I don't want to over-engineer the parser, I'll rely on basic markdown conversion.
    # Use python-markdown extensions for better compatibility
    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

    final_html = html_template.replace('{content}', html_content)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"Updated {html_path}")

if __name__ == "__main__":
    update_html()
