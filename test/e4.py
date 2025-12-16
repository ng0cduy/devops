from typing import List
import os
import re
from datetime import datetime, timedelta

def solution(threshold: int, duration: int) -> List[str]:

    CURRENT_DATE_STR = "15/Sep/2021:00:00:00 +0000"
    DATE_FMT = "%d/%b/%Y:%H:%M:%S %z"
    current_date = datetime.strptime(CURRENT_DATE_STR, DATE_FMT)
    start_date = current_date - timedelta(days=duration)
    # Implement the solution here
    path = "/var/logs/server/"
    regex_pattern = r'^\[(.*?)\] "(\w+) .*?" (\S+) (\d{3})'
    ip_timestamps = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        for line in f:
                            match = re.search(regex_pattern, line)
                            if match:
                                ts_str = match.group(1)
                                method = match.group(2)
                                ip = match.group(3)
                                status = int(match.group(4))

                                if method == "POST" and 200 <= status < 300:
                                    try:
                                        ts = datetime.strptime(ts_str, DATE_FMT)
                                        if start_date <= ts <= current_date:
                                            if ip not in ip_timestamps:
                                                ip_timestamps[ip] = []
                                            ip_timestamps[ip].append(ts)
                                    except ValueError:
                                        continue
                except (OSError, IOError):
                    continue

    result_ips = []
    window_delta = timedelta(minutes=15)

    for ip, timestamps in ip_timestamps.items():
        timestamps.sort()
        window = []
        found = False

        for t in timestamps:
            window.append(t)

            while window and (t - window[0] > window_delta):
                window.pop(0)

            if len(window) > threshold:
                result_ips.append(ip)
                found = True
                break

    # Return sorted list of unique IPs
    return sorted(result_ips)

    return ""


if __name__ == '__main__':
    print(solution())

