# import pandas as pd
# df = pd.read_excel('C:/Users/shamu/Downloads/3020 (EMSL)_kW.xlsx', header=None)
# counter=0
# #copying the first column to the third one
# df[3]=df[1]
# df[3].iloc[0]="NEW DATA_NO NAN"
# #extract the numbers of rows form a tuple
# dimensions = df. shape
# selected_elements = [dimensions[index] for index in range(0,2)]
# #
# while(counter<selected_elements[0] and str(df[1].iloc[counter]).isalnum):
#     if(str(df[1].iloc[counter]).isalpha()):
#         df[3].iloc[counter]=0
#         print(counter,"------------",0)
#     counter+=1
#     #print(counter)
# #################################################################
# df.to_excel('C:/Users/shamu/Downloads/data_3020 (EMSL)_newData_no_NAN.xlsx')
# #

import pandas as pd
table=pd.read_csv("./dataset/Phase#1_data/room_unavailable.csv",header=None)
counter=0
deleted=0
#extract the numbers of rows form a tuple
dimensions = table.shape
selected_elements = [dimensions[index] for index in range(0,2)]
#
while(counter<selected_elements[0]-counter):
    if(str(table[0].iloc[counter])=="nan" or str(table[1].iloc[counter])=="nan" or str(table[3].iloc[counter])=="nan"):
        table.drop(index=deleted+counter, inplace=True)
        print(counter,"------------",0)
        deleted+=1
    counter+=1
    #print(counter)
table.to_excel('C:/Users/shamu/Downloads/room_unavailable_NEW.xlsx')
