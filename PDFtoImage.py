from pdf2image import convert_from_path
import tempfile
import os


class PDFtoImage:
    def __init__(self):
        self.root_directory = os.getcwd()
        self.pdf_directory = self.root_directory + '/PDFs/'
        self.images_directory = self.root_directory + '/Images/'

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

                print('~~~~~~ CONVERTING THE FILE ' + folder_name + ' TO IMAGE ~~~~~~')
                for page in images_from_path:
                    page.save('Page' + str(temp_index) + '.jpg', 'JPEG')
                    temp_index += 1
                os.chdir(self.images_directory)
        os.chdir(self.root_directory)

    def pdf_files_names(self):
        all_files = os.listdir(self.pdf_directory)
        all_pdfs_names = []
        for temp_file_names in all_files:
            if temp_file_names[-4:] == '.pdf':
                all_pdfs_names.append(temp_file_names)

        return all_pdfs_names

    def folder_names(self):
        all_folders = os.listdir(self.images_directory)
        all_folders_names = []
        for temp_folder_names in all_folders:
            if temp_folder_names[0] != '.':
                all_folders_names.append(temp_folder_names)

        return all_folders_names

    def clean_folders(self, all_folders_names):
        for folder in all_folders_names:
            files_list = os.listdir(self.images_directory + folder)
            os.chdir(self.images_directory + folder)
            for file in files_list:
                os.remove(file)
            os.rmdir(self.images_directory + folder)
        os.chdir(self.root_directory)
