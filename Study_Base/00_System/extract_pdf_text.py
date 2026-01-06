import os
import argparse
import sys
from pypdf import PdfReader

# Force UTF-8 output to handle Unicode characters on Windows consoles
sys.stdout.reconfigure(encoding='utf-8')

def extract_text_from_pdfs(target_dir, output_file=None):
    """
    Extracts text from all PDF files in the target directory.
    Prints to stdout if output_file is None, otherwise writes to the file.
    """
    if not os.path.exists(target_dir):
        print(f"Error: Directory '{target_dir}' does not exist.")
        return

    pdf_files = [f for f in os.listdir(target_dir) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print(f"No PDF files found in '{target_dir}'.")
        return

    # Prepare output stream
    if output_file:
        f_out = open(output_file, 'w', encoding='utf-8')
    else:
        f_out = sys.stdout

    try:
        f_out.write(f"# Extracted Content from {target_dir}\n\n")

        for filename in pdf_files:
            file_path = os.path.join(target_dir, filename)
            f_out.write(f"## File: {filename}\n\n")
            try:
                reader = PdfReader(file_path)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                f_out.write(text)
                f_out.write("\n---\n\n")
            except Exception as e:
                f_out.write(f"Error reading {filename}: {e}\n\n")
    finally:
        if output_file:
            f_out.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from PDFs in a directory.")
    parser.add_argument("directory", help="The directory containing PDF files.")
    parser.add_argument("--output", help="Optional output file path.", default=None)
    args = parser.parse_args()
    
    extract_text_from_pdfs(args.directory, args.output)
