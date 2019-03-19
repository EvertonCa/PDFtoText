import os
import PDFtoImage
import ImageToString
import Timer

# saves the desired directories addresses to string
root_directory = os.getcwd()
images_directory = root_directory + '/Images/'

# start a PDFtoImage class
pdf_manager = PDFtoImage.PDFtoImage()

# user message
input('Put all the desired .pdfs on the /PDFs folder and press ENTER.\n')

# start time
start_time = Timer.timeNow()

# all the pdfs names
all_pdfs_names = pdf_manager.pdf_files_names()

# convert all pdfs to images
pdf_manager.convert_all(all_pdfs_names)

# start a ImageToString class
image_manager = ImageToString.ImageToString(all_pdfs_names)

# convert all images to string
image_manager.convert_all()

# clean all the images folders
pdf_manager.clean_folders(pdf_manager.folder_names())

# user feedback
print('~~~~~~ DONE IN ' + str(Timer.totalTime(start_time, Timer.timeNow())) + ' ~~~~~~')
print('~~~~~~ Check the folder /Results ~~~~~~')
