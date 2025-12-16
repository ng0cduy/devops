def solution():
    import re
    import os

    path = "/root/devops/app.log"

    # Dictionary to store data: path -> {'count': 0, 'bytes': 0}
    data = {}
    regex_pattern = r'^\[.*\] "([A-Z]+) (.+?) HTTP/.*" (\d{3}) (\d+)'

    try:
        with open(path, 'r') as f:
            for line in f:
                match = re.search(regex_pattern, line)
                if match:
                    method = match.group(1)
                    path_url = match.group(2)
                    status = int(match.group(3))
                    size = int(match.group(4))
                    if method == 'POST' and 200 <= status < 300:
                        if path_url not in data:
                            data[path_url] = {'count': 0, 'bytes': 0}

                        data[path_url]['count'] += 1
                        data[path_url]['bytes'] += size

    except FileNotFoundError:
        return []

    sorted_items = sorted(data.items(), key=lambda item: (-item[1]['count'], item[0]))

    result = []
    for path_url, stats in sorted_items:
        result.append(f"{path_url} {stats['bytes']}")

    return result


if __name__ == '__main__':
    print(solution())
