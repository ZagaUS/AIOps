def filter_lines(input_file, output_file, keywords):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if any(keyword in line for keyword in keywords):
                outfile.write(line)

# Example usage:
input_file = 'microshift.log'
output_file = 'output.txt'
keywords = ['error', 'Fail', 'Warn']

filter_lines(input_file, output_file, keywords)
