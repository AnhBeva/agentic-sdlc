#!/usr/bin/env python3
import os
import sys
import json
import re

CATEGORIES = {
    '.': 'Core Guides',
    'docs': 'Detailed Chapters',
    'checklists': 'Verification Checklists',
    'templates': 'Operational Templates',
    'examples': 'Practical Examples'
}

def extract_title(content, filepath):
    # First look for a leading # header
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h1_match:
        title = h1_match.group(1).strip()
        # Strip markdown formatting
        title = re.sub(r'[\*\_`]', '', title)
        return title
    
    # Fallback to title field in front matter
    fm_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
    if fm_match:
        return fm_match.group(1).strip()
        
    # Fallback to formatted filename
    basename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(basename)[0]
    return name_without_ext.replace('_', ' ').replace('-', ' ').title()

def get_doc_id(rel_path):
    # Convert backslashes to forward slashes, lowercase, strip extension
    clean = rel_path.lower().replace('\\', '/').replace('.md', '')
    # Allow alphanumeric characters, hyphens, underscores, and forward slashes. Turn everything else to hyphen.
    clean = re.sub(r'[^a-z0-9\-_/]', '-', clean)
    # Replace slashes with hyphens to make valid URL hashes without paths
    clean = clean.replace('/', '-')
    return clean

def main():
    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    docs_list = []
    path_map = {}

    print("Scanning for markdown files...")

    # Recursively find all markdown files
    for root, dirs, files in os.walk(workspace_dir):
        # Exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if not file.endswith('.md'):
                continue
                
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, workspace_dir)
            
            # Skip unwanted directories
            if 'node_modules' in rel_path or '.gemini' in rel_path:
                continue

            parts = rel_path.split(os.sep)
            parent = parts[0] if len(parts) > 1 else '.'
            
            # Map directory structure to category
            if parent in CATEGORIES:
                category = CATEGORIES[parent]
            elif len(parts) > 2 and parts[0] == 'templates':
                category = 'Operational Templates'
            elif len(parts) > 2 and parts[0] == 'examples':
                category = 'Practical Examples'
            else:
                category = 'Core Guides'

            # Parse subcategory if nested
            subcategory = None
            if len(parts) > 2:
                sub_raw = parts[1]
                # Format subcategory neatly
                subcategory = sub_raw.replace('_', ' ').replace('-', ' ').title()

            with open(abs_path, 'r', encoding='utf-8') as f:
                content = f.read()

            title = extract_title(content, rel_path)
            doc_id = get_doc_id(rel_path)

            # Map the exact relative path and the filename basename to the doc_id
            normalized_rel_path = rel_path.replace('\\', '/')
            path_map[normalized_rel_path] = doc_id
            path_map[os.path.basename(rel_path)] = doc_id

            docs_list.append({
                'id': doc_id,
                'category': category,
                'subcategory': subcategory,
                'title': title,
                'path': normalized_rel_path,
                'content': content
            })

    # Strict Quality Check: Assert exactly 51 Markdown files
    expected_count = 51
    found_count = len(docs_list)
    if found_count != expected_count:
        print(f"❌ QUALITY FAILURE: Expected exactly {expected_count} markdown files, but found {found_count}!")
        print("Please check the project directory and DOCUMENTATION_MAP.md layout.")
        sys.exit(1)
    
    print(f"✅ Verified exactly {found_count} markdown files present.")

    # Sort documents by category order then by path
    category_order = {
        'Core Guides': 1,
        'Detailed Chapters': 2,
        'Verification Checklists': 3,
        'Operational Templates': 4,
        'Practical Examples': 5
    }

    def sort_key(doc):
        cat_order = category_order.get(doc['category'], 99)
        return (cat_order, doc['path'])

    docs_list.sort(key=sort_key)

    # Read template file
    template_path = os.path.join(workspace_dir, 'portal_template.html')
    if not os.path.exists(template_path):
        print(f"❌ ERROR: Template file {template_path} does not exist!")
        sys.exit(1)

    with open(template_path, 'r', encoding='utf-8') as f:
        html_template = f.read()

    # Serialize variables to JSON
    docs_json = json.dumps(docs_list, ensure_ascii=False, indent=2)
    path_map_json = json.dumps(path_map, ensure_ascii=False, indent=2)

    # Perform direct string substitution to avoid python f-string curly braces parser crashes
    output_html = html_template.replace('/* DOCS_DATABASE_PLACEHOLDER */', docs_json)
    output_html = output_html.replace('/* PATH_MAP_PLACEHOLDER */', path_map_json)

    # Save output index.html
    output_path = os.path.join(workspace_dir, 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_html)

    print(f"✅ Successfully compiled {found_count} files into HTML Portal: {output_path}")

if __name__ == '__main__':
    main()
