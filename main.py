from pilot import FeaturesSelection
import pandas as pd



if __name__ =="__main__":

    #Read the csv  file  as dataframe 
    data= pd.read_csv(filepath_or_buffer="/home/lnit/pilot/DIAGNOSES_ICD.csv" , sep = ",")
    
    parser = FeaturesSelection(data)
    print(parser.CorrelationBasedFeatureSelection(treshold  = 0.95 , K=4 , scale = "default" , strategy="simple" , target="icd9_code"))
    