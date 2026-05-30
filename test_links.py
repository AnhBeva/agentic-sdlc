#!/usr/bin/env python3
import os
import re
import urllib.parse

def github_slugify(text):
    slug = text.lower().strip()
    # Keep alphanumeric characters (unicode-aware), hyphens, underscores, and spaces
    # In regex: \w matches unicode letters/numbers/underscores when Unicode flag is enabled.
    slug = re.sub(r'[^\w\-\s]', '', slug, flags=re.UNICODE)
    slug = re.sub(r'\s+', '-', slug)
    return slug.strip('-')

def extract_headings(filepath):
    headings = set()
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match headers starting with #, ##, ###, etc.
    # Reject inline hashes by ensuring it's at start of line
    for line in content.split('\n'):
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            header_text = match.group(2).strip()
            # Strip trailing markdown formatting if any
            header_text = re.sub(r'[\*\_`]', '', header_text)
            slug = github_slugify(header_text)
            headings.add(slug)
    return headings

def test_markdown_links():
    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    all_files = []
    
    # 1. Gather all markdown files
    for root, dirs, files in os.walk(workspace_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.md'):
                all_files.append(os.path.join(root, file))
                
    print(f"Analyzing {len(all_files)} markdown files for link integrity...\n")

    broken_links_count = 0
    checked_links_count = 0

    # Cache headings for each file
    headings_cache = {}

    for filepath in all_files:
        rel_src = os.path.relpath(filepath, workspace_dir)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Match markdown links: [text](link)
        # Avoid matching image links, http, etc.
        links = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', content)
        
        for text, href in links:
            # Clean url-encoded items like %20
            href_decoded = urllib.parse.unquote(href)
            
            # Skip web URLs or email links or absolute local paths that aren't file:///
            if href_decoded.startswith(('http://', 'https://', 'mailto:', 'tel:')):
                continue
                
            checked_links_count += 1
            
            # Handle absolute file:/// links (convert to relative inside workspace)
            if href_decoded.startswith('file:///'):
                # Extract path after file:///
                # e.g., file:///Users/tuananh/.../Agentic%20SDLC/docs/01.md
                # We want to check if the target file is in the workspace
                local_path = href_decoded.replace('file:///', '/')
                # Check if the workspace path is inside this absolute path
                workspace_dir_slash = workspace_dir.replace('\\', '/')
                if workspace_dir_slash in local_path:
                    # Make it relative to workspace
                    href_decoded = local_path.split(workspace_dir_slash)[-1].lstrip('/')
                else:
                    print(f"❌ [{rel_src}] Absolute link goes outside workspace: {href}")
                    broken_links_count += 1
                    continue

            # Split path and anchor
            parts = href_decoded.split('#')
            link_path = parts[0].strip()
            link_anchor = parts[1].strip() if len(parts) > 1 else None
            
            # If the link path is empty, it refers to the same file
            if not link_path:
                target_filepath = filepath
            else:
                # Find target path relative to source file directory
                src_dir = os.path.dirname(filepath)
                target_filepath = os.path.normpath(os.path.join(src_dir, link_path))

            # Verify target file exists
            if not os.path.exists(target_filepath):
                print(f"❌ [{rel_src}] Broken Link: Target file does not exist -> \"{href}\"")
                broken_links_count += 1
                continue
                
            # Verify anchor if specified
            if link_anchor:
                # Get or cache target headings
                if target_filepath not in headings_cache:
                    headings_cache[target_filepath] = extract_headings(target_filepath)
                    
                target_headings = headings_cache[target_filepath]
                
                # Check if anchor matches any heading slug
                if link_anchor not in target_headings:
                    print(f"⚠️  [{rel_src}] Warning: Anchor #{link_anchor} not found in target file: {os.path.relpath(target_filepath, workspace_dir)}")
                    print(f"   Link: [{text}]({href})")
                    # List first few valid slugs for help
                    valid_slugs = list(target_headings)[:5]
                    print(f"   Valid anchors: {valid_slugs}...\n")
                    broken_links_count += 1

    print(f"Verification complete: checked {checked_links_count} internal links.")
    if broken_links_count > 0:
        print(f"❌ Found {broken_links_count} broken/warning link issues.")
        return False
    else:
        print("✅ All internal links and header anchors are 100% valid!")
        return True

if __name__ == '__main__':
    test_markdown_links()
