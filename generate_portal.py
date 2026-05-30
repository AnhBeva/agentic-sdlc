#!/usr/bin/env python3
import os
import json
import re

# Categories mapping based on folders
CATEGORIES = {
    '.': 'Core Guides',
    'docs': 'Detailed Chapters',
    'checklists': 'Verification Checklists',
    'templates': 'Operational Templates',
    'examples': 'Practical Examples'
}

def extract_title(content, filepath):
    # Try to find first H1 title
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h1_match:
        return h1_match.group(1).strip()
    
    # Try frontmatter title if any
    fm_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
    if fm_match:
        return fm_match.group(1).strip()
        
    # Fallback to filename
    basename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(basename)[0]
    return name_without_ext.replace('_', ' ').replace('-', ' ').title()

def get_doc_id(rel_path):
    # Create a clean ID from the path
    clean = rel_path.lower().replace('\\', '/').replace('.md', '')
    clean = re.sub(r'[^a-z0-9\-_/]', '-', clean)
    clean = clean.replace('/', '-')
    return clean

def main():
    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    docs_list = []
    path_map = {}

    print("Scanning for markdown files...")

    # Traverse folders
    for root, dirs, files in os.walk(workspace_dir):
        # Skip git and hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if not file.endswith('.md'):
                continue
                
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, workspace_dir)
            
            # Skip temp or system files
            if 'node_modules' in rel_path or '.gemini' in rel_path:
                continue

            # Determine category based on folder depth/name
            parts = rel_path.split(os.sep)
            parent = parts[0] if len(parts) > 1 else '.'
            
            if parent in CATEGORIES:
                category = CATEGORIES[parent]
            elif len(parts) > 2 and parts[0] == 'templates':
                category = 'Operational Templates'
            elif len(parts) > 2 and parts[0] == 'examples':
                category = 'Practical Examples'
            else:
                category = 'Core Guides'

            # Subcategory extraction
            subcategory = None
            if len(parts) > 2:
                sub_raw = parts[1]
                subcategory = sub_raw.replace('_', ' ').replace('-', ' ').title()

            with open(abs_path, 'r', encoding='utf-8') as f:
                content = f.read()

            title = extract_title(content, rel_path)
            doc_id = get_doc_id(rel_path)

            # Map the original relative path to the resolved doc_id
            path_map[rel_path.replace('\\', '/')] = doc_id
            # Also map the basename for simple link fallback
            path_map[os.path.basename(rel_path)] = doc_id

            # Add document data
            docs_list.append({
                'id': doc_id,
                'category': category,
                'subcategory': subcategory,
                'title': title,
                'path': rel_path.replace('\\', '/'),
                'content': content
            })

    # Sort documents: Core Guides first, then Chapters, Checklists, Templates, Examples.
    # Inside Detailed Chapters, sort by filename (to respect 00-, 01- order)
    category_order = {
        'Core Guides': 1,
        'Detailed Chapters': 2,
        'Verification Checklists': 3,
        'Operational Templates': 4,
        'Practical Examples': 5
    }

    def sort_key(doc):
        cat_order = category_order.get(doc['category'], 99)
        # Inside detailed chapters, sorting by filename path will correctly sort 00, 01, etc.
        return (cat_order, doc['path'])

    docs_list.sort(key=sort_key)

    print(f"Found {len(docs_list)} documents.")

    # Write index.html with embedded data
    html_template = get_html_template(docs_list, path_map)
    output_path = os.path.join(workspace_dir, 'index.html')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
        
    print(f"Successfully generated HTML portal at: {output_path}")

