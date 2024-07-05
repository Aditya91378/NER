import re

# Sample text
text = '''This is to certify that

VISHAKHA SANJEEV SHINDE (Intern)
has successfully completed a 12-week Artificial Intelligence and Machine Learning Virtual Internship program
during the period of January to March 2024.
This internship was offered by Google for Developers in collaboration with International Institute of Information Technology (IAIT).
Dr. Satya Ranjan Biswas
Professor, Department of Computer Science
International Institute of Information Technology (IAIT)'''
# Regex pattern
pattern = r'Dr\.\s+([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)'
pattern1 = r'(\b\w+(?:\s\w+)*)\s(?:Inc\.\s)?(?:Pvt\s(?:Ltd)?\b)?(?:Offered\sby\s)?(?:Ltd|Corp\b)'

# Find all matches
matches = re.findall(pattern, text)

# Print the matches
for match in matches:
    print(f"Found: {match}")
    
    
    
# ^: This is the start-of-string anchor. It ensures that the regex matches the pattern from the beginning of the string.
# Dr\.: This matches the "Dr." prefix literally. The backslash \ is used to escape the period ., which is a special character in regex.
# \s+: This matches one or more whitespace characters (space, tab, newline, etc.) after the "Dr.".
# ([A-Z][a-z]+(\s[A-Z][a-z]+)*): This is the capturing group that matches the name (proper noun):
# [A-Z]: Matches a capital letter.
# [a-z]+: Matches one or more lowercase letters.
# (\s[A-Z][a-z]+)*: Matches zero or more occurrences of a space followed by a capital letter and one or more lowercase letters (for multi-word names).
# $: This is the end-of-string anchor. It ensures that the regex matches the pattern only if it's at the end of the string.