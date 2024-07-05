import re

# Example text
text = "The project duration is 6 weeks. The tenure of the contract is 3 months. The warranty is of 12 months."

# Regex pattern to match durations
regex = r'\b(?:(\d+)\s*weeks|(\d+)\s*months|tenure\s+of\s+(\d+)|of\s+(\d+))\b'

# Find all matches in the text
matches = re.findall(regex, text)

# Output the matches
for match in matches:
    if match[0]:
        print(f"{match[0]} weeks")
    elif match[1]:
        print(f"{match[1]} months")
    elif match[2]:
        print(f"tenure of {match[2]} months")
    else:
        print(f"of {match[3]} months")