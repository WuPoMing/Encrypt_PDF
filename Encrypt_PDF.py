import PyPDF2
import os

def encrypt_pdf(path, password):
    with open(path, 'rb') as f:
        pdfReader = PyPDF2.PdfFileReader(f)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        pdfWriter.encrypt(password)
        resultPdf = open('encrypted_'+path.split('\\')[-1], 'wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()

if __name__ == '__main__':
    FOLDER_PATH = r'C:\Users\wupoming\Downloads'
    PASSWARD = 'python'
    for root, dirs, files in os.walk(FOLDER_PATH):
        for file_name in files:
            if file_name.endswith('.pdf'):
                full_relative_file_name = os.path.join(root, file_name)
                print(full_relative_file_name)
                encrypt_pdf(full_relative_file_name, PASSWARD)