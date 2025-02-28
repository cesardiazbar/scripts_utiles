import os
import pypandoc

def convert_word_to_pdf(folder_path):
    if not os.path.exists(folder_path):
        print(f"La ruta {folder_path} no existe.")
        return

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.docx'):
            file_path = os.path.join(folder_path, file_name)
            pdf_path = os.path.join(folder_path, file_name.replace('.docx', '.pdf'))
            try:
                pypandoc.convert_file(file_path, 'pdf', outputfile=pdf_path)
                print(f'Convertido: {file_name} a PDF')
            except Exception as e:
                print(f'Error al convertir {file_name}: {e}')

ruta = r'C:\Users\cesar\Desktop\PADRE DUITAMA\CERTIFICACIONES'
convert_word_to_pdf(ruta)