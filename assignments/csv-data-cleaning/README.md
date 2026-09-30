# 📘 Assignment: CSV Data Cleaning with Python

## 🎯 Objective

Write a small Python program that cleans and validates contact records in a CSV file. Practice using the standard-library `csv` module, dictionaries, loops, and file handling without installing extra packages.

## 📝 Tasks

### 🛠️	Load and Normalize Contacts

#### Description
Read `messy_contacts.csv` with `csv.DictReader` and normalize each contact so inconsistent whitespace and letter casing do not affect the data.

#### Requirements
Completed program should:

- Read the `name`, `email`, and `city` columns from the provided CSV file.
- Remove leading and trailing whitespace from each field.
- Format names and cities in title case and convert email addresses to lowercase.


### 🛠️	Validate and Export Clean Data

#### Description
Skip incomplete contacts and repeated email addresses, then write the remaining records to `cleaned_contacts.csv` using `csv.DictWriter`.

#### Requirements
Completed program should:

- Skip a contact if its name, email, or city is empty after normalization.
- Keep only the first contact for each normalized email address.
- Write the cleaned contacts with the original `name`, `email`, and `city` column names.
- Print the number of contacts written and the number skipped.
- For the provided data, write 3 contacts and skip 3 rows.
