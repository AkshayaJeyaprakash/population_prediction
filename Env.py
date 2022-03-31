import os
import warnings
warnings.filterwarnings('ignore')
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
import streamlit as st

def predict_pop(df):
    year = df['YEAR']
    pop = df['POPULATION (in millions)']
    X1 = pop.values
    train1 = X1[0:len(X1)]
    history1 = [x for x in train1]
    predictions1 = list()
    for t in range(30):
        model1 = SARIMAX(history1, order=(1, 1, 1), seasonal_order=(0,0,0,0))
        model_fit1 = model1.fit(disp=False)
        output1 = model_fit1.forecast()
        yhat1 = output1[0]
        predictions1.append(yhat1)
        history1.append(yhat1)
        st.write("\nYEAR- ",2020+t+1,' : Predicted Population = %f' % (yhat1))
    size_india = 3.2003151e+13
    BPL = 6.7
    size_per_person_BPL = 400
    size_per_person_APL = 1500
    average_story_building = 10
    percentage_buildings = 44.2
    space_occupied_null = (0.067*117 + 0.933*600)*yhat1*1000000
    space_occupied = 90*space_occupied_null/100
    length_roads = 1.6404199e+10
    width_roads = 10
    area_roads = length_roads*width_roads
    barren = 0.06*size_india
    desert = 0.05*size_india
    dump_yard = 0.1*size_india
    buildings = 0.15*size_india
    water_bodies = 0.4*size_india
    remaining_space = size_india - area_roads - barren - desert - dump_yard - space_occupied - buildings - water_bodies
    st.write("\n")
    st.header("HOW DOES THIS AFFECT ME...")
    st.write("\n")
    st.write("Total size of INDIA in sq.feet = ", size_india)
    st.write("Space taken for houses[44% buildings] in sq.feet = ", space_occupied)
    st.write("Total length of highway network in feet. = ", length_roads)
    st.write("Assuming avg. width as 10 feet, area occupied \n by roads in sq.feet = ", area_roads)
    st.write("INDIA HAS 5% OF IT'S TOTAL LAND SPAN AS DESERTS, \n6% IT AS BARREN LANDS (UNCULTIVABLE), \n 10% IS USED AS DUMP YARD, \n 40% IS COVERED BY WATER BODIES, \nAND 15% WITH EXTREME INDUSTRIAL AREAS")
    st.write("Total barren land in INDIA in sq.feet = ",barren)
    st.write("Total desert land in INDIA in sq.feet = ",desert)
    st.write("Total dump yard in INDIA in sq.feet = ",dump_yard)
    st.write("Total water bodies in INDIA in sq.feet = ",water_bodies)
    st.write("Total industrial buildings in INDIA in sq.feet = ",buildings)
    left = "Remaining space in sq.feet = " + str(remaining_space)
    st.subheader(left)
    st.image("think.PNG")
    st.subheader("will this space be enough for me and my family to live ???")
    
    


menu = ["ABOUT ME","PREDICT THE NATION"]
choice = st.sidebar.selectbox("Menu",menu)
if choice=="PREDICT THE NATION":
    st.title("PREDICT YOUR NATION FROM POPULATION")
    st.subheader("Done by: TEAM-1 [AIE'24]")
    f = st.file_uploader("Choose a csv or excel file")
    if f is not None:
        try:
            df = pd.read_excel(f)
        except:
            try:
                df = pd.read_csv(f)
            except: 
                st.warning("you need to upload a csv or excel file.")
        predict_pop(df)

elif choice =="ABOUT ME":
    st.title("PREDICT YOUR STOCK")
    st.subheader("Done by: TEAM-1 [AIE'24]")
    st.write(" ")
    st.write("THIS WEB APPLICATION WILL PREDICT THE POPULATION OF ANY GEOGRAPHICAL LOCATION FOR \nTHE NEXT 30 YEARS PROVIDED THE PROPER DATA INPUT IS GIVEN FOR PREVIOUS 100 \nYEARS [AT THE LEAST]")
    st.write(" ")
    st.write("MORE THE AMOUNT OF DATA GIVEN AS AN INPUT, MORE ACCURATE THE PREDICTIONS ARE !!! ")
    st.write(" ")
    st.write("THE HISTORY OF POPULATION MUST BE UPLADED AS .XLS OR .CSV...\nTHE .CSV OR THE .XLS FILE UPLOADED MUST STRICTLY OBEY THE FORMAT GIVEN BELOW")
    st.image("file.PNG")
