
import os
import json
import re

def parse_paper_html():
    file_path = '/Users/harold/Desktop/Github-Program/Testing/Lab-master/paper.html'
    output_path = '/Users/harold/Desktop/Github-Program/Testing/hpc-lab-vue/src/data/publications.json'
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize whitespace
    content = re.sub(r'\s+', ' ', content)
    
    # Strategy: Find blocks starting with Year header and extract rows until next Header or end of table
    # Since the structure is flat (thead then tbody), we can split by '<thead><tr><th>'
    
    parts = re.split(r'<thead>\s*<tr>\s*<th>', content)
    
    final_data = []
    
    for part in parts:
        # Check if this part starts with a year
        year_match = re.match(r'(\d{4})</th>', part)
        if not year_match:
            continue
            
        year = year_match.group(1)
        print(f"Processing year: {year}")
        
        # Now find all <tr><td>...</td></tr> in this part (before the next split)
        # We need to be careful not to overshoot into next section if split didn't work perfectly
        # But split removes the delimiter.
        
        # It seems the structure is <thead>...</thead><tbody>...</tbody>
        # So we look for <tbody> content
        tbody_match = re.search(r'<tbody>(.*?)</tbody>', part)
        if not tbody_match:
            print(f"No tbody found for year {year}")
            continue
            
        tbody_content = tbody_match.group(1)
        
        # Find all rows
        # The rows are <tr><td>Content</td></tr>
        rows = re.findall(r'<tr>\s*<td>(.*?)</td>\s*</tr>', tbody_content)
        
        items_list = []
        for row_html in rows:
            # Clean HTML tags
            # Replace <span ...>[TXT]</span> with [TXT]
            # Replace <a ...>...</a> with just text? Or keep link?
            
            # Extract link if exists
            link_match = re.search(r'href=["\'](.*?)["\']', row_html)
            link = link_match.group(1) if link_match else ""
            
            # Remove tags
            clean_text = re.sub(r'<[^>]+>', '', row_html).strip()
            # Unescape html entities if needed, simplistic approach
            clean_text = clean_text.replace('&nbsp;', ' ').replace('&amp;', '&')
            
            items_list.append({
                "content": clean_text,
                "link": link
            })
            
        final_data.append({
            "year": year,
            "items": items_list
        })

    # Sort final_data by year descending
    final_data.sort(key=lambda x: x['year'], reverse=True)

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully exported data for years: {[x['year'] for x in final_data]}")

if __name__ == "__main__":
    parse_paper_html()
