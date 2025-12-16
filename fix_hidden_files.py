import glob
import os
import re

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if wrapped in comments
    if content.strip().startswith("<!--") and content.strip().endswith("-->"):
        # Remove the comments
        content = content.strip()[4:-3].strip()
        
        # Check if it has Front Matter
        if content.startswith("---"):
            # Find the end of Front Matter
            parts = content.split("---", 2)
            if len(parts) >= 3:
                front_matter = parts[1]
                body = parts[2]
                
                # Add published: false if not present
                if "published: false" not in front_matter:
                    front_matter = front_matter + "\npublished: false\n"
                
                new_content = "---" + front_matter + "---" + body
                
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"Fixed and hidden: {filepath}")
            else:
                print(f"Skipping {filepath}: Malformed Front Matter")
        else:
            print(f"Skipping {filepath}: No Front Matter found inside comments")
    else:
        print(f"Skipping {filepath}: Not wrapped in comments")

for f in glob.glob('_projects/*.md'):
    fix_file(f)
for f in glob.glob('_news/*.md'):
    fix_file(f)
