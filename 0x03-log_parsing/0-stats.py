#!/usr/bin/python3
import sys
import re

# Initialize variables to store statistics
total_file_size = 0
status_code_counts = {}

try:
    # Read lines from stdin
    for line_number, line in enumerate(sys.stdin, start=1):
        # Use regular expression to parse the input line
        match = re.match(r'^(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)', line)
        if match:
            ip_address, status_code, file_size = match.groups()

            # Update total file size
            total_file_size += int(file_size)

            # Update status code counts
            status_code = int(status_code)
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

        # Print statistics after every 10 lines
        if line_number % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                print(f"{code}: {status_code_counts[code]}")
        
except KeyboardInterrupt:
    pass  # Handle CTRL+C gracefully

# Print the final statistics
print(f"Total file size: {total_file_size}")
for code in sorted(status_code_counts.keys()):
    print(f"{code}: {status_code_counts[code]}")
