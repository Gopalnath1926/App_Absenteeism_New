import pandas as pd
import numpy as np
import pickle
import streamlit as st

  
# loading in the model to predict on the data
pickle_in = open('/model.pkl',  'rb')
model = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(age,bmi,day,disc,distance,height,hit,month,r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r21,r22,r23,r24,r25,r26,r27,r28,seasons,social_drinker,weight,wlapd):  
   
    
    ann_pred=model.predict([[age,bmi,day,disc,distance,height,hit,month,r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r21,r22,r23,r24,r25,r26,r27,r28,seasons,social_drinker,weight,wlapd]])
    

    pred=ann_pred.argmax(axis=-1)
  #  k_10=([[tp,dw,son,sd,pet,ss,weight,bmi,age,e1,e2,e3,e4,wlapd,r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r21,r22,r23,r24,r25,r26,r27,r28]])


    
    if pred == 0:
	    value = r'A$^+$'
    elif pred == 1:
        value = r'B$^+$'
   
    elif pred == 2:
        value = r'C$^+$'
    
    

    return value
      
  
def main():
      # giving the webpage a title
    #st.title("Iris Flower Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed

    html_temp = """
    <div style ="background-color:silver;padding:9px">
    <h1 style ="color:black;text-align:center;">Absenteeism Interactive Tool </h1>
    </div>
    """

    # this line allows us to display the front end aspects we have 

    st.markdown(html_temp, unsafe_allow_html = True)
    st.subheader("")       
     
if __name__=='__main__':
    main()
    
col1,col2 = st.columns(2)

    
    
with col1:
     age = st.slider("Age", 18, 60)
     bmi=st.number_input("Body mass index",step=1.,format="%.2f")
    
     day=st.number_input("Day of the week",step=1.,format="%.2f")
     
    
     disc= st.selectbox("Disciplinary failure",options=['Yes' , 'No'])
     
     
     
     disc = 0 if disc == 'No' else 1
     
     
     
     distance=st.number_input('Distance from Residence to Work(Kilometers)',step=1.,format="%.2f")
     
     height=st.number_input("Height(cm)",step=1.,format="%.2f")
    
     
     hit=st.number_input("Hit target",step=1.,format="%.2f")
    
     
    
     
     
 
with col2: 
    
    
         
     month = st.slider("Month of absence", 1, 12)
     
    
     p_class = st.selectbox("Reason of absence",options=['Abnormal clinical and laboratory findings','Blood Donation','Blood-forming organ & immune mechanism','Conditions originating in the perinatal period',  'Congenital malformations and chromosomal abnormalities','Certain infectious and parasitic diseases' , 'Dental Consultation'  ,'Diseases of the nervous system', 'Diseases of the eye and adnexa','Diseases of the ear and mastoid process','Diseases of the circulatory system', 'Diseases of the respiratory system','Diseases of the digestive system','Diseases of the skin and subcutaneous tissue', 'Diseases of musculoskeletal system & tissue', 'Diseases of the genitourinary system', 'Endocrine, nutritional and metabolic diseasess', 'External causes of morbidity and mortality', 'Factors to health status and health services',   'Injury, poisoning and consequences of external causes', 'Laboratory examination','Medical consultation','Mental and behavioural disorders',  'Neoplasms' , 'Patient follow-up',   'Physiotherapy', 'Pregnancy, childbirth and the puerperium' ])
     result =""
    

    
 
       
     r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r21,r22,r23,r24,r25,r26,r27,r28 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
     if p_class == 'Certain infectious and parasitic diseases':
	     r0 = 1
     elif p_class == 'Neoplasms':
	     r1 = 1
     elif p_class == 'Blood-forming organ & immune mechanism':
	     r2 = 1
     elif p_class == 'Endocrine, nutritional and metabolic diseasess':
	     r3 = 1
     elif p_class == 'Mental and behavioural disorders':
 	    r4 = 1
     elif p_class == 'Diseases of the nervous system':
	     r5 = 1
     elif p_class == 'Diseases of the eye and adnexa':
	     r6 = 1
     elif p_class == 'Diseases of the ear and mastoid process':
	     r7 = 1
     elif p_class == 'Diseases of the circulatory system':
	     r8 = 1
     elif p_class == 'Diseases of the respiratory system':
	     r9 = 1
    
     elif p_class == 'Diseases of the digestive system':
	      r10 = 1
     elif p_class == 'Diseases of the skin and subcutaneous tissue':
	       r11 = 1
     elif p_class == 'Diseases of musculoskeletal system & tissue':
	        r12 = 1
     elif p_class == 'Diseases of the genitourinary system':
	     r13 = 1
     elif p_class == 'Pregnancy, childbirth and the puerperium':
	     r14 = 1
     elif p_class == 'Conditions originating in the perinatal period':
       	 r15 = 1
     elif p_class == 'Congenital malformations and chromosomal abnormalities':
	     r16 = 1
         
     elif p_class == 'Congenital malformations and chromosomal abnormalities':
     	  r17 = 1
     elif p_class == 'Abnormal clinical and laboratory findings':
	     r18 = 1
     elif p_class == 'Injury, poisoning and consequences of external causes':
	      r19 = 1
     elif p_class == 'External causes of morbidity and mortality':
	      r21 = 1
     elif p_class == 'Factors to health status and health services':
	     r22 = 1
     elif p_class == 'Patient follow-up':
	     r23 = 1
     elif p_class == 'Medical consultation':
	     r24 = 1
     elif p_class == 'Blood Donation':
	     r25 = 1
     elif p_class == 'Laboratory examination':
	     r27 = 1
    
     elif p_class == 'Physiotherapy':
    	     r28 = 1

     else:
	     p_class = 1
     
    
     
    
     
    # trans=st.number_input("Transportation expense(R$)",step=1.,format="%.2f")
     seasons = st.slider("Seasons", 1, 4)
      
     social_drinker= st.selectbox("Social drinker",options=['Yes' , 'No'])
     social_drinker = 0 if social_drinker == 'No' else 1
   
     weight=st.number_input("Weight(Kg)",step=1.,format="%.2f")
#     height=st.number_input("Height",step=1.,format="%.2f")
    
    

    
     wlapd=st.number_input("Work load average/day",step=1.,format="%.4f")
  
    

      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
     if st.button("Predict"):
        result = prediction(age,bmi,day,disc,distance,height,hit,month,r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r21,r22,r23,r24,r25,r26,r27,r28,seasons,social_drinker,weight,wlapd)
     st.success('The potential candidate is classified as ---- {}'.format(result))
