import re

# Sample text
text = """
Internship Completion Certificate
this certificate is proudly awarded to
Waghmare Akash Arun

has successfully completed
4 WEEKS
of virtual/online internship program in
Java Programming at LearnSmasher EduTech LLP
during the duration/period of
30 December 2023 - 30 January 2024

We appreciate your hard work & sincerity towards your LSE's internship.
Your exemplary demonstration of required skills sets a high standard for professional achievement.
“LearnSmasher EduTech LLP” wishes you continued success in your future endeavors.
"""

# Regex pattern to match date range
date_pattern = r'period of\s+(\d{1,2} [A-Za-z]+ \d{4})\s*-\s*(\d{1,2} [A-Za-z]+ \d{4})'

# Find all matches in the text
matches = re.findall(date_pattern, text)

# Output the results
for match in matches:
    start_date, end_date = match
    print(f"Date range: From {start_date} to {end_date}")
