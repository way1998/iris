# Iris
This is a python program that parses the CSV of Iris data from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data, computes the average sepal length and petal length for each iris class, prints out the result and generates a chart of it.

## Prerequisites
This program is implemented using python 3.6.1 and the following packages:
* pandas - to read csv from url
* matplotlib, numpy - to generate the chart  
Please install these packages before running.  
Note that the matplotlib requires a python version >= 3.5

## Running the program
If your have done the installation properly, then you can simply run this program by:
```
python iris.py
```
Then it will print out the averages like:
```
Average petal length: 
Iris-setosa: 1.4653061224489796
Iris-versicolor: 4.26
Iris-virginica: 5.552
```
And generate a chart like:  
![Alt text](/images/sepal_length_and_petal_length.png?raw=true "sepal length and petal length")
