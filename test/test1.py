def solution():
    import re
    import os

    # Use the path provided in the problem description
    log_dir = "/root/devops/"
    # Fallback for local testing if the specific path doesn't exist
    if not os.path.exists(log_dir):
        log_dir = "."
        
    # Dictionary to store data: path -> {'count': 0, 'bytes': 0}
    data = {}
    
    # Regex to capture Method, Path, Status, Size
    # Example: [10/Oct/2024:03:30:12 -0500] "POST /api/v2/resource3 HTTP/1.0" 201 1931
    regex_pattern = r'^\[.*\] "([A-Z]+) (.+?) HTTP/.*" (\d{3}) (\d+)'
    
    try:
        # Get all .log files in the directory
        files = [f for f in os.listdir(log_dir) if f.endswith(".log")]
        
        for filename in files:
            file_path = os.path.join(log_dir, filename)
            with open(file_path, 'r') as f:
                for line in f:
                    match = re.search(regex_pattern, line)
                    if match:
                        method = match.group(1)
                        path_url = match.group(2)
                        status = int(match.group(3))
                        size = int(match.group(4))
                        
                        # Filter for successful POST requests (2xx status codes)
                        if method == 'POST' and 200 <= status < 300:
                            if path_url not in data:
                                data[path_url] = {'count': 0, 'bytes': 0}
                            
                            data[path_url]['count'] += 1
                            data[path_url]['bytes'] += size
                            
    except FileNotFoundError:
        return []

    # Sort the resources:
    # 1. By number of requests in descending order (-item[1]['count'])
    # 2. Lexicographically by path name (item[0])
    sorted_items = sorted(data.items(), key=lambda item: (-item[1]['count'], item[0]))

    result = []
    for path_url, stats in sorted_items:
        result.append(f"{path_url} {stats['bytes']}")

    return result

if __name__ == '__main__':
    print(solution())
