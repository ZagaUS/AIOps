import csv

# Function to extract error description and error code from each line
def extract_error_info(line):
    parts = line.split('Err:')
    if len(parts) == 2:
        err_part = parts[1].strip().split(' ')
        error_code = err_part[0]
        error_desc = ' '.join(err_part[2:])[1:-1]  # Removing quotes
        return error_code, error_desc
    else:
        return None, None

# Read the CSV file and extract error info
with open('removedTimestamps.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        line = row[0]
        error_code, error_desc = extract_error_info(line)
        print("Error Code:", error_code)
        print("Error Description:", error_desc)
        print("-----")