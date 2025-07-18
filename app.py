import streamlit as st
import pandas as pd
import numpy as np
import wget
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



url='https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/839/original/Jamboree_Admission.csv'
file=wget.download(url)
df=pd.read_csv(file)
df.rename({'LOR ':'LOR','Chance of Admit ':'Chance of Admit'},inplace=True,axis=1)

st.title('Jamboree Education Analyser')
st.write("This analysis is aimed to help Jamboree in understanding what factors are important in graduate admissions and how these factors are interrelated among themselves. The correlation of different factors with the target variable are to be analysed as well as between different variables. The relation can be verified by formulating a Linear Regression model using the variables. It will also help predict one's chances of admission given the rest of the variables")

fig, axs = plt.subplots(1, 3, figsize=(10, 4))
# Plot GRE Score distribution
sns.histplot(df['GRE Score'], ax=axs[0], kde=True)
axs[0].set_title('GRE Score Distribution')

# Plot TOEFL Score distribution
sns.histplot(df['TOEFL Score'], ax=axs[1], kde=True)
axs[1].set_title('TOEFL Score Distribution')
#plot cgpa
sns.histplot(df['CGPA'], ax=axs[2], kde=True)
axs[2].set_title('CGPA Distribution')

plt.tight_layout()
st.pyplot(fig)

fig2, axs2 = plt.subplots(1, 1, figsize=(10, 5))
sns.distplot(df['Chance of Admit'])
axs2.set_title('Chance of Admit Distribution')
st.pyplot(fig2)


#Data preparation
y=df['Chance of Admit']
X=df.drop(['Chance of Admit','Serial No.'],axis=1)
# scaler=StandardScaler()
# X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

#train-test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

#model building
st.subheader("Linear Regression Model")
st.write("Linear Regression Model is chosen to train on the dataset to predict the Chance of Admittance")
model=LinearRegression()
model.fit(X_train,y_train)

#Model coefficients

zipped=list(zip(X_train.columns,np.round(model.coef_,4)))
x_vals,y_vals=zip(*zipped)
fig3, axs3 = plt.subplots(figsize=(10, 5))
plt.bar(x_vals, y_vals, color='skyblue')
axs3.set_title('Model Coefficients')
axs3.set_xlabel('Coefficient')
axs3.set_ylabel('Weightage')
st.pyplot(fig3)

st.write("*   CGPA is the most impactful factor in deciding the chance of admittance.  ")
st.write("*   GRE and TOEFL scores have similar positive correlation with chance of admittance.")
st.write("*   Letter of Recommendation Strength and Research experience have positive correlation with chance of admittance.")
st.write("*   University rating  has weak and positive correlation with the chance of admittance.")
st.write("*   Statement of Purpose Strength have a weak and negative correlation with chance of admittance.")

#Predicting Chance of Admittance
st.title("Chance of Admit Predictor")
col1,col2=st.columns(2)
with col1:
    GRE=st.number_input("GRE Score (in 340) :", min_value=0.0,max_value=340.0,step=5.0)
with col2:
    TOEFL=st.number_input("TOEFL Score (in 120):",min_value=0.0,max_value=120.0,step=5.0)
col3,col4=st.columns(2)
with col3:
    LOR = st.slider("Letter of Recommendation Strength :", 0, 5, 1)
with col4:
    SOP=st.slider("Statement of Purpose Strength :", 0,5,1)
Uni=st.slider("University Rating :", 0,5,1)
GPA=st.slider("Undergraduate GPA  :",0.0,10.0,0.5)
Res= int( st.toggle("Research experience :"))
if(st.button("Predict Chance")):
    value=np.array([GRE,TOEFL,Uni,SOP,LOR,GPA,Res]).reshape(1,-1)
    COA=model.predict(value)[0]*100
    st.text(f"Chance of Admit is {COA.round(2)}%")
