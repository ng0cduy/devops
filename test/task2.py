import os
import re

def solution():
    log_dir = '/root/user/logs/'
    # Fallback for local testing if the specific path doesn't exist
    if not os.path.exists(log_dir):
        log_dir = '.'

    hourly_counts = {}

    # Regex to capture Hour, Method, Status
    # Example: [12/Feb/2023:08:23:17 +0000] "POST /api/v1/resource HTTP/1.1" 404 54321
    # Group 1: Hour (08)
    # Group 2: Method (POST)
    # Group 3: Status (404)
    regex_pattern = r'^\[\d{2}/[A-Za-z]{3}/\d{4}:(\d{2}):\d{2}:\d{2} .*?\] "([A-Z]+) .*?" (\d{3})'

    try:
        # Get all .log files in the directory
        files = [f for f in os.listdir(log_dir) if f.endswith('.log')]
        
        for filename in files:
            filepath = os.path.join(log_dir, filename)
            with open(filepath, 'r') as f:
                for line in f:
                    match = re.search(regex_pattern, line)
                    if match:
                        hour = match.group(1)
                        method = match.group(2)
                        status = int(match.group(3))

                        # Check for POST method and Client Error (4xx)
                        if method == 'POST' and 400 <= status < 500:
                            if hour not in hourly_counts:
                                hourly_counts[hour] = 0
                            hourly_counts[hour] += 1
                            
    except FileNotFoundError:
        return ""

    if not hourly_counts:
        return ""

    # Sort by count (descending) and then by hour (ascending)
    # Since hour is a two-digit string ("00" to "23"), string comparison works for finding the lowest hour.
    sorted_hours = sorted(hourly_counts.items(), key=lambda item: (-item[1], item[0]))
    
    best_hour, count = sorted_hours[0]
    return f"{best_hour} {count}"

if __name__ == "__main__":
    print(solution())
