import os
import json

def build_catalog():
    papers_dir = 'papers'
    catalog = []
    
    # Check if papers directory exists
    if not os.path.exists(papers_dir):
        print(f"Error: {papers_dir} directory not found.")
        return

    print("Scanning papers directory for quiz JSON files...")
    
    # Scan all json files in papers/
    filenames = sorted(os.listdir(papers_dir))
    for filename in filenames:
        if filename.endswith('.json') and filename != 'catalog.json':
            filepath = os.path.join(papers_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Check if it's the new format (dict with title/description/sections)
                if isinstance(data, dict):
                    title = data.get('title', filename.replace('.json', '').replace('_', ' ').title())
                    description = data.get('description', '')
                    sections = data.get('sections', [])
                else:
                    # Fallback to old format (list of sections)
                    title = filename.replace('.json', '').replace('_', ' ').title()
                    description = f"Timed test containing {len(data)} sections."
                    sections = data
                
                total_duration = sum(s.get('duration', 0) for s in sections)
                total_questions = sum(len(s.get('questions', [])) for s in sections)
                
                catalog.append({
                    "id": filename.replace('.json', ''),
                    "title": title,
                    "description": description,
                    "duration": total_duration,
                    "questionsCount": total_questions
                })
                print(f" - Parsed {filename}: '{title}' ({total_questions} Qs, {total_duration} mins)")
            except Exception as e:
                print(f"Error parsing {filename}: {e}")
                
    catalog_path = os.path.join(papers_dir, 'catalog.json')
    try:
        with open(catalog_path, 'w', encoding='utf-8') as f:
            json.dump(catalog, f, indent=2, ensure_ascii=False)
        print(f"\nSuccessfully generated {catalog_path} with {len(catalog)} papers!")
    except Exception as e:
        print(f"Error writing catalog.json: {e}")

if __name__ == '__main__':
    build_catalog()
