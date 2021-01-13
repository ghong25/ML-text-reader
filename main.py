# main body of code to process and read text off of pdf

from PIL import Image
import pytesseract


def ocr_core(filename):
    """
    handle the processing of images
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def main():
    print(ocr_core())


main()
