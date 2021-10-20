import os 
import img2pdf

with open('a.pdf','wb') as f:
    f.write(img2pdf.convert([i for i in os.listdir(files) if i.endwith(".jpg")]))