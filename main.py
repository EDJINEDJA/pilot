from pilot import FeaturesSelection
import pandas as pd



if __name__ =="__main__":

    #Read the csv  file  as dataframe 
    data= pd.read_csv(filepath_or_buffer="/home/lnit/pilot/DIAGNOSES_ICD.csv" , sep = ",")
    
    parser = FeaturesSelection(data)
    print(parser.featureSelection(K  = 4, target  = "icd9_code", scale  ="StandardScaler"))
    