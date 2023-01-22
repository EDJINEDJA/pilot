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


import numpy as np #https://github.com/EDJINEDJA/pilot.git
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import normalize
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

       
import pandas as pd 
import numpy as np
from typing import List

from prettytable import PrettyTable

class featuresSelection():
    def __init__(self , data : pd.core.frame.DataFrame) -> None:
        
        #Initialization
        self.data  =  data
        self.columns =data.columns


    @staticmethod
    def encode_data( data : pd.core.frame.DataFrame):
        """
           Define a function to encode the data
        """

        for column in data.columns:
            if data[column].dtype == 'object':
                data[column] = pd.Categorical(data[column]).codes

        return data


    def checkLowVariance(self, threshold : str = 0.05):

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
        # A copy of principal data

        data = self.data.copy()

        ind_num = np.isin(data.dtypes,['int16','int32','int64','float64','float16','float32'])

        data=data.iloc[:,ind_num]

        thresholder = VarianceThreshold(threshold=threshold)

        X_high_variance = thresholder.fit_transform(data)
        
        if len(X_high_variance[0])==len(data.columns):
            strLen = len("  _______ No Features have low-variance _____ ")
            print("+" + strLen * "-" + "+")
            print(" _______ No Features have low-variance _____ ")
            print("+" + strLen * "-" + "+")

        else :
            strLen = len(" _______ Certains Features have low-variance _____ ")
            print("+" + strLen * "-" + "+")
            print(" _______ Certains Features have low-variance _____ ")
            print("+" + strLen * "-" + "+")

    def checkLowVarianceColumns(self, threshold):
        """
           This tools helps us to know the low variance variable 
        """
        # A copy of principal data

        data = self.data.copy()

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
            strLen = len("  _______ No Features have low-variance _____ ")
            print("+" + strLen * "-" + "+")
            print("  _______ No Features have low-variance _____ ")
            print("+" + strLen * "-" + "+")
        else:
            strLen = len("_______low-variance columns : {variable}_______")
            print("+" + strLen * "-" + "+")
            print(f"_______low-variance columns : {variable}_______")
            print("+" + strLen * "-" + "+")


    def CorrelationBasedFeatureSelection(self, treshold : float = 0.95 ):

        """
            Correlation-based feature selection
            Sometimes we quickly deduce that our data contains unnecessary variables (eg : date) and we decide to drop it.
        """
        # copy the dataframe
        data = self.data.copy()

        # Calculate the correlation matrix
        corr_matrix = data.corr()

        # Select upper triangle of correlation matrix
        upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

        # Find index of feature columns with correlation greater than a threshold (e.g. 0.95)
        to_drop = [column for column in upper.columns if any(upper[column] > treshold)]

        # Drop the correlated columns from the DataFrame
        data.drop(data[to_drop], axis=1 , inplace = True)

        # Remainder comlumns 
        remainderColumns = set(self.columns)-set(data.columns)
      
        # Create a new table
        table = PrettyTable()

        # Create a list of dictionaries representing rows
        rows = []

        for item in remainderColumns:
            rows.append({"Unnecessary features" : item})
    
        # Define the column headers
        table.field_names = ['Unnecessary features']

        # Add some rows to the table
        
        # Use a for loop to add rows to the table
        for row in rows:
            table.add_row([row['Unnecessary features']])
        # string len 
        strLen = len(" ../ Unnecessary features such as: { remainderColumns } have/has been removed.")
        
        # Print the table
        print("+" + strLen * "-" + "+")
        print(data.head(4))
        print("+" + strLen * "-" + "+")
        print(f" ../ Unnecessary features such as: { remainderColumns } have/has been removed." )
        print("+" + strLen * "-" + "+")
        print(table)
       
        return data

    def UnivariateFeatureSelection(self , target : str , K : int , strategy : str = "default"):
        """
           This method uses statistical tests to select the best features based on their individual relevance to the target variable
        """
        # Reset K value if it is less than 0 and greater than len(self.columns)
        if K < 0 or K > len(self.columns)-1:
            K = "all"

        # Load data
        data =  self.encode_data(self.data)
       
        if strategy == "default" or "StandardScaler":
                # Instantiate the StandardScaler
                scaler = StandardScaler()

                # Scale the data
                X= scaler.fit_transform(X)
        elif strategy == "MinMaxScaler":
                # Instantiate the MinMaxScaler
                scaler = MinMaxScaler(feature_range=(0, 1))

                # Scale the data
                X = scaler.fit_transform(X)
        else:
                # Instantiate the MaxAbsScaler
                scaler = MaxAbsScaler()

                # Scale the data
                X = scaler.fit_transform(X)


        y = np.array(data[target])

        
        # Select the top K features
        
        selector = SelectKBest(f_regression, k=K).fit(X, y)
        X_new = selector.transform(X)

        return X_new

    def  RecursiveFeatureElimination(self  , target : str , K : int , strategy : str = "default"):

        """
           This method uses a model to recursively remove features, building the model with the remaining features at each iteration.
        """
        # Reset K value if it is less than 0 and greater than len(self.columns)
        if K < 0 or K > len(self.columns):
            K = len(self.columns)-1

        #Encode the data using encode_data function
        data =  self.encode_data(self.data)
       
        X = np.array(data.drop(target, axis=1))

        if strategy == "default" or "StandardScaler":
            # Instantiate the StandardScaler
            scaler = StandardScaler()

            # Scale the data
            X= scaler.fit_transform(X)
        elif strategy == "MinMaxScaler":
            # Instantiate the MinMaxScaler
            scaler = MinMaxScaler(feature_range=(0, 1))

            # Scale the data
            X = scaler.fit_transform(X)
        else:
            # Instantiate the MaxAbsScaler
            scaler = MaxAbsScaler()

            # Scale the data
            X = scaler.fit_transform(X)

        y = np.array(data[target])

        # Select the top K features using RFE
        rfe = RFE(estimator=LogisticRegression(), n_features_to_select=K)
        X_new = rfe.fit_transform(X, y)
        
        return X_new


        
    



