import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    
    cols =["SCH_ENR_HI_M", "SCH_ENR_HI_F", "SCH_ENR_AM_M", "SCH_ENR_AM_F", "SCH_ENR_AS_M", "SCH_ENR_AS_F", "SCH_ENR_HP_M", "SCH_ENR_HP_F", "SCH_ENR_BL_M", "SCH_ENR_BL_F", "SCH_ENR_WH_M", "SCH_ENR_WH_F", "SCH_ENR_TR_M", "SCH_ENR_TR_F"]
    
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    
    sums = {}
    
    for col in cols:
        sums[col] = data[col].sum()
        
    all_enrollment = data["total_enrollment"].sum()
    
    gender_race_perc = {}
    
    for col in cols:
        gender_race_perc[col] = (sums[col]*100) / all_enrollment
        
    counter = int()
    
    for keys,values in gender_race_perc.items():
        print(keys)
        print(values)