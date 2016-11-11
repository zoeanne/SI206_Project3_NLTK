# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
from bs4 import BeautifulSoup

print('\nName: Zoe Halbeisen\nUnique name: zoeanne\nUnique ID: 84194416\nSection Day/Time: Wednesday 5:30-6:30\n')

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html' 
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

string = soup.prettify()
amazstud = string.replace("student", "AMAZING student")
amazstud2 = amazstud.replace("Student", "AMAZING Student")

amazstud3 = amazstud2.replace("logo2.png", "https://www.dropbox.com/s/2u2r3lbjmuzof5x/logo.png?dl=1")
amazstud4 = amazstud3.replace("https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg", "https://www.dropbox.com/s/n4ubyprj4gz92fv/IMG_7089.jpg?dl=1")

f = open ('alteredUMSI.html','w')
f.write(amazstud4)
f.close()