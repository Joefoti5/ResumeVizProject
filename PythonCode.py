import PyPDF2
 
pdffileobj=open(r"C:\Users\jfoti\OneDrive\Documents\\Joseph Foti Resume (Data Science).pdf",'rb')

pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
if pdfreader.isEncrypted:
    pdfreader.decrypt('')
pdfreader.pages[0]
 
text=pageobj.extractText()
 
file1=open(r"C:\Users\jfoti\OneDrive\Documents\\Joseph Foti Resume (Data Science).txt","a")
file1.writelines(text)

from string import ascii_lowercase
from collections import Counter

with open(r"C:\Users\jfoti\OneDrive\Documents\\Joseph Foti Resume (Data Science).txt") as f:
         x= Counter(letter for line in f 
                  for letter in line.lower() 
                  if letter in ascii_lowercase)
                 
                 
import matplotlib.pyplot as plt

plt.bar(*zip(*x.most_common()), width=.75, color = 'r')
plt.show()                 
