# PDFtoText
## About
Convert any .PDF file to a .txt file. The default recognized language is English. You must change the pytesseract
 configuration for other languages

# Installing
This program can run in **Windows, MacOS and Linux**.
You must have the following items installed in your machine:
- Python 3.6 or above
- poppler
- Google Tesseract
- pytesseract
- pillow
- pdf2image

## Installing Tesseract 4.0

Please follow the instructions from the 
**[Project Tesseract-OCR Wiki Page](https://github.com/tesseract-ocr/tesseract/wiki)**

## Installing poppler

Windows users will have to install 
**[poppler for Windows](http://blog.alivate.com.au/poppler-windows/)**
and add the `/bin/` folder to **[PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)**

Mac users will have to install **[poppler for Mac](http://macappstore.org/poppler/)** 

Linux users will have both tools pre-installed with Ubuntu 16.04+ and Archlinux. If it's not, run `sudo apt install poppler-utils`

## Installing the Python dependencies

Make sure you have **Python 3.6 or above and Pip** installed.

Install via **Pip** the following packages:

- pytesseract
- pillow
- pdf2image

# Running

Run the file Main.py by inputing to following command in the Terminal or CMD:

`python Main.py`

The program will ask you to save all the pdf files you would like to convert in the folder **/PDFs**. After doing that, 
just press **ENTER**. 

The converted **txt** files will be in the folder **/Results**
