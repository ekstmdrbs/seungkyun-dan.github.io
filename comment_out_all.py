import os
import glob

def comment_out_body(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Find the second '---'
    dash_count = 0
    insert_idx = -1
    for i, line in enumerate(lines):
        if line.strip() == '---':
            dash_count += 1
            if dash_count == 2:
                insert_idx = i + 1
                break
    
    if insert_idx != -1:
        content_after = "".join(lines[insert_idx:]).strip()
        if content_after.startswith("<!--") and content_after.endswith("-->"):
            print(f"Already commented: {filepath}")
            return

        lines.insert(insert_idx, "\n<!--\n")
        lines.append("\n-->\n")
        
        with open(filepath, 'w') as f:
            f.writelines(lines)
        print(f"Commented out body of: {filepath}")

def comment_out_entire_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if content.strip().startswith("<!--") and content.strip().endswith("-->"):
        print(f"Already commented: {filepath}")
        return

    new_content = "<!--\n" + content + "\n-->"
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Commented out entire file: {filepath}")

def comment_out_lines(filepath, prefix):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        if not line.strip().startswith(prefix):
            new_lines.append(prefix + " " + line)
        else:
            new_lines.append(line)
            
    with open(filepath, 'w') as f:
        f.writelines(new_lines)
    print(f"Commented out lines in: {filepath}")

# 1. About page: Body only
comment_out_body('_pages/about.md')

# 2. Projects & News: Entire file (to hide from Jekyll collections)
for f in glob.glob('_projects/*.md'):
    comment_out_entire_file(f)
for f in glob.glob('_news/*.md'):
    comment_out_entire_file(f)

# 3. Data & Bib: Line comments
comment_out_lines('_data/cv.yml', '#')
comment_out_lines('_bibliography/papers.bib', '%')