def get_html_template(docs, path_map):
    # JSON-serialize the document list and the path mapping
    docs_json = json.dumps(docs, ensure_ascii=False, indent=2)
    path_map_json = json.dumps(path_map, ensure_ascii=False, indent=2)

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Agentic SDLC — Operating System Portal</title>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="Cổng thông tin quy trình Agentic SDLC - Cẩm nang thiết kế, vận hành, kiểm soát chất lượng và tự cải thiện cho AI Coding Agents và AI nghiệp vụ.">
  <meta name="keywords" content="Agentic SDLC, AI Agent, Software Development Life Cycle, Software Engineering, Observability, OWASP Agentic, DevOps, CI/CD">
  <meta name="author" content="AnhBeva">
  
  <!-- Fonts & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Markdown, Code Highlighting & Diagrams Libraries -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  
  <!-- Prism JS for beautiful Apple-style code highlighting -->
  <link href="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-core.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>

  <!-- Mermaid.js for flowcharts, diagrams -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.0/dist/mermaid.min.js"></script>

  <style>
    /* Design Tokens */
    :root {{
      --bg-main: #f5f5f7;
      --bg-card: #ffffff;
      --bg-sidebar: rgba(245, 245, 247, 0.85);
      --border-color: #e8e8ed;
      --text-primary: #1d1d1f;
      --text-secondary: #86868b;
      --text-body: #333336;
      --accent: #0066cc;
      --accent-hover: #0077ed;
      --accent-soft: #e8f2fc;
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.04);
      --shadow-md: 0 4px 20px rgba(0, 0, 0, 0.08);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
      --font-heading: 'Outfit', -apple-system, sans-serif;
      --font-body: 'Plus Jakarta Sans', -apple-system, sans-serif;
      --font-mono: 'Fira Code', monospace;
    }}

    /* CSS Reset */
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-body);
      background-color: var(--bg-main);
      color: var(--text-body);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}

    /* Main Layout */
    .app-container {{
      display: flex;
      height: 100vh;
      width: 100vw;
      overflow: hidden;
    }}

    /* Sidebar Styling */
    .sidebar {{
      width: 320px;
      background-color: var(--bg-card);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      height: 100%;
      flex-shrink: 0;
      z-index: 10;
      transition: var(--transition);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
    }}

    .sidebar-header {{
      padding: 24px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .logo-container {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .logo-icon {{
      width: 36px;
      height: 36px;
      border-radius: 10px;
      background: linear-gradient(135deg, #0066cc, #54a0ff);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      box-shadow: 0 4px 10px rgba(0, 102, 204, 0.3);
    }}

    .logo-title {{
      font-family: var(--font-heading);
      font-size: 18px;
      font-weight: 700;
      color: var(--text-primary);
      letter-spacing: -0.5px;
    }}

    .search-wrapper {{
      position: relative;
    }}

    .search-input {{
      width: 100%;
      padding: 10px 14px 10px 38px;
      background-color: var(--bg-main);
      border: 1px solid transparent;
      border-radius: var(--radius-sm);
      font-family: var(--font-body);
      font-size: 14px;
      color: var(--text-primary);
      transition: var(--transition);
    }}

    .search-input:focus {{
      outline: none;
      background-color: var(--bg-card);
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.15);
    }}

    .search-icon {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-secondary);
      pointer-events: none;
    }}

    /* Sidebar Nav List */
    .sidebar-nav {{
      flex: 1;
      overflow-y: auto;
      padding: 16px 12px;
    }}

    .nav-category {{
      margin-bottom: 24px;
    }}

    .category-title {{
      font-family: var(--font-heading);
      font-size: 11px;
      font-weight: 700;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 1px;
      padding-left: 12px;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .nav-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .nav-item-btn {{
      width: 100%;
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 12px;
      border: none;
      background: transparent;
      border-radius: var(--radius-sm);
      color: var(--text-body);
      font-family: var(--font-body);
      font-size: 13.5px;
      font-weight: 500;
      text-align: left;
      cursor: pointer;
      transition: var(--transition);
    }}

    .nav-item-btn:hover {{
      background-color: var(--bg-main);
      color: var(--text-primary);
    }}

    .nav-item-btn.active {{
      background-color: var(--accent-soft);
      color: var(--accent);
      font-weight: 600;
      position: relative;
    }}

    .nav-item-btn.active::before {{
      content: '';
      position: absolute;
      left: 0;
      top: 8px;
      bottom: 8px;
      width: 3px;
      background-color: var(--accent);
      border-radius: 0 4px 4px 0;
    }}

    .nav-icon {{
      color: var(--text-secondary);
      transition: var(--transition);
    }}

    .nav-item-btn.active .nav-icon {{
      color: var(--accent);
    }}

    /* Subcategory Hierarchical Tree Styling */
    .subcategory-wrapper {{
      margin-bottom: 2px;
    }}
    
    .nav-subcat-btn {{
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      border: none;
      background: transparent;
      border-radius: var(--radius-sm);
      color: var(--text-body);
      font-family: var(--font-body);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
      text-align: left;
    }}
    
    .nav-subcat-btn:hover {{
      background-color: var(--bg-main);
      color: var(--text-primary);
    }}
    
    .subcat-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 2px;
      margin-top: 2px;
      margin-bottom: 6px;
    }}
    
    .nav-item-btn.indent {{
      padding-left: 28px;
      font-size: 13px;
    }}
    
    .subcat-count {{
      font-size: 10px;
      background-color: var(--border-color);
      color: var(--text-secondary);
      padding: 1px 6px;
      border-radius: 10px;
      font-weight: 600;
    }}
    
    .nav-text {{
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      flex-grow: 1;
    }}

    /* Main Area Styling */
    .main-wrapper {{
      flex: 1;
      display: flex;
      flex-direction: column;
      height: 100%;
      background-color: var(--bg-card);
      overflow: hidden;
      position: relative;
    }}

    /* Top Bar Header */
    .topbar {{
      height: 64px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 32px;
      background-color: rgba(255, 255, 255, 0.8);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      z-index: 5;
    }}

    .topbar-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .menu-toggle-btn {{
      display: none;
      background: transparent;
      border: none;
      cursor: pointer;
      color: var(--text-primary);
    }}

    .breadcrumbs {{
      font-size: 13px;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .breadcrumb-sep {{
      color: #d2d2d7;
    }}

    .topbar-right {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .action-btn {{
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border: 1px solid var(--border-color);
      background-color: var(--bg-card);
      color: var(--text-body);
      border-radius: var(--radius-sm);
      font-family: var(--font-body);
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      transition: var(--transition);
    }}

    .action-btn:hover {{
      background-color: var(--bg-main);
      border-color: #d2d2d7;
      color: var(--text-primary);
    }}

    /* Document Layout */
    .document-layout {{
      display: flex;
      flex: 1;
      overflow: hidden;
      width: 100%;
    }}

    .content-container {{
      flex: 1;
      overflow-y: auto;
      padding: 48px 48px 80px 48px;
      scroll-behavior: smooth;
    }}

    .article-wrapper {{
      max-width: 780px;
      margin: 0 auto;
    }}

    /* Table of Contents */
    .toc-wrapper {{
      width: 260px;
      border-left: 1px solid var(--border-color);
      padding: 32px 24px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
      flex-shrink: 0;
    }}

    .toc-title {{
      font-family: var(--font-heading);
      font-size: 12px;
      font-weight: 700;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .toc-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .toc-link {{
      font-size: 13px;
      color: var(--text-body);
      text-decoration: none;
      transition: var(--transition);
      cursor: pointer;
      display: block;
      border-left: 2px solid transparent;
      padding-left: 10px;
    }}

    .toc-link:hover {{
      color: var(--accent);
    }}

    .toc-link.active {{
      color: var(--accent);
      font-weight: 600;
      border-left-color: var(--accent);
    }}

    .toc-link.indent-h3 {{
      padding-left: 20px;
    }}

    /* Styled Markdown Content styling (Apple style) */
    .markdown-body {{
      font-family: var(--font-body);
      font-size: 16px;
      color: var(--text-body);
      line-height: 1.7;
    }}

    .markdown-body h1 {{
      font-family: var(--font-heading);
      font-size: 32px;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 24px;
      letter-spacing: -0.8px;
      line-height: 1.25;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 12px;
    }}

    .markdown-body h2 {{
      font-family: var(--font-heading);
      font-size: 22px;
      font-weight: 600;
      color: var(--text-primary);
      margin-top: 40px;
      margin-bottom: 16px;
      letter-spacing: -0.4px;
      line-height: 1.3;
      border-bottom: 1px solid rgba(232, 232, 237, 0.5);
      padding-bottom: 8px;
    }}

    .markdown-body h3 {{
      font-family: var(--font-heading);
      font-size: 18px;
      font-weight: 600;
      color: var(--text-primary);
      margin-top: 24px;
      margin-bottom: 12px;
      line-height: 1.4;
    }}

    .markdown-body p {{
      margin-bottom: 20px;
    }}

    .markdown-body a {{
      color: var(--accent);
      text-decoration: none;
      font-weight: 500;
      border-bottom: 1px solid transparent;
      transition: var(--transition);
    }}

    .markdown-body a:hover {{
      border-bottom-color: var(--accent);
    }}

    /* Lists styling */
    .markdown-body ul, .markdown-body ol {{
      margin-bottom: 20px;
      padding-left: 24px;
    }}

    .markdown-body li {{
      margin-bottom: 8px;
    }}

    .markdown-body li > ul, .markdown-body li > ol {{
      margin-top: 8px;
      margin-bottom: 0;
    }}

    /* Beautiful checklists */
    .markdown-body ul li input[type="checkbox"] {{
      margin-right: 8px;
      accent-color: var(--accent);
      transform: scale(1.1);
      vertical-align: middle;
      position: relative;
      top: -1px;
    }}

    /* Blockquotes */
    .markdown-body blockquote {{
      border-left: 4px solid var(--accent);
      padding: 12px 20px;
      background-color: var(--bg-main);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin-bottom: 24px;
      color: var(--text-body);
      font-style: italic;
    }}

    /* Tables */
    .markdown-body table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 28px;
      font-size: 14px;
      box-shadow: var(--shadow-sm);
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-color);
    }}

    .markdown-body th, .markdown-body td {{
      padding: 12px 16px;
      text-align: left;
    }}

    .markdown-body th {{
      background-color: var(--bg-main);
      color: var(--text-primary);
      font-weight: 600;
      border-bottom: 2px solid var(--border-color);
    }}

    .markdown-body td {{
      border-bottom: 1px solid var(--border-color);
      background-color: var(--bg-card);
    }}

    .markdown-body tr:last-child td {{
      border-bottom: none;
    }}

    .markdown-body tr:nth-child(even) td {{
      background-color: #fafafc;
    }}

    /* Code Blocks */
    .markdown-body code {{
      font-family: var(--font-mono);
      font-size: 13.5px;
      background-color: var(--bg-main);
      padding: 3px 6px;
      border-radius: 4px;
      color: #bf3434;
    }}

    .markdown-body pre {{
      background-color: #1e1e24;
      padding: 18px;
      border-radius: var(--radius-md);
      overflow-x: auto;
      margin-bottom: 24px;
      border: 1px solid rgba(255, 255, 255, 0.05);
      position: relative;
    }}

    .markdown-body pre code {{
      background-color: transparent;
      padding: 0;
      color: #e5c07b;
      font-size: 13px;
    }}

    /* Custom Alerts (Github Alerts in Apple design) */
    .custom-alert {{
      margin-bottom: 24px;
      border-radius: var(--radius-md);
      padding: 16px 20px;
      border-left: 4px solid transparent;
      display: flex;
      flex-direction: column;
      gap: 6px;
      box-shadow: var(--shadow-sm);
    }}

    .custom-alert-header {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .custom-alert-title {{
      font-family: var(--font-heading);
      font-size: 14px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .custom-alert-content {{
      font-size: 14.5px;
      color: var(--text-body);
    }}

    .custom-alert-content p {{
      margin-bottom: 0 !important;
    }}

    .alert-note {{
      background-color: #f2f7fc;
      border-left-color: #0066cc;
    }}
    .alert-note .custom-alert-title, .alert-note i {{
      color: #0066cc;
    }}

    .alert-tip {{
      background-color: #f2faf3;
      border-left-color: #34c759;
    }}
    .alert-tip .custom-alert-title, .alert-tip i {{
      color: #34c759;
    }}

    .alert-important {{
      background-color: #fbf5fc;
      border-left-color: #af52de;
    }}
    .alert-important .custom-alert-title, .alert-important i {{
      color: #af52de;
    }}

    .alert-warning {{
      background-color: #fff9f2;
      border-left-color: #ff9500;
    }}
    .alert-warning .custom-alert-title, .alert-warning i {{
      color: #ff9500;
    }}

    .alert-caution {{
      background-color: #fff2f2;
      border-left-color: #ff3b30;
    }}
    .alert-caution .custom-alert-title, .alert-caution i {{
      color: #ff3b30;
    }}

    /* Copy Code Button */
    .copy-btn {{
      position: absolute;
      top: 10px;
      right: 10px;
      background: rgba(255, 255, 255, 0.08);
      border: none;
      color: #86868b;
      padding: 6px;
      border-radius: 6px;
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .copy-btn:hover {{
      background: rgba(255, 255, 255, 0.15);
      color: white;
    }}

    /* Mermaid Container */
    .mermaid-container {{
      background: white;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 24px;
      margin-bottom: 28px;
      display: flex;
      justify-content: center;
      overflow-x: auto;
      box-shadow: var(--shadow-sm);
    }}

    .mermaid {{
      width: 100%;
      text-align: center;
    }}

    /* Search Results View */
    .search-results-container {{
      display: none;
      flex-direction: column;
      gap: 20px;
    }}

    .search-result-item {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 20px;
      cursor: pointer;
      transition: var(--transition);
      box-shadow: var(--shadow-sm);
    }}

    .search-result-item:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: var(--accent);
    }}

    .search-result-title {{
      font-family: var(--font-heading);
      font-size: 16px;
      font-weight: 600;
      color: var(--accent);
      margin-bottom: 6px;
    }}

    .search-result-snippet {{
      font-size: 13.5px;
      color: var(--text-body);
      line-height: 1.5;
    }}

    .search-result-path {{
      font-size: 11px;
      color: var(--text-secondary);
      margin-top: 8px;
      display: inline-block;
      background-color: var(--bg-main);
      padding: 2px 6px;
      border-radius: 4px;
    }}

    .highlight {{
      background-color: rgba(255, 204, 0, 0.35);
      border-radius: 2px;
      padding: 0 2px;
    }}

    /* Responsive Styles */
    @media (max-width: 1024px) {{
      .toc-wrapper {{
        display: none;
      }}
    }}

    @media (max-width: 768px) {{
      .sidebar {{
        position: absolute;
        left: -320px;
        top: 0;
        bottom: 0;
      }}

      .sidebar.open {{
        left: 0;
      }}

      .menu-toggle-btn {{
        display: block;
      }}

      .content-container {{
        padding: 24px;
      }}
    }}

    /* Print styling */
    @media print {{
      .sidebar, .topbar, .toc-wrapper, .copy-btn, .action-btn {{
        display: none !important;
      }}
      .app-container {{
        height: auto;
        overflow: visible;
      }}
      .main-wrapper {{
        overflow: visible;
      }}
      .content-container {{
        overflow: visible;
        padding: 0;
      }}
      .article-wrapper {{
        max-width: 100%;
      }}
    }}
  </style>
</head>
<body>

  <div class="app-container">
    
    <!-- Sidebar -->
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <div class="logo-container">
          <div class="logo-icon">
            <i data-lucide="cpu" style="width: 20px; height: 20px;"></i>
          </div>
          <div class="logo-title">Agentic SDLC OS</div>
        </div>
        <div class="search-wrapper">
          <i data-lucide="search" class="search-icon" style="width: 16px; height: 16px;"></i>
          <input type="text" id="search-input" class="search-input" placeholder="Tìm kiếm tài liệu...">
        </div>
      </div>
      
      <nav class="sidebar-nav" id="sidebar-nav">
        <!-- Rendered dynamically -->
      </nav>
    </aside>

    <!-- Main Wrapper -->
    <div class="main-wrapper">
      
      <!-- Topbar Header -->
      <header class="topbar">
        <div class="topbar-left">
          <button class="menu-toggle-btn" id="menu-toggle">
            <i data-lucide="menu"></i>
          </button>
          <div class="breadcrumbs" id="breadcrumbs">
            <span>Core Guides</span>
            <span class="breadcrumb-sep">&gt;</span>
            <span style="color: var(--text-primary); font-weight: 500;">README.md</span>
          </div>
        </div>
        
        <div class="topbar-right">
          <button class="action-btn" onclick="window.print()">
            <i data-lucide="printer" style="width: 14px; height: 14px;"></i>
            In / Lưu PDF
          </button>
        </div>
      </header>

      <!-- Document Layout -->
      <div class="document-layout">
        
        <!-- Content Container -->
        <main class="content-container" id="content-container">
          <div class="article-wrapper">
            
            <!-- Standard Document Content -->
            <div id="document-content" class="markdown-body">
              <!-- Rendered dynamically -->
            </div>

            <!-- Search Results Display -->
            <div id="search-results" class="search-results-container">
              <h2 style="font-family: var(--font-heading); font-size: 24px; font-weight: 600; color: var(--text-primary); margin-bottom: 20px;">Kết quả tìm kiếm</h2>
              <div id="search-results-list" style="display: flex; flex-direction: column; gap: 16px;">
                <!-- Search matches go here -->
              </div>
            </div>

          </div>
        </main>

        <!-- Right Sidebar Table of Contents -->
        <aside class="toc-wrapper" id="toc-wrapper">
          <div class="toc-title">Mục lục trang</div>
          <ul class="toc-list" id="toc-list">
            <!-- Rendered dynamically -->
          </ul>
        </aside>

      </div>

    </div>

  </div>

  <!-- Document Data and Application Logic -->
  <script>
    // Embedded Document Database
    const docs = {docs_json};
    
    // Path mapping for markdown links conversion
    const pathMap = {path_map_json};

    // Initialize Lucide Icons
    lucide.createIcons();

    // Configure marked to intercept code blocks for mermaid and render icons/tables
    const renderer = new marked.Renderer();
    
    // Overriding code renderer to capture Mermaid syntax
    renderer.code = function(code, language, escaped) {{
      if (language === 'mermaid') {{
        return `<div class="mermaid-container"><div class="mermaid">${{code}}</div></div>`;
      }}
      
      // Escape HTML to prevent broken layouts inside pre/code
      const safeCode = code
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
      
      const copyBtn = `<button class="copy-btn" onclick="copyToClipboard(this)" title="Copy code"><i data-lucide="copy" style="width: 14px; height: 14px;"></i></button>`;
      
      return `<pre style="position: relative;">${{copyBtn}}<code class="language-${{language || 'text'}}">${{safeCode}}</code></pre>`;
    }};

    marked.setOptions({{
      renderer: renderer,
      gfm: true,
      breaks: true
    }});

    // Initialize Mermaid Configuration
    mermaid.initialize({{
      startOnLoad: false,
      theme: 'default',
      securityLevel: 'loose',
      flowchart: {{ useMaxWidth: true, htmlLabels: true }}
    }});

    // Global App States
    let currentDocId = "";
    
    // Icon Mapping for Sidebar Categories
    const categoryIcons = {{
      'Core Guides': 'book-open',
      'Detailed Chapters': 'file-text',
      'Verification Checklists': 'check-square',
      'Operational Templates': 'layout-template',
      'Practical Examples': 'code'
    }};

    // DOM Elements
    const sidebarNav = document.getElementById('sidebar-nav');
    const documentContent = document.getElementById('document-content');
    const searchResults = document.getElementById('search-results');
    const searchResultsList = document.getElementById('search-results-list');
    const searchInput = document.getElementById('search-input');
    const tocList = document.getElementById('toc-list');
    const breadcrumbs = document.getElementById('breadcrumbs');
    const sidebar = document.getElementById('sidebar');
    const menuToggle = document.getElementById('menu-toggle');

    // Clipboard copy helper
    function copyToClipboard(btn) {{
      const pre = btn.closest('pre');
      const code = pre.querySelector('code').innerText;
      navigator.clipboard.writeText(code).then(() => {{
        btn.innerHTML = `<i data-lucide="check" style="width: 14px; height: 14px; color: #34c759;"></i>`;
        lucide.createIcons();
        setTimeout(() => {{
          btn.innerHTML = `<i data-lucide="copy" style="width: 14px; height: 14px;"></i>`;
          lucide.createIcons();
        }}, 2000);
      }});
    }}

    // Helper to resolve relative path strings (e.g. docs/00-overview.md + ../Agentic_SDLC_Master_Map.md -> Agentic_SDLC_Master_Map.md)
    function resolveRelativePath(basePath, relativePath) {{
      if (relativePath.startsWith('http') || relativePath.startsWith('#')) {{
        return relativePath;
      }}
      
      const baseParts = basePath.split('/');
      baseParts.pop(); // remove filename
      
      const relParts = relativePath.split('/');
      
      for (const part of relParts) {{
        if (part === '.') {{
          continue;
        }} else if (part === '..') {{
          if (baseParts.length > 0) baseParts.pop();
        }} else {{
          baseParts.push(part);
        }}
      }}
      
      return baseParts.join('/');
    }}

    // Path normalization helper for links
    function resolveDocId(href) {{
      const currentDoc = docs.find(d => d.id === currentDocId);
      if (!currentDoc) return null;
      
      const resolvedPath = resolveRelativePath(currentDoc.path, href);
      if (pathMap[resolvedPath]) {{
        return pathMap[resolvedPath];
      }}
      
      let cleanPath = href.replace(/^(\\.\\.\\/|\\.\\/)+/, '');
      if (pathMap[cleanPath]) {{
        return pathMap[cleanPath];
      }}
      
      // Fallback: match by basename
      const base = cleanPath.split('/').pop();
      if (pathMap[base]) {{
        return pathMap[base];
      }}
      return null;
    }}

    // Search Diacritic remover
    function removeDiacritics(str) {{
      return str.normalize("NFD").replace(/[\\u0300-\\u036f]/g, "").toLowerCase();
    }}

    // Custom Alert Parser
    function parseAlerts(html) {{
      const alertClasses = {{
        'NOTE': 'alert-note',
        'TIP': 'alert-tip',
        'IMPORTANT': 'alert-important',
        'WARNING': 'alert-warning',
        'CAUTION': 'alert-caution'
      }};
      const alertTitles = {{
        'NOTE': 'Lưu ý',
        'TIP': 'Gợi ý',
        'IMPORTANT': 'Quan trọng',
        'WARNING': 'Cảnh báo',
        'CAUTION': 'Thận trọng'
      }};
      const alertIcons = {{
        'NOTE': '<i data-lucide="info" style="width: 16px; height: 16px; margin-right: 8px;"></i>',
        'TIP': '<i data-lucide="lightbulb" style="width: 16px; height: 16px; margin-right: 8px;"></i>',
        'IMPORTANT': '<i data-lucide="alert-circle" style="width: 16px; height: 16px; margin-right: 8px;"></i>',
        'WARNING': '<i data-lucide="alert-triangle" style="width: 16px; height: 16px; margin-right: 8px;"></i>',
        'CAUTION': '<i data-lucide="shield-alert" style="width: 16px; height: 16px; margin-right: 8px;"></i>'
      }};
      
      return html.replace(/<blockquote>\s*<p>\s*\\?\\?\[\!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(?:<br\s*\\/?>)?([\s\S]*?)<\/p>\s*<\/blockquote>/gi, (match, type, content) => {{
        type = type.toUpperCase();
        return `<div class="custom-alert ${{alertClasses[type]}}">
          <div class="custom-alert-header">
            ${{alertIcons[type]}}
            <span class="custom-alert-title">${{alertTitles[type]}}</span>
          </div>
          <div class="custom-alert-content">${{content}}</div>
        </div>`;
      }});
    }}

    // Toggle subcategory fold open/close
    function toggleSubcategory(subcatId) {{
      const list = document.getElementById(`list-${{subcatId}}`);
      const arrow = document.getElementById(`arrow-${{subcatId}}`);
      if (list.style.display === 'none') {{
        list.style.display = 'block';
        arrow.style.transform = 'rotate(90deg)';
      }} else {{
        list.style.display = 'none';
        arrow.style.transform = 'rotate(0deg)';
      }}
    }}

    // Expand subcategory of a document
    function expandSubcategoryOfDoc(docId) {{
      const doc = docs.find(d => d.id === docId);
      if (doc && doc.subcategory) {{
        const subcatId = `${{doc.category.toLowerCase().replace(/ /g, '-')}}-${{doc.subcategory.toLowerCase().replace(/ /g, '-')}}`;
        const list = document.getElementById(`list-${{subcatId}}`);
        const arrow = document.getElementById(`arrow-${{subcatId}}`);
        if (list && list.style.display === 'none') {{
          list.style.display = 'block';
          arrow.style.transform = 'rotate(90deg)';
        }}
      }}
    }}

    // Build sidebar navigation dynamically with tree hierarchy
    function renderSidebar() {{
      const categories = ['Core Guides', 'Detailed Chapters', 'Verification Checklists', 'Operational Templates', 'Practical Examples'];
      let navHtml = "";
      
      categories.forEach(category => {{
        const categoryDocs = docs.filter(doc => doc.category === category);
        if (categoryDocs.length === 0) return;
        
        const iconName = categoryIcons[category] || 'folder';
        
        navHtml += `
          <div class="nav-category">
            <div class="category-title">
              <span>${{category}}</span>
              <i data-lucide="${{iconName}}" style="width: 12px; height: 12px;"></i>
            </div>
            <ul class="nav-list">
        `;
        
        // Group category docs by subcategory
        const subcategories = {{}};
        const flatDocs = [];
        
        categoryDocs.forEach(doc => {{
          if (doc.subcategory) {{
            if (!subcategories[doc.subcategory]) {{
              subcategories[doc.subcategory] = [];
            }}
            subcategories[doc.subcategory].push(doc);
          }} else {{
            flatDocs.push(doc);
          }}
        }});
        
        // Render flat docs (no subfolder)
        flatDocs.forEach(doc => {{
          navHtml += `
            <li>
              <button class="nav-item-btn" data-id="${{doc.id}}" onclick="navigateTo('${{doc.id}}')">
                <i data-lucide="file-text" class="nav-icon" style="width: 14px; height: 14px; flex-shrink: 0;"></i>
                <span class="nav-text" title="${{doc.title}}">${{doc.title}}</span>
              </button>
            </li>
          `;
        }});
        
        // Render nested folders (subcategories)
        for (const subcat in subcategories) {{
          const subcatDocs = subcategories[subcat];
          const subcatId = `${{category.toLowerCase().replace(/ /g, '-')}}-${{subcat.toLowerCase().replace(/ /g, '-')}}`;
          
          navHtml += `
            <li class="subcategory-wrapper">
              <button class="nav-subcat-btn" onclick="toggleSubcategory('${{subcatId}}')">
                <div style="display: flex; align-items: center; gap: 8px; overflow: hidden;">
                  <i data-lucide="chevron-right" class="subcat-arrow" id="arrow-${{subcatId}}" style="width: 14px; height: 14px; transition: transform 0.2s; flex-shrink: 0;"></i>
                  <i data-lucide="folder" class="subcat-icon" style="width: 14px; height: 14px; color: var(--text-secondary); flex-shrink: 0;"></i>
                  <span class="nav-text" style="font-weight: 600; font-size: 12.5px;">${{subcat.toUpperCase()}}</span>
                </div>
                <span class="subcat-count">${{subcatDocs.length}}</span>
              </button>
              <ul class="subcat-list" id="list-${{subcatId}}" style="display: none;">
          `;
          
          subcatDocs.forEach(doc => {{
            navHtml += `
              <li>
                <button class="nav-item-btn indent" data-id="${{doc.id}}" onclick="navigateTo('${{doc.id}}')">
                  <i data-lucide="file-text" class="nav-icon" style="width: 13px; height: 13px; flex-shrink: 0;"></i>
                  <span class="nav-text" title="${{doc.title}}">${{doc.title}}</span>
                </button>
              </li>
            `;
          }});
          
          navHtml += `
              </ul>
            </li>
          `;
        }}
        
        navHtml += `
            </ul>
          </div>
        `;
      }});
      
      sidebarNav.innerHTML = navHtml;
      lucide.createIcons();
      
      if (currentDocId) {{
        expandSubcategoryOfDoc(currentDocId);
      }}
    }}

    // Handle Article Selection
    async function loadDocument(id) {{
      const doc = docs.find(d => d.id === id);
      if (!doc) return;
      
      currentDocId = id;
      document.title = `${{doc.title}} — Agentic SDLC Portal`;

      // Update Navigation State
      document.querySelectorAll('.nav-item-btn').forEach(btn => {{
        btn.classList.toggle('active', btn.getAttribute('data-id') === id);
      }});
      expandSubcategoryOfDoc(id);

      // Update Breadcrumbs
      breadcrumbs.innerHTML = `
        <span>${{doc.category}}</span>
        <span class="breadcrumb-sep">&gt;</span>
        <span style="color: var(--text-primary); font-weight: 500;">${{doc.path.split('/').pop()}}</span>
      `;

      // Toggle views
      documentContent.style.display = 'block';
      searchResults.style.display = 'none';

      // Parse Markdown to HTML
      let html = marked.parse(doc.content);
      
      // Translate Alerts
      html = parseAlerts(html);

      // Render Content
      documentContent.innerHTML = html;

      // Initialize Icons
      lucide.createIcons();

      // Highlight code blocks
      Prism.highlightAllUnder(documentContent);

      // Render Mermaid Diagrams
      try {{
        await mermaid.run({{
          querySelector: '.mermaid'
        }});
      }} catch (err) {{
        console.error("Mermaid parsing error:", err);
      }}

      // Build Table of Contents
      buildTOC();

      // Intercept and resolve cross links inside documentContent
      documentContent.querySelectorAll('a').forEach(a => {{
        const href = a.getAttribute('href');
        if (href && !href.startsWith('http') && !href.startsWith('#') && href.endsWith('.md')) {{
          const resolved = resolveDocId(href);
          if (resolved) {{
            a.setAttribute('href', `#${{resolved}}`);
            a.onclick = function(e) {{
              e.preventDefault();
              navigateTo(resolved);
            }};
          }}
        }}
      }});

      // Reset Content Scroll
      document.getElementById('content-container').scrollTop = 0;
    }}

    // Dynamic TOC builder
    function buildTOC() {{
      const headings = documentContent.querySelectorAll('h2, h3');
      if (headings.length === 0) {{
        tocList.innerHTML = '<li><span class="toc-link" style="color: var(--text-secondary); cursor: default;">Không có mục lục</span></li>';
        return;
      }}

      let tocHtml = "";
      headings.forEach((heading, idx) => {{
        const text = heading.textContent;
        const tag = heading.tagName.toLowerCase();
        
        // Ensure element has an ID to link to
        const headingId = `heading-${{idx}}`;
        heading.setAttribute('id', headingId);

        tocHtml += `
          <li>
            <a class="toc-link ${{tag === 'h3' ? 'indent-h3' : ''}}" data-target="${{headingId}}" onclick="scrollToHeading('${{headingId}}')">
              ${{text}}
            </a>
          </li>
        `;
      }});
      
      tocList.innerHTML = tocHtml;
      
      // Intersection Observer to highlight active heading on scroll
      setupTOCScrollSpy();
    }}

    function scrollToHeading(id) {{
      const el = document.getElementById(id);
      if (el) {{
        el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}
    }}

    function setupTOCScrollSpy() {{
      const headings = Array.from(documentContent.querySelectorAll('h2, h3'));
      const tocLinks = Array.from(document.querySelectorAll('.toc-link'));
      const container = document.getElementById('content-container');
      
      container.onscroll = () => {{
        let activeId = "";
        const scrollPos = container.scrollTop + 100;
        
        for (const heading of headings) {{
          if (heading.offsetTop <= scrollPos) {{
            activeId = heading.getAttribute('id');
          }} else {{
            break;
          }}
        }}
        
        tocLinks.forEach(link => {{
          const target = link.getAttribute('data-target');
          link.classList.toggle('active', target === activeId);
        }});
      }};
    }}

    // Dynamic Navigation Routing
    function navigateTo(id) {{
      window.location.hash = id;
      // Close sidebar on mobile
      sidebar.classList.remove('open');
    }}

    // Full-text Local Search Engine
    function executeSearch(query) {{
      if (!query.trim()) {{
        // Reset to last active doc if empty
        if (currentDocId) {{
          loadDocument(currentDocId);
        }}
        return;
      }}

      documentContent.style.display = 'none';
      searchResults.style.display = 'flex';
      
      breadcrumbs.innerHTML = `
        <span>Tìm kiếm</span>
        <span class="breadcrumb-sep">&gt;</span>
        <span style="color: var(--text-primary); font-weight: 500;">"${{query}}"</span>
      `;

      const normalizedQuery = removeDiacritics(query);
      const results = [];

      docs.forEach(doc => {{
        const titleMatch = removeDiacritics(doc.title).includes(normalizedQuery);
        const contentNorm = removeDiacritics(doc.content);
        const queryIndex = contentNorm.indexOf(normalizedQuery);
        
        if (titleMatch || queryIndex !== -1) {{
          let snippet = "";
          
          if (queryIndex !== -1) {{
            const start = Math.max(0, queryIndex - 60);
            const end = Math.min(doc.content.length, queryIndex + normalizedQuery.length + 100);
            let rawSnippet = doc.content.substring(start, end);
            
            // Format highlights
            const searchPattern = new RegExp(`(${{query.replace(/[-\\/\\\\^$*+?.()|[\\]{{}}]/g, '\\\\$&')}})`, 'gi');
            snippet = rawSnippet.replace(searchPattern, '<span class="highlight">$1</span>');
            snippet = (start > 0 ? '...' : '') + snippet + (end < doc.content.length ? '...' : '');
          }} else {{
            snippet = doc.content.substring(0, 160) + '...';
          }}

          results.push({{
            id: doc.id,
            title: doc.title,
            path: doc.path,
            snippet: snippet
          }});
        }}
      }});

      // Show Results
      if (results.length === 0) {{
        searchResultsList.innerHTML = `<div style="text-align: center; padding: 40px; color: var(--text-secondary);">
          <i data-lucide="frown" style="width: 48px; height: 48px; margin-bottom: 12px;"></i>
          <p>Không tìm thấy kết quả nào phù hợp với từ khóa.</p>
        </div>`;
      }} else {{
        let listHtml = "";
        results.forEach(res => {{
          listHtml += `
            <div class="search-result-item" onclick="navigateTo('${{res.id}}'); document.getElementById('search-input').value = '';">
              <div class="search-result-title">${{res.title}}</div>
              <div class="search-result-snippet">${{res.snippet}}</div>
              <div class="search-result-path">${{res.path}}</div>
            </div>
          `;
        }});
        searchResultsList.innerHTML = listHtml;
      }}
      lucide.createIcons();
    }}

    // Event Listeners
    searchInput.addEventListener('input', (e) => {{
      executeSearch(e.target.value);
    }});

    menuToggle.addEventListener('click', () => {{
      sidebar.classList.toggle('open');
    }});

    // Handle Hash Navigation (browser history)
    window.addEventListener('hashchange', () => {{
      const hash = window.location.hash.substring(1);
      if (hash) {{
        loadDocument(hash);
      }}
    }});

    // On Load Initial Setup
    window.addEventListener('DOMContentLoaded', () => {{
      renderSidebar();
      
      const hash = window.location.hash.substring(1);
      if (hash && docs.some(d => d.id === hash)) {{
        loadDocument(hash);
      }} else {{
        // Load default document (usually README or overview)
        const defaultDoc = docs.find(d => d.id === 'readme') || docs[0];
        if (defaultDoc) {{
          navigateTo(defaultDoc.id);
        }}
      }}
    }});

  </script>
</body>
</html>
"""
    
if __name__ == '__main__':
    main()
