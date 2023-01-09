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
              
dataset was taken as it has missing values.
      This technology will help you to have you hand on features engineering and perform well the choice of prominent variables
      
"""


import numpy as nphttps://github.com/EDJINEDJA/pilot.git
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import normalize
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
        percentageMV=data.isnull().sum()/len(data)*100

        if len(NanColumns) == 0 :
            return " _______ No missing values in the data |-- {percentageMV}% missing values --|_____ "
        else : 
            text="--"
            for item in  NanColumns:
                
                text = text + item + "--"
            text 
            print( text + f" contains {percentageMV}% of missing values.")


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
           Variance tells us about the spread of the data.
           It tells us how far the points are from the mean.

           The mathematical formulation about that is the following sigma²= sum_i(xi - mean)²/n
           For example, if the integer values ​​of a variable are the same, the variance equals 0. 
           A treshold tr=0.05 allow us to benchmark and  delete low variance variable.
           The low variance variable has no impact on the target variable.
           Apply the low variance filter tries to reduce the dimensionality of the data.

           This tools helps us to know only if the data contains low variance variable 
        """

        ind_num = np.isin(data.dtypes,['int16','int32','int64','float64','float16','float32'])

        data=data.iloc[:,ind_num]

        thresholder = VarianceThreshold(threshold=threshold)

        X_high_variance = thresholder.fit_transform(data)
        
        if len(X_high_variance[0])==len(data.columns):
            return  print(" _______ No Features have low-variance _____ ")
        else :
            print(" _______ Certains Features have low-variance _____ ")

    def checkLowVarianceColumns(self, data,threshold):
        """
           This tools helps us to know the low variance variable 
        """

        ind_num = np.isin(data.dtypes,['int16','int32','int64','float64','float16','float32'])

        data=data.iloc[:,ind_num]

        Normalize = normalize(data)

        data_scaled = pd.DataFrame(Normalize)

        #storing the variance and name of variables
        variance = data_scaled.var()
        columns = data.columns

        #saving the names of variables having variance more than a threshold value
        variable = [columns[i] for i in range(0,len(variance)) if variance[i]>=threshold]

        if len(variable ) == 0:
            print("  _______ No Features have low-variance _____ ")
        else:
            print(f"_______low-variance columns : {variable}_______")

    
    def Ordinal2numerical(self,ordinalColumns,data):
        """
          It is important to know which encoder used depending on the type of categorical variable we have.
          Ordinal2numerical is used to encoder only ordinal variable:
          Indeed Ordinal variable do not have an inherent order
        """
        print("Make sure that ordinalColumns contains only ordinal variables")
        print("This tools use dummy encoder wich better than one-hot-encoding encoder")
        print("If you prefer one-hot-encoding use Ordinal2numericalBeta")
        
        columns= data.columns
        dataCategorical=pd.get_dummies(data[ordinalColumns],dummy_na=True)
        remainderV=set(columns)-set(ordinalColumns)

        return pd.concat([data[list(remainderV)],dataCategorical], axis = 1)
    
    def nominal2numerical(self,nominalColumns,data):
        """
          It is important to know which encoder used depending on the type of categorical variable we have.
          nominal2numerical is used to encoder only nominal variable:
          Indeed nominal variable have an inherent order
        """
        print("Make sure that nominalColumns contains only nominal variables")
        print("This tools use Label encoder ")

        columns= data.columns
        dataCategorical=data[nominalColumns].apply(LabelEncoder().fit_transform)
        remainderV=set(columns)-set(nominalColumns)

        return pd.concat([data[list(remainderV)],dataCategorical], axis = 1)


    def HandlMissingValues(data, delete = False, Replace = False, fill = "zero", interpolate=False):
        """
        Unprocessed data must be contain some missing values  
        Variables:
        data: dataset was taken as it has missing values.
        delete: Delete Rows with Missing Values
        Replace: Replacing With Arbitrary Value
        fill: Filling missing values with zero or backfill or forward fill 
             * fill = "zero": filling NaN values with Zero
             * fill = "forward": Filling NaN values with forward fill value
             * fill = "Backward": Filling NaN values in Backward Direction
        interpolate: Interpolation to fill missing values in series data
                -line:Linear Method
                -back:Backward Direction
                -pad:Interpolation through Padding
        """
        # delete all missing values 
        if delete:
            data = data.dropna(how='all')
        
        #  replace the missing value with some arbitrary value
        if Replace:
            #Filling missing values with 0
            if fill == "zero":
                Filling NaN values in Backward Direction
                data = data.fillna(0)

            #Filling Nan values with forward fill values
            if fill =="Forward":
                data = data.fillna(method="ffill")

            # Filling NaN values in Backward Direction
            if fill == "Backward":
                data = data.fillna(method="bfill")
            
            
        if interpolate == "line":
           data = data.interpolate(method ='linear')
        
        #  Linear Interpolation in Backward Direction
        if interpolate == "fline"
        data = data.interpolate(method ='linear', limit_direction ='forward')
        
        # Linear Interpolation in Backward Direction
        if interpolate == "bline":
           data = data.interpolate(method ='linear', limit_direction = 'backward')

        # Interpolation with Padding
        if interpolate == "pad":
           data = data.interpolate(method ='pad')
    
    return data










