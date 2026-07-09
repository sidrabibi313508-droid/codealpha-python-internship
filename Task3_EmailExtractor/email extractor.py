"""
Task 3: Email Extractor
------------------------
Reads a .txt file, finds all email addresses using regex,
and saves them into a new .txt file (duplicates removed).

Usage:
    python email_extractor.py input.txt output.txt
"""

import re
import sys
import os


EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails(input_file: str, output_file: str) -> int:
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found.")
        return 0

    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    emails = re.findall(EMAIL_PATTERN, content)
    unique_emails = sorted(set(emails))  # remove duplicates, sort alphabetically

    with open(output_file, "w", encoding="utf-8") as f:
        for email in unique_emails:
            f.write(email + "\n")

    return len(unique_emails)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
    else:
        # Default filenames if run without command-line arguments
        input_path = "input.txt"
        output_path = "emails_found.txt"

    count = extract_emails(input_path, output_path)
    print(f"Done. {count} unique email(s) saved to '{output_path}'.")