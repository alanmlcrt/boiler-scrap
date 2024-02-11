import requests
from bs4 import BeautifulSoup
import csv
import time

url='https://www.helloasso.com/associations/analog-mind-fm/evenements/boiler-junia-2'
previous_label = None


while True:
    time.sleep(10)
    response=requests.get(url)

    if response.ok:
        soup= BeautifulSoup(response.text, 'lxml')
        label = soup.find('label', {'id': 'quantity-selector-label_1064351'})

        #si l'id n'existe plus :
        if label is None:
            print("Error: Label not found!")
            # conversion d'un str en attribut de text pour la suite
            class TextString:
                def __init__(self, string):
                    self.text = string
            label = TextString("ERREUR")




        with open('output.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([label.text])

            
            # Check if the label is different from the previous one
            if previous_label is not None and label.text != previous_label:
                print("Error: Label has changed!")
            elif label!="ERREUR":
                print("label toujours pareil")

            previous_label = label.text

