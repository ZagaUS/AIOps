import csv

# Define keywords to filter lines
keywords = ["error", "ailed"]

# Open input and output files
input_file_path = "microshift.log"
output_file_path = "filtered_microshift_logs.csv"

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
    # Create CSV writer
    csv_writer = csv.writer(output_file)

    # Write header to CSV file
    csv_writer.writerow(['Timestamp', 'Host', 'process', 'Message'])
    linecounter=0
    # Process each line in the log file
    for line in input_file:
        # Split the line into components
        parts = line.split()
        
        # Extract relevant information
        timestamp = f"{parts[0]} {parts[1]} {parts[2]}"
        component = parts[3]
        level = parts[4]
        message = ' '.join(parts[5:])

        # Check if the line contains any keyword
        #if any(keyword in message for keyword in keywords):
        if all(keyword in message for keyword in keywords):
            # Write relevant information to CSV file
            csv_writer.writerow([timestamp, component, level, message])
            linecounter+=1

print(f"Filtered {linecounter} log lines with keywords '{', '.join(keywords)}' to {output_file_path}")
