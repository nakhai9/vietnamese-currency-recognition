from flask import Flask, render_template, request
import os
import cv2
import numpy as np
import pickle
import xml.etree.ElementTree as ET

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
pca = pickle.load(open('pca.pkl', 'rb'))

app.config['UPLOAD_PATH'] = 'static/upload'

def getExchangeRate(path):
     exchangeRate = []
     tree = ET.parse('exchangeRate_Vietcombank.xml')
     root = tree.getroot()
     for x in root.findall('Exrate'):
          # print(x.attrib)
          # print(type(x.attrib))
          # print(x.attrib['CurrencyCode'])
          # transfer = x.attrib['Transfer'].replace(',', '')
          # print(round(10000 / float(transfer), 4))
          exchangeRate.append(
               {
                    'CurrencyName': x.attrib['CurrencyName'].strip(),
                    'CurrencyCode': x.attrib['CurrencyCode'].strip(),
                    'CurrencyTransfer': float(x.attrib['Transfer'].replace(',', '').strip())
               }
          )
     return exchangeRate

def getCurrencyTransfer(code):
     for item in getExchangeRate('exchangeRate_Vietcombank.xml'):
          if item['CurrencyCode'] == code:
               return item['CurrencyTransfer'] 

def getCurrencyById(id):
     labels = [
          {  "id": 10, "value": "Ten Thousand Vietnam Dongs", 'denomination': 10000},
          {  "id": 20, "value": "Two Thousand Vietnam Dongs", 'denomination': 20000}, 
          {  "id": 50, "value": "Five Thousand Vietnam Dongs", 'denomination': 50000 }, 
          {  "id": 100, "value": "One Hundred Thousand VND", 'denomination': 100000}, 
          {  "id": 200, "value": "Two Hundred Thousand VND", 'denomination': 200000}, 
          {  "id": 500, "value": "Five Hundred Thousand VND", 'denomination': 500000},
     ]
     for i in labels:
          if i['id'] == id:
               return i['value'], i['denomination']

@app.route('/')
def homePage():
     return render_template('index.html', title="Thesis", currencies = getExchangeRate('exchangeRate_Vietcombank.xml'))

@app.route('/detection', methods=['POST'])
def detect():
     image = request.files['image']
     image.save(os.path.join(app.config['UPLOAD_PATH'], image.filename))

     IMAGE_SIZE = (28, 28)

     hh = app.config['UPLOAD_PATH']+'/' + image.filename

     image = cv2.imread(app.config['UPLOAD_PATH']+'/' + image.filename)
     image = cv2.resize(image, IMAGE_SIZE)
     Image = image.reshape(1, -1)

     img = Image / 255.0
     principalComponentAnalysis = pca.transform(img)
     result = model.predict(principalComponentAnalysis)

     # convert2 = [option for option in request.form.values()]
     convert2 = request.form.get('convert2').strip()


     return render_template('detection.html',
                              title = "Thesis",
                              label = getCurrencyById(result[0])[0],
                              transfer = round(getCurrencyById(result[0])[1] / (getCurrencyTransfer(convert2)), 3),
                              unit = convert2,
                              src=hh,
                              denomination = getCurrencyById(result[0])[1]
                         )

if __name__ == '__main__':
    app.run(debug= True);