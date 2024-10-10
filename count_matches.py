import csv
from collections import defaultdict

# Define the file path
file_path = "results.txt"

# Open and read the file
with open(file_path, "r") as file:
    lines = file.readlines()

# Define the fixed search terms provided by the user
search_terms = [
    "domain", "referrer", "cookie", "lastModified", "readyState", "title", "dir", "body", "head", "images", "embeds",
    "plugins", "links", "forms", "scripts", "getElementsByName", "only", "open", "close", "write", "writeln",
    "defaultView", "hasFocus", "designMode", "execCommand", "queryCommandEnabled", "queryCommandIndeterm",
    "queryCommandState", "queryCommandSupported", "queryCommandValue", "hidden", "visibilityState",
    "onreadystatechange", "onvisibilitychange", "fgColor", "linkColor", "vlinkColor", "alinkColor", "bgColor",
    "anchors", "applets", "clear", "captureEvents", "releaseEvents", "all", "onabort", "onauxclick", "onbeforeinput",
    "onbeforematch", "onbeforetoggle", "onblur", "oncancel", "oncanplay", "oncanplaythrough", "onchange",
    "onclick", "onclose", "oncontextlost", "oncontextmenu", "oncontextrestored", "oncopy", "oncuechange", "oncut",
    "ondblclick", "ondrag", "ondragend", "ondragenter", "ondragleave", "ondragover", "ondragstart", "ondrop",
    "ondurationchange", "onemptied", "onended", "onerror", "onfocus", "onformdata", "oninput", "oninvalid",
    "onkeydown", "onkeypress", "onkeyup", "onload", "onloadeddata", "onloadedmetadata", "onloadstart",
    "onmousedown", "onmouseenter", "onmouseleave", "onmousemove", "onmouseout", "onmouseover", "onmouseup",
    "onpaste", "onpause", "onplay", "onplaying", "onprogress", "onratechange", "onreset", "onresize", "onscroll",
    "onscrollend", "onsecuritypolicyviolation", "onseeked", "onseeking", "onselect", "onslotchange", "onstalled",
    "onsubmit", "onsuspend", "ontimeupdate", "ontoggle", "onvolumechange", "onwaiting", "onwebkitanimationend",
    "onwebkitanimationiteration", "onwebkitanimationstart", "onwebkittransitionend", "onwheel", "implementation",
    "URL", "documentURI", "compatMode", "characterSet", "contentType", "doctype", "documentElement",
    "getElementsByTagName", "getElementsByTagNameNS", "getElementsByClassName", "createElement", "createElementNS",
    "createDocumentFragment", "createTextNode", "createCDATASection", "createComment", "createProcessingInstruction",
    "importNode", "adoptNode", "createAttribute", "createAttributeNS", "createEvent", "createRange",
    "createNodeIterator", "createTreeWalker", "activeElement"
]

# Reset counts
counts = defaultdict(int)

# Keep track of the current page
current_page_terms = set()

# Process each line in the file
for line in lines:
    # Check if a new page is found
    if line.startswith("Matches found on"):
        # Reset the current page terms for a new page
        current_page_terms = set()

    # Check for element lines
    elif "Element:" in line:
        # Extract id and name attributes
        parts = line.split(", ")
        element_values = set()
        for part in parts:
            if "id:" in part or "name:" in part:
                value = part.split(": ")[1].strip()
                if value != "No id" and value != "No name" and value in search_terms:
                    element_values.add(value)

        # Only count each element value once per page
        for value in element_values:
            if value not in current_page_terms:
                counts[value] += 1
                current_page_terms.add(value)

# Sort the counts by descending page count
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

# Write the sorted results to a CSV file
csv_file_path_sorted = "results_counts.csv"
with open(csv_file_path_sorted, mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name/ID", "Page Count"])  # Write header
    for term, count in sorted_counts:
        writer.writerow([term, count])
