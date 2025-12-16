def solution():
    import re
    import os
    
    # Use the path provided in the user's code, but fallback to local for testing
    path = "/root/devops/app.log"
    if not os.path.exists(path):
        path = "app.log"
        
    result_dict = {}
    
    # Regex to capture Method, Path, Status, Size
    # Example: [10/Oct/2024:03:30:12 -0500] "POST /api/v2/resource3 HTTP/1.0" 201 1931
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
                    
                    # Filter for POST requests and 2xx status codes
                    if method == 'POST' and 200 <= status < 300:
                        if path_url in result_dict:
                            result_dict[path_url] += size
                        else:
                            result_dict[path_url] = size
                            
    except FileNotFoundError:
        return []

    result = []
    for item in result_dict:
        result.append(f"{item} {result_dict[item]}")
    return result

if __name__ == '__main__':
    print(solution())
