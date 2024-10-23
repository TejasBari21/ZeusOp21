import pandas as pan
import numpy as NuPy


DataSet = NuPy.random.randn(500)
print(DataSet)
Category = pan.cut(DataSet , 4 , precision=2)
print(Category)
pan.value_counts(Category)
print(pan.value_counts(Category))
Category_QCUT = pan.qcut(DataSet , 4 )
print(Category_QCUT)
pan.value_counts(Category_QCUT)
print(pan.value_counts(Category_QCUT))
pan.qcut(DataSet , [0.1 , 0.2,0.3,0.4])
print(pan.qcut(DataSet , [0.1 , 0.2,0.3,0.4]))
print(pan.value_counts(pan.qcut(DataSet , [0.1 , 0.2,0.3,0.4])))

DataF = pan.DataFrame(NuPy.random.randn(1000,4))
print(DataF)
Col = DataF[2]
print(Col)
Col[NuPy.abs(Col) > 3]
print(Col[NuPy.abs(Col) > 3])
DataF[(NuPy.abs(DataF) > 3).any(1)]
DataF[NuPy.abs(Col) > 3] = NuPy.sign(DataF)*3
print(DataF)
print(Col[NuPy.abs(Col) > 3])
print(Col[NuPy.abs(Col)== 3])
DataF.describe()
print(DataF)
NuPy.sign(DataF).head()
print(NuPy.sign(DataF).head())

DataF = pan.DataFrame(NuPy.arange(5*4).reshape(5,4))
print("DataSet : " , DataF)
SampleData = NuPy.random.permutation(5)
print("Permuatations : ",SampleData)
print("Data With Permutation:" , DataF.take(SampleData))
print("Display DataSet: " , DataF)
DataF.sample(n=4)
print("For n=4  : " ,DataF.sample(n=4))
SeriesObj = pan.Series([3,5,1,6,2])
print("Display Series : " , SeriesObj)
SampleSet=SeriesObj.sample(n=10 , replace=True)
print("Display SampleSet for n=20 :" , SampleSet)