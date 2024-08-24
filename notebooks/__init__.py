import sys
import os

# Add the project's root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts import load_and_prepare_data

from scripts import load_and_prepare_data
from scripts import evaluate_region


def main():
    # Accept file paths for analysis
    file_paths = [
        (r'./data/benin-malanville.csv', 'Benin (Malanville)'),
        (r'./data/sierraleone-bumbuna.csv', 'Sierra Leone (Bumbuna)'),
        (r'./data/togo-dapaong_qc.csv', 'Togo (Dapaong)')
    ]
    
    region_ghis = {}
    models = {}
    
    for file_path, region_name in file_paths:
        df = load_and_prepare_data(file_path)
        avg_ghi, model = evaluate_region(df, region_name)
        region_ghis[region_name] = avg_ghi
        models[region_name] = model
    
    best_region = max(region_ghis, key=region_ghis.get)
    print(f"\nBased on the analysis, the region with the highest solar potential is: {best_region}")
    
if __name__ == "__main__":
    main()
