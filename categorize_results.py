import csv
from collections import defaultdict

# Define the file path
file_path = "results.txt"

# Open and read the file
with open(file_path, "r") as file:
    lines = file.readlines()

# Define the fixed search terms provided by the user
matches = {
  "hidden": {},
  "body": {},
  "cookie": {},
  "title": {},
  "head": {},
  "links": {},
  "domain": {},
  "images": {},
  "all": {},
  "forms": {},
}

search_terms = matches.keys()

# Process each line in the file
url = None
for line in lines:

    # Check if a new page is found
    if line.startswith("Matches found on"):
        # Reset the current page terms for a new page
        url = line.removeprefix("Matches found on ").strip()

    # Check for element lines
    elif "Element:" in line:
        # Extract element + id and name attributes
        parts = line.split(", ")
        element_values = {}
        for part in parts:
            value = part.split(": ")[1].strip()
            if "Element:" in part:
                element_values["element"] = value
            if "id:" in part:
                if value != "No id" and value in search_terms:
                    element_values["id"] = value
            if "name:" in part:
                if value != "No name" and value in search_terms:
                    element_values["name"] = value

        strippedLine = line.removeprefix(" - ").strip()
        if "name" in element_values:
            if url in matches[element_values["name"]]:
                matches[element_values["name"]][url].append(strippedLine)
            else:
                matches[element_values["name"]][url] = [strippedLine]
        else:
            if url in matches[element_values["id"]]:
                matches[element_values["id"]][url].append(strippedLine)
            else:
                matches[element_values["id"]][url] = [strippedLine]

# Write the sorted results to a CSV file
csv_file_path = "results_categorized.csv"
with open(csv_file_path, mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Document property", "url", "elements"])  # Write header
    for term in matches:
        for url in matches[term]:
            writer.writerow([term, url, ", ".join(matches[term][url])])