class pilot( ):

    def __init__(self , data : pd.core.frame.DataFrame) -> None:
        
        #Initialization
        self.data  =  data
        self.columns =data.columns


    def checkMissingValues(self):
        """  
            Check missing values
            What is missing values?
                Missing values can occur due to several reasons, They are the lack values inside the data
                This is due to sensor failure.
                Sometimes if there are no value we found NaN 
                They can introduce a bias in your estimates and therefore lead to erroneous conclusions.
                That is importance to know if some variable contains NaN values
        """

        NanColumns =  [item for item in self.columns if self.data[item].isna().sum().sum()!=0]
        percentageMV=self.data.isnull().sum()/len(self.data)*100

        if len(NanColumns) == 0 :
            return " _______ No missing values in the data |-- {percentageMV}% missing values --|_____ "
        else : 
            text="--"
            for item in  NanColumns:
                
                text = text + item + "--"
            text 
            print( text + f" contains {percentageMV}% of missing values.")


    def checkDtypes(self):
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

        ind_num = np.isin(self.data.dtypes,['int16','int32','int64','float64','float16','float32'])

        indexCV=[i for i, b in enumerate(list(ind_num)) if b==False]

        
        categoricalV= [self.columns[index] for index in indexCV]

        NumericalV=set(self.columns)-set(categoricalV)

        print(f"____Numerical variables : {list(NumericalV)} ____")
        print(f"____Categorical variables : {categoricalV} ___")




    def checkOutliers(self, strategy : str = "default"):

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
        data=self.data.iloc[:,ind_num]
        
        if len(self.columns) != len(ind_num) :
            raise "../ warning: detects categorical variables and does not take care of them."
       
        if strategy == "default":

            treshold = 3

            outliersDict={keys : [item  for item in data[keys] if np.abs((item - np.mean(data[keys]))/np.std(data[keys]))>treshold] for keys in data.columns}

            outliersCol=[keys for (keys , values) in outliersDict.items() if len(values)!=0]
        

            if len(outliersCol) == 0:
                print(" _______ No outliers in the columns _____ ")
            else:
                print(f"_______outliers columns : {outliersCol}_______")

        
    
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


    def HandlMissingValues(self, data , scalar = None , strategy = "default"):
        """
        Unprocessed data must be contain some missing values  
        Variables:
        data: dataset was taken as it has missing values.
        strategy = "default" ---> Delete Rows with Missing Values
        strategy = "replace" ---> Replacing With Arbitrary Value

        fill: Filling missing values with zero or backfill or forward fill 
        strategy = "fill_zero" ---> filling NaN values with Zero
        strategy = "fill_forward" ---> Filling NaN values with forward fill value
        strategy = "fill_backward"  ---> Filling NaN values in Backward Direction

        interpolate: Interpolation to fill missing values in series data
                -line:Linear Method
                -back:Backward Direction
                -pad:Interpolation through Paddingion to fill missing values in series data
        strategy = "interpolate_line"  ---> Linear Method
        strategy = "interpolate_line"  ---> forward Method
        strategy = "interpolate_bline"  ---> Backward Direction
        strategy = "interpolate_pad"  ---> Interpolation through Padding
        
        """
        # delete all missing values 
        if strategy == "default":
            data = data.dropna(how='all')
        
        #  replace the missing value with some arbitrary value
        #Filling missing values with a scalar
        if strategy == "fill_scalar": 
            data = data.fillna(scalar)

        #Filling Nan values with forward fill values
        if strategy == "fill_forward":
            data = data.fillna( method="ffill")

        # Filling NaN values in Backward Direction
        if strategy == "fill_backward":
            data = data.fillna(method="bfill")
        
        #  Interpolation to fill missing values in series data  
        if strategy =="interpolate_line":
           data = data.interpolate(method ='linear')
        
        #  Linear Interpolation in forward Direction
        if strategy =="interpolate_fline":
            data = data.interpolate(method ='linear', limit_direction ='forward')
        
        # Linear Interpolation in Backward Direction
        if strategy =="interpolate_bline":
           data = data.interpolate(method ='linear', limit_direction = 'backward')

        # Interpolation with Padding
        if strategy == "interpolate_pad":
           data = data.interpolate(method ='pad')
    
        return data
