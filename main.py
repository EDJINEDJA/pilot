from pilot import featuresSelection
import pandas as pd

import pandas as pd


if __name__ =="__main__":

    #Read the csv  file  as dataframe 
    data= pd.read_csv(filepath_or_buffer="/home/lnit/pilot/DIAGNOSES_ICD.csv" , sep = ",")
    
    parser = featuresSelection(data)
    parser.RecursiveFeatureElimination(target = 'icd9_code' , K=4)
    


   