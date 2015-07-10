# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:50:29 2015

@author: student
"""

def GetWeightedAvg(DataMap, SearchDistance):
    Result = []
    for i in range(SearchDistance,len(DataMap)-SearchDistance):
        row = []        #loops thru the rows (y-coordinates)
        for j in range(SearchDistance,len(DataMap[0])-SearchDistance):
            if SearchDistance ==0:
                Center_Sq = DataMap[i][j]
                weight_center ==1
                sum_total = weight_center*Center_Sq
            elif SearchDistance ==1:
                Center_Sq = DataMap[i][j]

                Up_Sq = DataMap[i+1][j]
                Down_Sq = DataMap[i-1][j]
                Right_Sq = DataMap[i][j+1]
                Left_Sq = DataMap[i][j-1]
                SE_Sq = DataMap[i+1][j+1]
                NE_Sq = DataMap[i-1][j+1]
                SW_Sq = DataMap[i+1][j-1]
                NW_Sq = DataMap[i-1][j-1]
                weight1 = 0.0625
                weight2 = 0.5
                sum_total = weight1*(Up_Sq+Down_Sq+Right_Sq+Left_Sq+NE_Sq+NW_Sq+SE_Sq+SW_Sq) + weight2*Center_Sq
            elif SearchDistance ==2:
                Center_Sq = DataMap[i][j]

                Up_Sq = DataMap[i+1][j]
                Up2_Sq = DataMap[i+2][j]
                Down_Sq = DataMap[i-1][j]
                Down2_Sq = DataMap[i-2][j]
                
                Right_Sq = DataMap[i][j+1]
                Right2_Sq = DataMap[i][j+2]
                Left_Sq = DataMap[i][j-1]
                Left2_Sq = DataMap[i][j-2]
                
                SE_Sq = DataMap[i+1][j+1]
                SE_R_Sq = DataMap[i+1][j+2]
                SE_D_Sq = DataMap[i+2][j+1]
                SE_SE_Sq = DataMap[j+2][j+2]
            
                NE_Sq = DataMap[i-1][j+1]
                NE_R_Sq = DataMap[i-1][j+2]
                NE_U_Sq = DataMap[i-2][j+1]
                NE_NE_Sq = DataMap[i-2][j+2]
                
                SW_Sq = DataMap[i+1][j-1]
                SW_L_Sq = DataMap[i+1][j-2]
                SW_D_Sq = DataMap[i+2][j-1]
                SW_SW_Sq = DataMap[i+2][j-2]
                
                NW_Sq = DataMap[i-1][j-1]
                NW_L_Sq = DataMap[i-1][j-2]
                NW_U_Sq = DataMap[i-2][j-1]
                NW_NW_Sq = DataMap[i-2][j-2]
                
                weight1 = 0.0208
                weight2 = 0.04163
                weight3 = 0.333
                sum_1 = weight1*(Up2_Sq+Down2_Sq+Left2_Sq+Right2_Sq+SE_R_Sq+SE_D_Sq+SE_SE_Sq+NE_R_Sq+NE_U_Sq+NE_NE_Sq+SW_L_Sq+SW_D_Sq+SW_SW_Sq+NW_L_Sq+NW_U_Sq+NW_NW_Sq)
                sum_2 = weight2*(NW_Sq+SW_Sq+NE_Sq+SE_Sq+Up_Sq+Down_Sq+Left_Sq+Right_Sq)
                sum_3 = weight3*(Center_Sq)
                sum_total = sum_1+sum_2+sum_3

            #loops thru the columns (x-coordinates)
            
            row.append(sum_total)
        Result.append(row)    
        
    return Result
    
        
 def GenSOMInput():
	SOM_Input = []
	for year in range(1990,2005)
		row = []
		latIndex = LatLonIndex.findLatIndex(45,[])
		lonIndex = LatLonIndex.findLonIndex(200,[])
		data = LoadDataYear.loadDataYear(year, 'tasmax', latIndex[0], lonIndex[1])
		for day in data:
			row.append(day)
		SOM_Input.append(row)
	return np.array(SOM_Input)
    
    #different ranges (use searchdistance variable, )
    
    