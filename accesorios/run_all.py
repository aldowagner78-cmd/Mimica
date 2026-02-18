import os
import csv
import subprocess
import glob

def run_script(script_name):
    print(f"Running {script_name}...")
    subprocess.run(["python", script_name], check=True)

def merge_csvs(output_file, input_files):
    print(f"Merging {len(input_files)} CSV files into {output_file}...")
    
    header_written = False
    
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        
        for input_file in input_files:
            if not os.path.exists(input_file):
                print(f"Warning: {input_file} not found.")
                continue
                
            with open(input_file, 'r', encoding='utf-8') as infile:
                reader = csv.reader(infile)
                try:
                    header = next(reader) # Read header
                except StopIteration:
                    continue # Empty file
                
                if not header_written:
                    writer.writerow(header)
                    header_written = True
                
                # Verify header matches (optional, but good practice)
                # if header != ...
                
                for row in reader:
                    writer.writerow(row)
    
    print("Merge complete.")

def main():
    # 1. Run all generations
    scripts = ["gen_part1.py", "gen_part2.py", "gen_part3.py", "gen_part4.py", "gen_part5.py"]
    csvs = ["db_part1.csv", "db_part2.csv", "db_part3.csv", "db_part4.csv", "db_part5.csv"]
    
    for script in scripts:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"Error: {script} missing!")
            return

    # 2. Merge into main DB
    merge_csvs("charadas_latam_database.csv", csvs)
    
    # 3. Convert to JS
    if os.path.exists("convert_database.py"):
        run_script("convert_database.py")
    else:
        print("Error: convert_database.py missing!")

if __name__ == "__main__":
    main()
