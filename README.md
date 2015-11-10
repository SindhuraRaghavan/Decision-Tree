#Decision Tree
```
##Implementation of ID3 Decision Tree algorithm for classification of Cleveland's heart disease dataset for the presence or absence of heart disease.

ID3 is a greedy algorithm that constructs the decision tree by obtaining the best decision attribute at every node as the one which gives the maximum information gain

  * Entropy : The average amount of information transmitted by the random variable
  * Information Gain : Mutual information between an input attribute and target variable

  * Performance of the system is measured as the ratio of number of instances correctly classified to the total number of instances in the test dataset
```

```
##More about the Dataset : cleve_heart_disease.txt
* The complete dataset consists of 76 attributes
* We are interested in only 14 attributes of the 76 - Age, Sex, Chest pain type, Resting blood pressure, Cholesteral level, Fasting blood sugar, Resting ECG, Maximum heart rate, Angina, Oldpeak, Slope, Colored vessels, Thal, Healthy/sick
* We discretize the input attributes 
  1. Resting blood pressure (in mm Hg)
    - low : < 120
    - mid : 120 to 140 
    - high : > 140
  2. Cholesteral level (in mg/dl)
    - low : < 200
    - mid : 200 to 240
    - high : > 240
  3. Resting ECG
    - low : norm
    - mid : hyp
    - high : otherwise
  4. Maximum heart rate
    - low : < 130
    - mid : 130 to 160
    - high : > 160
  5. Oldpeak
    - low : 0
    - mid : 0 to 2
    - high : otherwise
* Training set : 80% ~ 240 samples
  Testing set : 20% ~ 63 samples
```
