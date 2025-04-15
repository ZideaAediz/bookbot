def get_num_words(content):
    words = content.split()
    return len(words)

def get_character_count(content):
    results = {}
    for c in content:
        lc = c.lower()
        if (lc not in results):
            results[lc] = 0
        
        results[lc] += 1

    return results

def get_sorted_character_count(char_dict):
    def sort_on(d):
        return d["count"]
    
    results = []
    for key in char_dict:
        if key.isalpha():
            results.append({"char":key, "count":char_dict[key]})

    results.sort(reverse=True, key=sort_on)
    return results