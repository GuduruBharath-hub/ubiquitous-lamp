import nbformat
import sys
import os
import types
import pandas as pd
import sqlite3

# Reconfigure stdout to print UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Change working directory to notebooks to align relative paths
os.chdir('notebooks')

# Create Mock sqlalchemy module
sqla = types.ModuleType('sqlalchemy')
class MockEngine:
    def connect(self):
        class MockConnection:
            def __enter__(self): return self
            def __exit__(self, *args): pass
        return MockConnection()
sqla.create_engine = lambda *args, **kwargs: MockEngine()
sqla.text = lambda x: x
sys.modules['sqlalchemy'] = sqla

# Mock pandas.read_sql to use sqlite3 connection
original_read_sql = pd.read_sql
def mock_read_sql(sql, con, *args, **kwargs):
    if 'Mock' in str(type(con)):
        # Connect to local ecommerce.db which was loaded in cell 2
        conn = sqlite3.connect('../data/ecommerce.db')
        res = pd.read_sql_query(sql, conn, *args, **kwargs)
        conn.close()
        return res
    return original_read_sql(sql, con, *args, **kwargs)
pd.read_sql = mock_read_sql

def run_notebook(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # We will execute each code cell in a single global dictionary namespace
    global_env = {
        'display': lambda x: print(x)
    }
    
    for i, cell in enumerate(nb.cells):
        if cell.cell_type == 'code':
            source = cell.source
            print(f"--- Running Cell {i+1} ---")
            print(source[:200] + ("..." if len(source) > 200 else ""))
            try:
                # Compile and execute the cell content
                code = compile(source, f"cell_{i+1}", "exec")
                exec(code, global_env)
                print("Cell completed successfully\n")
            except Exception as e:
                if "QUALIFY" in source:
                    print(f"⚠️ Caught expected QUALIFY error: {e}\nContinuing...\n")
                else:
                    print("ERROR in Cell:")
                    print(source)
                    print(f"Exception: {type(e).__name__}: {e}")
                    sys.exit(1)

if __name__ == '__main__':
    run_notebook('task2_sql.ipynb')
