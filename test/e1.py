def solution():
    import re
    # Implement the solution here
    path = "/var/logs/events.log"
    regex_pattern = r'^\[.*\] "([A-Z]+) (.+?) HTTP/.*" (\d{3}) (\d+)'
    with open(path, 'r') as f:
        logs = f.readlines()
    success_post_request = 0
    for log in logs:
        match = re.search(regex_pattern, log)
        if match:
            method = match.group(1)
            status = int(match.group(3))
            if method == 'POST' and 200 <= status < 300:
                success_post_request += 1
    return success_post_request


if __name__ == '__main__':
    print(solution())
