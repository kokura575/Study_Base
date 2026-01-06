import sys
import re

def read_section(dump_file, index):
    with open(dump_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by "## File: "
    # Note: The first split might be empty if the file starts with the delimiter or header
    sections = re.split(r'^## File: ', content, flags=re.MULTILINE)[1:] # Skip preamble

    if 0 <= index < len(sections):
        print(f"## File: {sections[index]}")
    else:
        print("INDEX_OUT_OF_RANGE")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python read_dump_section.py <dump_file> <index> <output_file>")
        sys.exit(1)
    
    dump_file = sys.argv[1]
    index = int(sys.argv[2])
    output_file = sys.argv[3]
    
    with open(dump_file, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = re.split(r'^## File: ', content, flags=re.MULTILINE)[1:] 

    if 0 <= index < len(sections):
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write(f"## File: {sections[index]}")
    else:
        print(f"INDEX_OUT_OF_RANGE: {index} (Total: {len(sections)})")
