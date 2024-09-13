import pypdf

def get_first_line(file):
  reader = pypdf.PdfReader(file)
  page1 = reader.pages[0]
  page1text = page1.extract_text()
  first_line = page1text.splitlines()[0]
  first_line_sanitized = first_line \
    .replace(')', '')               \
    .replace('/', '')               \
    .replace('\\', '')              \
    .replace('\x03', '') 
  return first_line_sanitized

def has_fsul_coverpage(file):
  first_line = get_first_line(file)
  fsul_coverpage_first_lines = ['Florida State University', 'Florida State University Libraries', 'ORULGD6WDWH8QLYHUVLWLEUDULHV']
  if first_line in fsul_coverpage_first_lines:
    coverpage = True
  else:
    coverpage = False
  return coverpage
