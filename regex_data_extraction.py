# regex_data_extraction.py
import re

# Sample text containing various data patterns
sample_text = """
Hello, my email is user@example.com and my work email is firstname.lastname@company.co.uk.
Check out these websites: https://www.example.com and https://subdomain.example.org/page
Call me at (123) 456-7890 or my other number 123-456-7890 or even 123.456.7890
Trending topics: #Programming #ThisIsAHashtag #WebDev
The product costs $19.99 and the total is $1,234.56
"""

# 1. Email Address Regex
email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# 2. URL Regex (FIXED to support special characters and optional subdomains)
url_regex = r"https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)"

# 3. Phone Number Regex (Supports various formats)
phone_regex = r"(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]?\d{4}"

# 4. Hashtag Regex
hashtag_regex = r"#[a-zA-Z0-9_]+"

# 5. Currency Amount Regex
currency_regex = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"

# Function to extract data from text using regex
def extract_data(text, regex_pattern, data_type):
    matches = re.findall(regex_pattern, text)
    print(f"Found {len(matches)} {data_type}:")
    for match in matches:
        print(f"  - {match}")
    return matches

# Extract all data types from the sample text
print("=== REGEX DATA EXTRACTION RESULTS ===")
emails = extract_data(sample_text, email_regex, "Email Addresses")
urls = extract_data(sample_text, url_regex, "URLs")
phone_numbers = extract_data(sample_text, phone_regex, "Phone Numbers")
hashtags = extract_data(sample_text, hashtag_regex, "Hashtags")
currency_amounts = extract_data(sample_text, currency_regex, "Currency Amounts")

# Test function to verify regex patterns with specific inputs
def test_regex_pattern(pattern, test_cases, data_type):
    print(f"\n=== TESTING {data_type.upper()} REGEX ===")
    for test in test_cases:
        is_match = bool(re.fullmatch(pattern, test))
        print(f'"{test}" {"MATCHES" if is_match else "DOES NOT MATCH"}')

# Test email regex
test_regex_pattern(email_regex, [
    'user@example.com', 
    'firstname.lastname@company.co.uk',
    'invalid-email',
    'missing@domain'
], "Email")

# Test URL regex
test_regex_pattern(url_regex, [
    'https://www.example.com',
    'https://subdomain.example.org/page',
    'http://example.com',
    'www.example.com' # This should not match
], "URL")

# Test phone number regex
test_regex_pattern(phone_regex, [
    '(123) 456-7890',
    '123-456-7890',
    '123.456.7890',
    '12345678' # This should not match
], "Phone Number")

# Test hashtag regex
test_regex_pattern(hashtag_regex, [
    '#example',
    '#ThisIsAHashtag',
    'example', # This should not match
    '#123'
], "Hashtag")

# Test currency regex
test_regex_pattern(currency_regex, [
    '$19.99',
    '$1,234.56',
    '19.99', # This should not match
    '$1000'
], "Currency Amount")

