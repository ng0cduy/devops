def solution():
    import re
    import os
    import sys
    # Implement the solution here
    path = "/root/user/logs/"
    files = [x for x in os.listdir(path) if x.endswith(".log")]
    regex_pattern = r'^\[\d{2}/[A-Za-z]{3}/\d{4}:(\d{2}):\d{2}:\d{2} .*?\] "([A-Z]+) .*?" (\d{3})'
    hourly_counts = {}
    for file in files:
        with open(f"{path}/{file}", 'r') as f:
            logs = f.readlines()
        for log in logs:
            match = re.search(regex_pattern, log)
            if match:
                hour = match.group(1)
                method = match.group(2)
                status = int(match.group(3))
                if method == 'POST' and 400 <= status < 500:
                    if hour not in hourly_counts:
                        hourly_counts[hour] = 0
                    hourly_counts[hour] += 1
    if not hourly_counts:
        return ""
    sorted_hours = sorted(hourly_counts.items(), key=lambda item: (-item[1], item[0]))
    best_hour, count = sorted_hours[0]
    return f"{best_hour} {count}"


if __name__ == '__main__':
    print(solution())
