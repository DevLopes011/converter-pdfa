import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class SelectFile:
    def __init__(self):
        # Definir as variáveis de estado
        self.file_paths = []

    def select_files(self):
        """ Método para selecionar arquivos (imagens ou PDFs). """
      
        root = tk.Tk()
        root.title("Conversor de Imagem para PDF/A")
        root.geometry("400x300")
        root.config(bg="#f5f5f5") 
        root.resizable(False, False)  
        

        title_label = tk.Label(root, text="Conversão de Imagens", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
        title_label.pack(pady=20)
        
        def on_convert_click():
            self.file_paths = filedialog.askopenfilenames(
                title="Selecione os arquivos", 
                filetypes=[("Arquivos", "*.jpg;*.jpeg;*.png;*.bmp;*.gif;*.pdf")]
            )
            if self.file_paths:
                messagebox.showinfo("Arquivos Selecionados", f"{len(self.file_paths)} arquivos selecionados com sucesso!")
            else:
                messagebox.showwarning("Nenhum Arquivo", "Nenhum arquivo foi selecionado.")

        convert_button = tk.Button(
            root, 
            text="Converter Imagem ou PDF para PDF/A", 
            font=("Arial", 12, "bold"), 
            bg="#4CAF50", 
            fg="white", 
            relief="raised", 
            command=on_convert_click
        )
        convert_button.pack(pady=30, ipadx=20, ipady=10)

        footer_label = tk.Label(root, text="Desenvolvido por João Alvaro Rocha Lopes", font=("Helvetica", 10), bg="#f5f5f5", fg="#777")
        footer_label.pack(side="bottom", pady=10)

        root.mainloop()

        return self.file_paths


if __name__ == "__main__":
    selector = SelectFile()
    files = selector.select_files()
    if files:
        print("Arquivos selecionados:", files)
