# main body of code to process and read text off of pdf

from PIL import Image
import sys
import os
from pdf2image import convert_from_path
import pytesseract


def ocr_core(filename):
    """
    handle the processing of images
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text

def write_to_txt(text, filename=None):
    """
    take in string processed by pytesseract and output to txt file. default file name is text.txt. Optional keyword for
    specifying file name
    """
    file = filename + '.txt'
    with open(file, 'w') as f:


def pdf_to_image(pdf_file):
    """"
    Given the path of pdf_file, first convert to JPG, then translate to text. Export txt file of the text
    """

    # variable containing all pages of the PDF
    pages = convert_from_path(pdf_file, 500)

    # counter to store images of each page of PDF to image
    image_counter = 1

    for page in pages:
        # file name for each page of PDF as JPG, e.g. page_1.jpg, page_2.jpg
        file = f"page_{image_counter}.jpg"

        page.save(file, 'JPEG')
        image_counter += 1

    output = 'text.txt'

    # open the file in append mode so all contents of all images are added to the same file
    f = open(output, 'a')

    for i in range(1, image_counter):
        file = f"page_{i}.jpg"
        text = pytesseract.image_to_string(Image.open(file))
        text = text.replace('-\n', '')

        f.write(text)
    f.close()



def main():

    pdf_path = "_"

    # path of the file
    print(ocr_core(''))


main()
