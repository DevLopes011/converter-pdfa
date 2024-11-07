import tkinter as tk
from converter import Convert

def start_conversion_images():
    converter = Convert()
    files = converter.select_files()
    
    if not files:
        return


    converter.convert_images_to_pdf(files) 
    converter.convert_pdf_to_pdfa()  

root = tk.Tk()
root.title("Conversor de Imagem para PDF/A")

convert_button = tk.Button(root, text="Converter Imagem ou PDF para PDF/A", command=start_conversion_images)
convert_button.pack(pady=20)

root.mainloop()
