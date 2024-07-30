import pandas as pd;
#TO check version of panda
# print(pd.__version__);
#To get help 
# help(pd);
#To read data form csv file
data = pd.read_csv("C:\\Users\\Ruddarm\\Downloads\\PandasLearning\\PandasTutorial\\Employee.csv");
#Head function i will print frist n number of rows by default it value is 5
print("First 5 rows \n",data.head())
#or we can change the defualt value 
print("First 2 rows \n ",data.head(2))
#Tail funciton is use to get data from last n rows  by default value is 5
print("last 5 Rows \n",data.tail())
#we can change defualt value 
print("last 3 Rows : \n",data.tail(3))
#get Column Names
print("*****Data columns are******* \n",data.columns)
#get Index value
print("****Data index : ",data.index)
#get info
print("***Data info is **** \n",data.info())
#describe
print("****Data Descripsion is ****\n",data.describe())
#type of data in pandas
print(data)
