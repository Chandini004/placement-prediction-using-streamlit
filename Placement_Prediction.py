import streamlit as st
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv(r"C:\Users\Harshi\Downloads\collegePlace.csv")
le = preprocessing.LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['Stream'] = le.fit_transform(df['Stream'])
x = df.drop(columns=['PlacedOrNot'])
x = x.drop(columns=['Age','Hostel'])
y = df['PlacedOrNot']
rf=DecisionTreeClassifier(max_depth=6,random_state=3)
rf.fit(x,y)
def predict_place(gender,str1,interns,cgpa,backlog):	
	data=[[gender,str1,interns,cgpa,backlog]]	
	prediction=rf.predict(data)
	return prediction
def main():
	st.title("college placement")
	st.write("please enter following details:")
	str1=st.radio("select Stream:",['civil','cse','electrical','electronics and communication','it','mechanical'])
	if(str1=='civil'):
		str1=0
	elif(str1=='cse'):
		str1=1
	elif(str1=='electrical'):
		str1=2
	elif(str1=='electronics and communication'):
		str1=3
	elif(str1=='it'):
		str1=4
	elif(str1=='mechanical'):
		str1=5
	else:
		str1=6	
	cgpa=st.text_input("enter cgpa:")
	interns=st.text_input("enter previous internships:")	
	backlog=st.text_input("enter backlogs:")
	gender=st.radio("Select Gender:",('male','female'))
	if(gender=='female'):
		gender=0
	elif(gender=='male'):
		gender=1
	else:
		gender=2
	if(st.button('predict')):
		h=0
		if(str1==6):
			st.error("select Stream")
			h=1
		if(float(cgpa)>10):
			st.error("enter correct cgpa")
			h=1
		if(gender==2):
			st.error("select gender")
		if(h==0):
			p=predict_place(str1,cgpa,interns,backlog,gender)
			if(p==1):
				st.success("will be placed")
			if(p==0):
				st.warning("will not be placed")
if __name__=='__main__':
	main()
			
	
			
	