import csv
from pathlib import Path

FIELDNAMES = ["name", "email", "city"]
ASSIGNMENT_DIR = Path(__file__).resolve().parent
INPUT_FILE = ASSIGNMENT_DIR / "messy_contacts.csv"
OUTPUT_FILE = ASSIGNMENT_DIR / "cleaned_contacts.csv"


def normalize_contact(row):
    # TODO: Return a new contact with trimmed fields, title-case name and city,
    # and a lowercase email address.
    pass


def is_valid_contact(contact):
    # TODO: Return True only when name, email, and city are all non-empty.
    pass


def clean_contacts():
    cleaned_contacts = []
    seen_emails = set()
    skipped_count = 0

    with INPUT_FILE.open("r", newline="", encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            contact = normalize_contact(row)

            if not is_valid_contact(contact):
                skipped_count += 1
                continue

            if contact["email"] in seen_emails:
                skipped_count += 1
                continue

            # TODO: Track this email and add the contact to cleaned_contacts.
            pass

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(cleaned_contacts)

    print(f"Contacts written: {len(cleaned_contacts)}")
    print(f"Rows skipped: {skipped_count}")


if __name__ == "__main__":
    clean_contacts()
