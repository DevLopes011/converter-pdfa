from converter import Convert
from selectFiles import SelectFile

def run():
    converter = Convert()
    selectFiles = SelectFile()
    
    files = selectFiles.select_files()
    
    if not files:
        return
    
    converter.convert_images_to_pdf(files)
    converter.convert_pdf_to_pdfa()

run()
