import re

def parse_js_array(raw_array):
    # This regex handles escaped quotes: matches content between ' or " 
    # taking into account backslash escapes.
    pattern = r"'(.*?(?<!\\))'|\"(.*?(?<!\\))\""
    matches = re.findall(pattern, raw_array)
    # re.findall with groups returns tuples, we take the non-empty one
    return [m[0] if m[0] else m[1] for m in matches]

def create_csv():
    try:
        with open('gameData.js', 'r', encoding='utf-8') as f:
            content = f.read()

        cat_pattern = r'\{\s*id:\s*\'(.*?)\'.*?words_es:\s*\[(.*?)\].*?words_en:\s*\[(.*?)\].*?\}'
        blocks = re.findall(cat_pattern, content, re.DOTALL)

        csv_lines = ['Category,Spanish,English']
        for cat_id, es_words_raw, en_words_raw in blocks:
            es_words = parse_js_array(es_words_raw)
            en_words = parse_js_array(en_words_raw)
            
            max_len = max(len(es_words), len(en_words))
            for i in range(max_len):
                es = es_words[i] if i < len(es_words) else ""
                en = en_words[i] if i < len(en_words) else ""
                
                # Unescape standard JS escapes for the CSV
                es = es.replace("\\'", "'").replace('\\"', '"')
                en = en.replace("\\'", "'").replace('\\"', '"')
                
                es_csv = es.replace('"', '""')
                en_csv = en.replace('"', '""')
                csv_lines.append(f'"{cat_id}","{es_csv}","{en_csv}"')

        with open('palabras_mimica.csv', 'w', encoding='utf-8') as f:
            f.write('\n'.join(csv_lines))
        print("CSV created successfully")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_csv()
