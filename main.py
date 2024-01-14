import re
def extract_asin(url):
    # Define a regular expression pattern to match ASIN in Amazon URLs
    pattern = r'/([A-Z0-9]{10})(?:[/?]|$)'

    match = re.search(pattern, url)

    if match:
        return match.group(1)
    else:
        return None

file_path = r'C:\Users\********' #file path hidden

with open(file_path, 'r') as file:
    lines = file.readlines()

    for line in lines:
        url = line.strip()
        asin = extract_asin(url)
        if asin:
            print(asin)
        else:
            print("ASIN not found")