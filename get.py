import requests
import json

# Step 1: Correct API URL
response = requests.get("https://coderbyte.com/api/challenges/json/wizard-list")

# Step 2: Convert to Python data
data = response.json()

# Step 3: Case-insensitive sort of all dictionary keys
def sort_case_insensitive(obj):
    if isinstance(obj, dict):
        return {k: sort_case_insensitive(obj[k]) for k in sorted(obj, key=lambda x: x.lower())}
    elif isinstance(obj, list):
        return [sort_case_insensitive(i) for i in obj]
    else:
        return obj

sorted_data = sort_case_insensitive(data)

# Step 4: Remove duplicate dictionaries from lists
def remove_duplicate_dicts(obj):
    if isinstance(obj, list):
        new_list = []
        seen = set()
        for item in obj:
            if isinstance(item, dict):
                item_str = json.dumps(item, sort_keys=True)
                if item_str not in seen:
                    seen.add(item_str)
                    new_list.append(remove_duplicate_dicts(item))
            else:
                new_list.append(remove_duplicate_dicts(item))
        return new_list
    elif isinstance(obj, dict):
        return {k: remove_duplicate_dicts(v) for k, v in obj.items()}
    else:
        return obj

# Step 5: Apply deduplication
deduped_data = remove_duplicate_dicts(sorted_data)

# Step 6: Output final result
print(json.dumps(deduped_data, indent=2))
