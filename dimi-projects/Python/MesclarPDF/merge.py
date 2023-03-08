import pypdf, os, traceback
from tqdm import tqdm
from time import sleep

# Código para a mesclagem
error_message = traceback.format_exc()
merger = pypdf.PdfMerger()

listaPDF = os.listdir("./MesclarPDF")
finalpdf = os.listdir("./MesclarPDF/PDF-Final")
nfile = 1

for pdf in tqdm(listaPDF, desc="Progresso"):
    sleep(.1)
    if ".pdf" in pdf:
        merger.append(f"./MesclarPDF/{pdf}")

if "final.pdf" in finalpdf:
    for n in finalpdf, nfile + 1:
        merger.write(f"final({nfile}).pdf")
        shutil.move(f"/home/zero/Documents/VSCode/Project Python/final({nfile}).pdf", "/home/zero/Documents/VSCode/Project Python/MesclarPDF/PDF-Final/")
        merger.close()
else:
    merger.write("final.pdf")
    ̣̣?.move(f"/home/zero/Documents/VSCode/Project Python/final(1).pdf", "/home/zero/Documents/VSCode/Project Python/MesclarPDF/PDF-Final/")
    merger.close()

if "NoneType: None" in error_message:
    print("PDFs mesclados com sucesso.")
    print("Nenhum erro detectado.")
else:
    print(f"Ocorreu um erro durante a execução: {error_message}")

print(finalpdf)