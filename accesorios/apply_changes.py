import csv
import re
import json

def update_data():
    csv_path = 'palabras_mimica.csv'
    js_path = 'gameData.js'
    
    deleted_lines = {45, 94, 95, 122, 123, 127, 128, 129, 133, 195, 197, 207, 209, 300}
    
    rows = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        current_line = 1
        for row in reader:
            current_line += 1
            if current_line in deleted_lines:
                continue
            
            # Modifications
            if current_line == 104:
                row[1] = "Mujer Maravilla"
            elif current_line == 110:
                row[1] = "Robin Hood"
                row[2] = "Robin Hood"
            elif current_line == 131:
                row[1] = "Hulk golpeando"
                row[2] = "Hulk hitting"
            elif current_line == 174:
                row[1] = "Cambiar foco"
            elif current_line == 255:
                row[1] = "Tocar la guitarra"
                row[2] = "Playing guitar"
            
            rows.append(row)

    # Save modified CSV
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

    # Re-group by category
    categories_dict = {}
    for row in rows:
        cat_id = row[0]
        if cat_id not in categories_dict:
            categories_dict[cat_id] = {'es': [], 'en': []}
        categories_dict[cat_id]['es'].append(row[1])
        categories_dict[cat_id]['en'].append(row[2])

    with open(js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()

    meta_pattern = r"id:\s*'(.*?)',\s*icon:\s*'(.*?)'"
    metadata = re.findall(meta_pattern, js_content)
    
    new_cat_blocks = []
    for cid, icon in metadata:
        if cid in categories_dict:
            es_words = categories_dict[cid]['es']
            en_words = categories_dict[cid]['en']
            
            def js_list(words):
                items = []
                for w in words:
                    cleaned = w.replace("'", "\\'")
                    items.append(f"'{cleaned}'")
                return "[" + ", ".join(items) + "]"

            block = f"  {{\n    id: '{cid}', icon: '{icon}',\n    words_es: {js_list(es_words)},\n    words_en: {js_list(en_words)}\n  }}"
            new_cat_blocks.append(block)

    new_categories_js = "const CATEGORIES = [\n" + ",\n\n".join(new_cat_blocks) + "\n];"
    updated_js = re.sub(r'const CATEGORIES = \[.*?\];', new_categories_js, js_content, flags=re.DOTALL)

    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(updated_js)
    
    print("Updates applied successfully")

if __name__ == "__main__":
    update_data()
