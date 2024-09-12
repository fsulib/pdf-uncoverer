from pypdf import PdfReader

def has_coverpage(file):
  reader = PdfReader(file)
  coverpage = False
  page1 = reader.pages[0]
  if '/Annots' in page1:
    for annot in page1['/Annots']:
        if annot.get_object()['/A']['/URI'] == 'mailto:lib-ir@fsu.edu':
            coverpage = True
  return coverpage
