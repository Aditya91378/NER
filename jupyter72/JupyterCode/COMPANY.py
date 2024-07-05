import re

# Example text
text = "Acme Corporation Ltd, Globex Inc. Ltd, Stark Industries Pvt Ltd, Stark Industries Offered by Stark Industries"

# Regex pattern to match company name with various keywords
regex = r'(\w+(?:\s\w+)*)\s(?:Inc\.\s)?(?:Pvt\s)?(?:Offered\sby\s)?Ltd'

# Find all matches in the text
matches = re.findall(regex, text, re.IGNORECASE)

# Output the company names
for company in matches:
    print(company)