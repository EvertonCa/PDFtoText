import os
import Article
import pytesseract
from PIL import Image
import pickle
from multiprocessing import Pool
from multiprocessing import cpu_count


class ImageToString:
    def __init__(self, all_pdfs_names):
        self.all_pdfs_names = all_pdfs_names
        self.root_directory = os.getcwd()
        self.images_directory = self.root_directory + '/Images/'
        self.results_directory = self.root_directory + '/Results/'

    # convert all images to strings using Tesseract and saves them as an Article object and to file
    def convert_all(self):
        os.chdir(self.images_directory)
        with Pool(cpu_count()) as p:
            p.map(self.convert_one, self.all_pdfs_names)
        os.chdir(self.root_directory)

    # convert one folder of images to string
    def convert_one(self, pdf_name):
        folder_name = pdf_name[:-4]

        os.chdir(self.images_directory + folder_name)

        temp_directory = os.getcwd()

        all_images = os.listdir(temp_directory)

        new_article = Article.Article(folder_name)

        print('~~~~~~ CONVERTING THE FILE ' + folder_name + ' TO .txt ~~~~~~')
        for page in range(len(all_images)):
            new_article.add_page(pytesseract.image_to_string(Image.open(temp_directory +
                                                                        '/Page' + str(page + 1) + '.jpg')))

        self.save_to_file(folder_name, new_article)

        os.chdir(self.images_directory)

    # saves the articles to .pkl and .txt files
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
