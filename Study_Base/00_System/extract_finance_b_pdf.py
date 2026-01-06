
import os
import pypdf

# 対象ディレクトリ
TARGET_DIR = r"c:\Users\るけす\OneDrive\antigravity\Study_Base\01_Active_Courses\Schooling\25秋スク\財政学B"
OUTPUT_FILE = r"c:\Users\るけす\OneDrive\antigravity\Study_Base\00_System\finance_b_raw_text.txt"

def extract_text_from_pdf(pdf_path):
    text_content = []
    try:
        with open(pdf_path, 'rb') as f:
            reader = pypdf.PdfReader(f)
            # 全ページ読むと膨大になる可能性があるため、スライド資料なら全ページ、
            # 文書なら最初の数ページ等調整が必要だが、まずは全ページ取得を試みる。
            # ただし、文字数制限に引っかからないよう、各ページ冒頭1000文字程度にするか、
            # あるいは単純に全取得して後で切るか。
            # ここでは「全ページ」取得する。後でAIが読む際に調整する。
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    text_content.append(f"--- Page {i+1} ---\n{text}\n")
    except Exception as e:
        text_content.append(f"Error reading {pdf_path}: {e}")
    return "\n".join(text_content)

def main():
    if not os.path.exists(TARGET_DIR):
        print(f"Directory not found: {TARGET_DIR}")
        return

    all_texts = []
    
    # ファイル名でソートして処理
    files = sorted([f for f in os.listdir(TARGET_DIR) if f.lower().endswith(".pdf")])
    
    for filename in files:
        pdf_path = os.path.join(TARGET_DIR, filename)
        print(f"Processing: {filename}")
        
        extracted = extract_text_from_pdf(pdf_path)
        
        all_texts.append(f"■■■■■ FILE: {filename} ■■■■■\n")
        all_texts.append(extracted)
        all_texts.append("\n\n" + "="*50 + "\n\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("".join(all_texts))
    
    print(f"All extraction complete. Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
