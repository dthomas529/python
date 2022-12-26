# This program extract an image from a pdf using PyMuPDF, Pillow, and io
import fitz # PyMuPDF
import PIL.Image # pillow
import io # input/output module to use bites io to work 
# with the image data

pdf = fitz.open('sample.pdf')
counter = 1
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
         base_img = pdf.extract_images(image[0])
         print(base_img) # is not an image. it's meta data
         image_data = base_img["image"]
         img = PIL.Image.open(io.BytesIO(image_data))
         extension = base_img['ext']
         img.save(open(f"image{counter}.{extension}", "wb"))
         counter += 1