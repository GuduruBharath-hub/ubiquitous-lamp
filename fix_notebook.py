"""
Fix script v3 for task5_final.ipynb
Fixes:
  1. Incorrect escaping of datetime.now().strftime in Cell 14 that produces syntax error in pipeline.py
  2. Clean up 'Done Done' to 'Done' in Cell 11
"""
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

nb_path = r'notebooks/task5_final.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# ── Fix 1: Correct datetime.now().strftime inside pipeline_script in Cell 14 ──
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        src = cell['source']
        if isinstance(src, list):
            src_joined = ''.join(src)
        else:
            src_joined = src

        # Check for the strftime issue inside pipeline_script
        if "datetime.now().strftime(\\\\%Y-%m-%d %H:%M:%S\\\\)" in src_joined:
            print(f"Found strftime issue in Cell {i}")
            if isinstance(src, list):
                new_src = []
                for line in src:
                    new_line = line.replace(
                        "datetime.now().strftime(\\\\%Y-%m-%d %H:%M:%S\\\\)",
                        "datetime.now().strftime('%Y-%m-%d %H:%M:%S')"
                    )
                    new_src.append(new_line)
                cell['source'] = new_src
                print("  -> Fixed strftime in Cell source")

        # Check for 'Done Done' in PDF generator
        if "'Done Done'" in src_joined:
            print(f"Found 'Done Done' issue in Cell {i}")
            if isinstance(src, list):
                new_src = []
                for line in src:
                    new_line = line.replace(
                        "'Done Done'",
                        "'Done'"
                    )
                    new_src.append(new_line)
                cell['source'] = new_src
                print("  -> Fixed 'Done Done' to 'Done'")

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("\n✅ Fix v3 applied successfully!")
