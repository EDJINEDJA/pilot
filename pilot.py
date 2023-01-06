
""" 
   Description: 
      _____ pilot is a package that aims to perform features engineering.____
      An optimal machine learning using python can't be build without features engineering.
      What is exactlly Features Engineering? 
      In order to select prominent variables for avoid issues such as overfitting, underfitting etc
      When we build machine learning models, it is suitable to consuming little bit time on feature engineering.
      Features engineering contains numerous types of technologies:
               -Handle missing values 
               -Handle outliers
               -Remove unnecessary variables 
               -Delete low-variance variables 
               -Show Numerical and categorical variables
               -Encoding categorical variables
               -Numerical transformation 
               -Scaling numerical features 
               -Extracting of date
              

      This technology will help you to have you hand on features engineering and perform well the choice of prominent variables
      
"""

import numpy as np
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd 

class pilot( ):

    def __init__(self) -> None:
        pass

    @staticmethod
    def Columns(data):
        return data.columns

    def checkMissingValues(self, data):
        """  
            Check missing values
            What is missing values?
                Missing values can occur due to several reasons, They are the lack values inside the data
                This is due to sensor failure.
                Sometimes if there are no value we found NaN 
                They can introduce a bias in your estimates and therefore lead to erroneous conclusions.
                That is importance to know if some variable contains NaN values
        """
        columns= self.Columns()

        NanColumns =  [item for item in columns if data[item].isna().sum().sum()!=0]

        if len(NanColumns) == 0 :
            return " _______ No missing values in the data _____ "
        else : 
            text="--"
            for item in  NanColumns:
                
                text = text + item + "--"
            text 
            print( text + " contains missing values.")


    def checkDtypes(self,data):
        """
           The overall structre of data is 
               -Numerical variable
               -Categorical variable (nominal and ordinal)
                  Numerical variable have type int and float while the categorical have type string and stratified in two categories 
                   * Nominal variable and 
                   * Ordinal variable 
                      Nominal variable are the string object (leg: name of personne yes or no etc )
                      while Ordinal variable is a string wich have order relation 
            To have highlight insight of wether the variable is categoricla or numerical can help us 
            to know wich variable we are going to transform.
        """
        columns= self.Columns()

        ind_num = np.isin(data.dtypes,['int16','int32','int64','float64','float16','float32'])

        indexCV=[i for i, b in enumerate(list(ind_num)) if b==False]

        
        categoricalV= [columns[index] for index in indexCV]

        NumericalV=set(columns)-set(categoricalV)

        print(f"____Numerical variables : {list(NumericalV)} ____")
        print(f"____Numerical variables : {categoricalV} ___")

    
    def removeUnnecessaryColumns(self,data,UnnecessaryColumns):

        """
        Sometimes we quickly deduce that our data contains unnecessary variables (eg : date) and we decide to drop it.
        """

        data.drop(UnnecessaryColumns, axis=1, inplace=True)

        print("Unnecessary Columns removed")


    def checkOutliers(self, data):

        """
                Outliers values engineering 
                To determine whether the data contain outliers, we use the following techniques

                1- Z-score 
                2- Percentille 
                In our side, we use Z-score wich is formalise as follow:for each variable denote X_j we perform the mean and the variance 
                z-score of each value X_ij of X_j is: |X_ij-mean/var(Xj)|
                We use the third standard deviation as treshold
                All value which have z-score fall outside the treshold is considered to be a outlier values.
                eg: if the treshold=3 and we have the equality as follow
                z-score_ij > 3 mean that X_ij is not an outlier values.
        """
        ind_num = np.isin(data.dtypes,['int16','int32','int64','float64','float16','float32'])

        data=data.iloc[:,ind_num]

        treshold = 3

        outliersDict={keys : [item  for item in data[keys] if np.abs((item - np.mean(data[keys]))/np.std(data[keys]))>treshold] for keys in data.columns}

        outliersCol=[keys for (keys , values) in outliersDict.items() if len(values)!=0]
      

        if len(outliersCol) == 0:
            print(" _______ No outliers in the columns _____ ")
        else:
            print(f"_______outliers columns : {outliersCol}_______")

        
    def checkLowVariance(self, data,threshold):

        """
           Check low-variance features
        """

        ind_num = np.isin(data.dtypes,['int16','int32','int64','float64','float16','float32'])

        data=data.iloc[:,ind_num]

        thresholder = VarianceThreshold(threshold=threshold)

        X_high_variance = thresholder.fit_transform(data)
        
        if len(X_high_variance[0])==len(data.columns):
            return  print(" _______ No Features have low-variance _____ ")
        else :
            print(" _______ Certains Features have low-variance _____ ")

    
    def Ordinal2numericalAlpha(self,ordinalColumns,data):
        """
          It is important to know which encoder used depending on the type of categorical variable we have.
          Alpha is used to encoder only ordinal variable:
          Indeed Ordinal variable do not have an inherent order
        """
        print("Make sure that ordinalColumns contains only ordinal variables")
        print("This tools use dummy encoder wich better than one-hot-encoding encoder")
        print("If you prefer one-hot-encoding use Ordinal2numericalBeta")
        
        columns= data.columns
        dataCategorical=pd.get_dummies(data[ordinalColumns],dummy_na=True)
        remainderV=set(columns)-set(ordinalColumns)

        return pd.concat([data[list(remainderV)],dataCategorical], axis = 1)
    
    def Ordinal2numericalBeta(self,ordinalColumns,data):

        onehotencoder = OneHotEncoder(categorical_features = [0])
        X = onehotencoder.fit_transform(X).toarray()



