import os
import requests
from bs4 import BeautifulSoup

# File path to your HTML file
file_path = 'file.html'

# Output folder (will be created if not exists)
output_folder = ' CKA-study-guide'
os.makedirs(output_folder, exist_ok=True)

# Read HTML file
with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find and download all data-src images
for idx, li in enumerate(soup.find_all('li', class_='carousel-slide'), start=1):
    img = li.find('img')
    if img and img.get('data-src'):
        img_url = img['data-src']
        try:
            print(f"Downloading image {idx} from {img_url}")
            response = requests.get(img_url)
            response.raise_for_status()
            # Save as 1.jpg, 2.jpg, ...
            file_path = os.path.join(output_folder, f"{idx}.jpg")
            with open(file_path, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            print(f"Failed to download image {idx}: {e}")
