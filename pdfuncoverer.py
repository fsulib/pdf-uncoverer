import pypdf

def dump_coverpage_metadata(file):
  reader = pypdf.PdfReader(file)
  page1 = reader.pages[0]
  coverpage_metadata = page1
  return coverpage_metadata

def has_coverpage(file):
  reader = pypdf.PdfReader(file)
  coverpage_emails = ['mailto:lib-ir@fsu.edu', 'mailto:lib-support@fsu.edu']
  coverpage = False
  page1 = reader.pages[0]
  if '/Annots' in page1:
    for annot in page1['/Annots']:
      if '/A' in annot.get_object():
        if '/URI' in annot.get_object()['/A']:
          if annot.get_object()['/A']['/URI'] in coverpage_emails:
            coverpage = True
  return coverpage
