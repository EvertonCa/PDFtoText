import os
import PDFtoImage
import ImageToString

root_directory = os.getcwd()
images_directory = root_directory + '/Images/'

pdf_manager = PDFtoImage.PDFtoImage()

input('Put all the desired .pdfs on the /PDFs folder and press ENTER.\n')

all_pdfs_names = pdf_manager.pdf_files_names()

pdf_manager.convert_all(all_pdfs_names)

image_manager = ImageToString.ImageToString(all_pdfs_names)

image_manager.convert_all()

pdf_manager.clean_folders(pdf_manager.folder_names())

print('~~~~~~ DONE ~~~~~~')
print('~~~~~~ Check the folder /Results ~~~~~~')