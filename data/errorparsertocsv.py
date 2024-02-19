import re
import csv

def parse_error_log(log_file_path, output_csv_path):
    try:
        # Open the log file for reading
        with open(log_file_path, 'r') as file:
            # Open the CSV file for writing
            with open(output_csv_path, 'w', newline='') as csvfile:
                # Define the CSV writer
                csv_writer = csv.writer(csvfile)

                # Write the header row
                csv_writer.writerow(["Error Message"])

                # Read each line of the log file
                for line in file:
                    # Define a regex pattern to match error messages
                    #error_pattern = r'ERROR: (.*)'  # Adjust this pattern based on your log format
                    #error_warning_pattern = r'(ERROR|WARNING): (.*)'

                    # error_pattern = r'E0210|I0210 (.*)'  # Adjust this pattern based on your log format
                    
                    error_pattern = r'error|Failed|Error|failed (.*)'  # Adjust this pattern based on your log format

                    # Search for the error pattern in the current line
                    match = re.search(error_pattern, line)
                    if match:
                        # If a match is found, extract the error message
                        error_message = match.group(1)
                        
                        # Write the error message to the CSV file
                        csv_writer.writerow([error_message])

    except IOError as e:
        # Handle file IO errors
        print(f"Error reading or writing file: {e}")

# Example usage:
# log_file_path = '/Users/jpaulraj/aiopsdemo/microshift.log'
# output_csv_path = '/Users/jpaulraj/aiopsdemo/output.csv'
log_file_path = './microshift.log'
output_csv_path = './output.csv'

parse_error_log(log_file_path, output_csv_path)
