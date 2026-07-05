import json

with open('notebooks/task1_eda.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('eda_matches.txt', 'w', encoding='utf-8') as out:
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            code = "".join(cell['source'])
            if 'InvoiceDate' in code or 'Year' in code or 'Month' in code or 'Day' in code:
                out.write(f"Cell {i}:\n")
                out.write(code)
                out.write("\n" + "-" * 40 + "\n")
print("✅ Matches written to eda_matches.txt")
