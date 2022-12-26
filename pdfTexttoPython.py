# This program extracts text from a pdf and uses regular expression
# regular expression module used to find specified patterns of 
# strings
# definition high_level
import re
from pdfminer.high_level import extract_pages, extract_text

# This looks at the individual elements of the pdf
#for page_layout in extract_pages("sample.pdf"):
 #   for element in page_layout:
  #      print(element)

# This prints all of the raw text from the pdf 
# or I could use extract_pages to print each page of the pdf
text = extract_text("sample pdf")
print(text)

# This prints all the matches in the pdf that meet the criteria
# specified in the regular expression
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text)
print(matches)
names = [n[:-2] for n in matches]
print(names)

