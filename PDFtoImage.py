from pdf2image import convert_from_path
import tempfile
import os


class PDFtoImage:
    def __init__(self):
        self.current_directory = os.getcwd()
        self.pdf_directory = self.current_directory + '/PDFs/'
        self.images_directory = self.current_directory + '/Images/'

        if os.path.exists(self.pdf_directory):
            pass
        else:
            os.mkdir('PDFs')

        if os.path.exists(self.images_directory):
            pass
        else:
            os.mkdir('Images')

    def convert_all(self, all_pdfs_names):
        os.chdir(self.images_directory)
        for pdf_name in all_pdfs_names:
            with tempfile.TemporaryDirectory() as path:
                images_from_path = convert_from_path(self.pdf_directory + pdf_name, output_folder=path)
                temp_index = 1

                folder_name = pdf_name[:-4]

                if os.path.exists(self.images_directory + folder_name):
                    pass
                else:
                    os.mkdir(folder_name)

                os.chdir(self.images_directory + folder_name)
                for page in images_from_path:
                    page.save('Page' + str(temp_index) + '.jpg', 'JPEG')
                    temp_index += 1
                os.chdir(self.images_directory)
        os.chdir(self.current_directory)

    def files_names(self):
        all_files = os.listdir(self.pdf_directory)
        all_pdfs_names = []
        for temp_file_names in all_files:
            if temp_file_names[-4:] == '.pdf':
                all_pdfs_names.append(temp_file_names)

        return all_pdfs_names

i = PDFtoImage()
i.convert_all(i.files_names())


