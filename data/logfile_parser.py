import re
import csv

# Define the regular expression pattern to extract information
pattern = re.compile(r'(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) .*? microshift\[(\d+)\]: ')

# Function to parse log lines and extract information
def parse_log_line(line):
    match = pattern.match(line)
    if match:
        return {
            'Timestamp': match.group(1),
            'Process_ID': match.group(2),
            'Error_Code': match.group(3),
            'Line_Number': match.group(4),
            'Message': match.group(5),
            'Error_Description': match.group(6),
            'Pod': match.group(7)
        }
    else:
        return None

# Function to write extracted information into a CSV file
def write_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Timestamp', 'Process_ID', 'Error_Code', 'Line_Number', 'Message', 'Error_Description', 'Pod'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Parse the log file and extract information
parsed_data = []
with open('microshift.log', 'r') as log_file:
    for line in log_file:
        parsed_line = parse_log_line(line)
        if parsed_line:
            parsed_data.append(parsed_line)

# Write extracted information into a CSV file
write_to_csv(parsed_data, 'microshift_parsed.csv')
