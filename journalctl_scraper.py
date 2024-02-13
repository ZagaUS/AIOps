import subprocess

def monitor_journalctl(keywords):
    # Run the journalctl command with the '-f' option to follow the journal
    process = subprocess.Popen(['journalctl', '-f'], stdout=subprocess.PIPE)

    # Continuously monitor the output and print new lines
    while True:
        # Read a line from the journalctl output
        line = process.stdout.readline()

        # Decode the line from bytes to string
        line = line.decode('utf-8')

        # Check if the line contains any of the specified keywords
        if any(keyword in line for keyword in keywords):
            # Print the line
            print(line.strip())
            ##add code to forward to LLLM/RAG/VectorDB

if __name__ == "__main__":
    # Specify the keywords you want to filter by
    keywords = ["microshift"]

    # Start monitoring journalctl with the specified keywords
    monitor_journalctl(keywords)