# Vietnamese Currency Recognition

## Overview

Nowadays, banknotes are a major instrument of our transactions. For foreign tourists coming to Vietnam, they are often worried because they don’t know clearly how much the banknote is worth compared to their country's currency or to the common currency as USD, which causes difficulties in the transaction process. Therefore, it is very necessary to build an application program to recognize Vietnamese banknotes. The system uses image feature extraction by principal component analysis (PCA) in combination with support vector machine (SVM) algorithms to build a banknote classification model. We build a model using a radial basis function (Radial Basis Function - RBF) and a polynomial function (Poly). We evaluate the results as accuracy and training time and compare two models to choose the best one. Then display the denomination and equivalent banknote value. Experiments show that the Vietnamese currency recognition system using the radial basis function (RBF) gives an accuracy of 64.24%.

## Vietnamese Banknote Images Dataset

### Data Set information:

- This is a Vietnamese banknote images data set. Each image have size of 28x28 pixel. Image format is used RGB.
- The data set contains 6 classes of 150-156 KVinstances each, where refer to a type of Vietnamese currency.
- Predicted attribute: class of Vietnamese Currency.

### Attribute information:
     There are 6 classes such as:

     | Ord | Label                               | Denomination |
     | --- | ----------------------------------- | ------------ |
     | 1   | Ten thousand Vietnam Dongs          | 10,000       |
     | 2   | Two thousand Vietnam Dongs          | 20,000       |
     | 3   | Five thousand Vietnam Dongs         | 50,000       |
     | 4   | One hundred thousand Vietnam Dongs  | 100,000       |
     | 5   | Two hundred thousand Vietnam Dongs  | 200,000       |
     | 6   | Five hundred thousand Vietnam Dongs | 500,000       |

### Example: [All images](https://github.com/nguyenanhkhai/Vietnamese-Currency-Recognition/tree/master/assets)

![image](/screenshot/datasetExample.png)

### Download or discover dataset: [Discover here.](https://raw.githubusercontent.com/nguyenanhkhai/Vietnamese-Currency-Recognition/master/dataset/RGB.csv)

## Installation

We required Python > 3.8.x to run 

```sh
git clone https://github.com/nguyenanhkhai/Vietnamese-Currency-Recognition.git

cd Vietnamese-Currency-Recognition

cd app

python app.py
```
Then open [http://localhost:5000](http://localhost:5000) to view it in the browser.

Use the images on [**Test**](https://github.com/nguyenanhkhai/Vietnamese-Currency-Recognition/tree/master/test) 

Or take a photo from your phone as template below.
![image](https://github.com/nguyenanhkhai/Vietnamese-Currency-Recognition/blob/master/test/Ti%E1%BB%81n%20ch%E1%BB%A5p%20t%E1%BB%AB%20%C4%91i%E1%BB%87n%20tho%E1%BA%A1i/Nh%E1%BA%ADn%20d%E1%BA%A1ng%20%C4%91%C3%BAng/200_f0.jpg?raw=true)

## Development Steps

- Step 1: Collects and makes a dataset.
- Step 2: Preprocessing data.
- Step 3: Build a model.
- Step 4: Prediction.

## Technologies Used

- OpenCV.
- Principal Components Analysis (PCA).
- Support Vector Machine (SVM).
- Micro Web Framework: Flask.

## Author

Student: Nguyen Anh Khai. [Contact with me via email](anhkhainguyen9@gmail.com) or [Phone](0945757051)

Instructor: Master Le Thi Phuong Dung. [Contact with her via email](ltpdung@cit.ctu.edu.vn) 

Copyright 12/2021 Nguyen Anh Khai.
