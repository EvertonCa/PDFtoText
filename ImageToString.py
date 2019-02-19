import os
import Article
import pytesseract
from PIL import Image
import pickle


class ImageToString:
    def __init__(self, all_pdfs_names):
        self.all_pdfs_names = all_pdfs_names
        self.root_directory = os.getcwd()
        self.images_directory = self.root_directory + '/Images/'
        self.results_directory = self.root_directory + '/Results/'

    def convert_all(self):
        os.chdir(self.images_directory)
        for pdf_name in self.all_pdfs_names:
            folder_name = pdf_name[:-4]

            os.chdir(self.images_directory + folder_name)

            temp_directory = os.getcwd()

            all_images = os.listdir(temp_directory)

            new_article = Article.Article(folder_name)

            print('~~~~~~ CONVERTING THE FILE ' + folder_name + ' TO .txt ~~~~~~')
            for page in range(len(all_images)):
                new_article.add_page(pytesseract.image_to_string(Image.open(temp_directory +
                                                                            '/Page' + str(page+1) + '.jpg')))

            self.save_to_file(folder_name, new_article)

            os.chdir(self.images_directory)
        os.chdir(self.root_directory)

    def save_to_file(self, folder_name, article):
        os.chdir(self.root_directory)
        if os.path.exists(self.results_directory):
            pass
        else:
            os.mkdir('Results')

        os.chdir(self.results_directory)

        with open(folder_name + '.pkl', 'wb') as file_output:
            pickle.dump(article, file_output, -1)

        text_file = open(folder_name + '.txt', 'w')
        for page in article.pages:
            text_file.write(page)
        text_file.close()

        os.chdir(self.root_directory)
