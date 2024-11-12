import os
import subprocess
from tkinter import messagebox
from PIL import Image

class Convert:
    def __init__(self):
        self.temp_pdf_paths = []
        self.pdf_output_path = None  
        self.file_paths = []  

    def convert_images_to_pdf(self, file_paths):
        """ Método que converte as imagens selecionadas para PDF. """
        if not file_paths:
            return
        
        for file_path in file_paths:
            if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                temp_pdf_path = os.path.splitext(file_path)[0] + "_temp.pdf"
                self.temp_pdf_paths.append(temp_pdf_path)
                
                try:
                    image = Image.open(file_path)
                    image.convert("RGB").save(temp_pdf_path)  
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao converter a imagem para PDF:\n{e}")
            else:
                self.temp_pdf_paths.append(file_path)

    def convert_pdf_to_pdfa(self):
        """ Método que converte os PDFs (temporários ou já existentes) para PDF/A. """
        if not self.temp_pdf_paths:
            messagebox.showerror("Erro", "Nenhum arquivo PDF foi encontrado para conversão.")
            return

        for temp_pdf_path in self.temp_pdf_paths:
            self.pdf_output_path = temp_pdf_path.replace(".pdf", "_output_pdfa.pdf")

            command = [
                r'C:\Program Files\gs\gs10.04.0\bin\gswin64c.exe', 
                '-dPDFA', 
                '-dNOPAUSE', 
                '-dBATCH', 
                '-sDEVICE=pdfwrite', 
                '-sOutputFile=' + self.pdf_output_path, 
                '-dPDFACompatibilityPolicy=1', 
                temp_pdf_path
            ]

            try:
                subprocess.run(command, check=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Erro", f"Erro ao converter o PDF para PDF/A:\n{e}")
            finally:
                if self.pdf_output_path:
                    os.remove(temp_pdf_path)
        messagebox.showinfo("Sucesso", f"PDF convertido para PDF/A com sucesso!\n{self.pdf_output_path}")
