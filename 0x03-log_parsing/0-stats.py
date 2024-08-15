#!/usr/bin/env python3
import sys
import signal
import re

# Initialize variables
total_file_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

# Regular expression pattern to match the required input format
log_pattern = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

def print_stats():
    """Prints the current statistics."""
    global total_file_size, status_codes_count
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def process_line(line):
    """Process a single line of input and update metrics."""
    global total_file_size, status_codes_count
    match = log_pattern.match(line)
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))

        total_file_size += file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

def handle_interrupt(signum, frame):
    """Handle the keyboard interrupt (Ctrl + C) signal."""
    print_stats()
    sys.exit(0)

# Set up signal handler for Ctrl + C
signal.signal(signal.SIGINT, handle_interrupt)

try:
    # Read input line by line
    for line in sys.stdin:
        process_line(line.strip())
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    handle_interrupt(None, None)

# Print remaining stats at the end of the input
print_stats()

