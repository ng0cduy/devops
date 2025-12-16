import re
import os

def remove_timestamp():
    input_file = 'app.log'
    output_file = 'app_cleaned.log'
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    # Regex to match the timestamp [dd/Mon/yyyy:hh:mm:ss +/-zone] and optional following whitespace
    # Pattern breakdown:
    # \[          : Literal [
    # \d{2}       : 2 digits (day)
    # /           : Literal /
    # [A-Za-z]{3} : 3 letters (month)
    # /           : Literal /
    # \d{4}       : 4 digits (year)
    # :           : Literal :
    # \d{2}:\d{2}:\d{2} : hh:mm:ss
    # \s          : Space
    # [+-]\d{4}   : Timezone offset
    # \]          : Literal ]
    # \s*         : Optional trailing whitespace
    timestamp_pattern = r'\[\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2} [+-]\d{4}\]\s*'

    try:
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            for line in f_in:
                # Remove the timestamp from the line
                cleaned_line = re.sub(timestamp_pattern, '', line)
                f_out.write(cleaned_line)
        
        print(f"Successfully removed timestamps. Output saved to {output_file}")
        
        # Optional: Print first few lines to verify
        print("\nFirst 3 lines of cleaned file:")
        with open(output_file, 'r') as f:
            for i in range(3):
                print(f.readline().strip())
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    remove_timestamp()
