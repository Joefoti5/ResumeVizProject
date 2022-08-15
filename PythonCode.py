#import libraries, PyPDF2 is an open-source library I use when working with PDFs/PDF transformation
import PyPDF2
#create a PDF object(binary)
pdffileobj=open(r"C:\Users\jfoti\OneDrive\Documents\\Joseph Foti Resume (Data Science).pdf",'rb')
#create pdfreader
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
#creates page object after decrypting PDF reader (ran into this issue and googled the fix, this is what I got. File is a bit odd so this helped)
#this tells the program to grab pages from document. Usually would be pdfreader.pages[x+1] but
if pdfreader.isEncrypted:
    pdfreader.decrypt('')
pageobj = pdfreader.pages[0]
#create new var that extracts text from pdf
text=pageobj.extractText()
#create new txt file from resume in 'a' mode for appending 
file1=open(r"C:\Users\jfoti\OneDrive\Documents\\Joseph Foti Resume (Data Science).txt","a")
#writes all text from file 1 (the resume) to text for parsing
file1.writelines(text)

#importing library of letters
from string import ascii_lowercase
#importing collections from Counter to count letters individually
from collections import Counter
#with statement opening resume in txt
#count characters as variable z, as long as character is in alphabet
with open(r"C:\Users\jfoti\OneDrive\Documents\\Joseph Foti Resume (Data Science).txt") as f:
         z=Counter(letter for line in f 
                  for letter in line.lower() 
                  if letter in ascii_lowercase)
                 
#plot a bar chart               
import matplotlib.pyplot as plt
#*zip(*z.most_common()) creates list of the most common values that appear, default is all values (26 here) but can change. Set width and color and plot
#* is used to unpack the list, allowing each letter to be counted on it's own away from other values
plt.bar(*zip(*z.most_common()), width=.75, color = 'r')
plt.show()                 
