# This file consist of streamlit app template

# importing necessary modules
import streamlit as st
import joblib
import pandas as pd
import time
import csv

# loading model and list of symptoms
model = joblib.load("saved_model/random_f.joblib")
symptoms_list = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']

# start of streamlit UI
st.title("Oluwabukola's Health Diagnosis & Drug Recommendation Portal")
st.header("Please enter your symptoms 🩺")

symptoms = st.multiselect('Enter your symptoms so that we can get you a primary diagnosis:',[*symptoms_list],key='symptoms')

# creating dataframe for accepting testing values
prediction_value = [0 for i in range(132)]
for sym in symptoms:
	index = symptoms_list.index(sym)
	# assigning encoded value to testing frame
	prediction_value[index] = 1

# convert list to Pandas dataframe and transpose it for model evaluation
query = pd.DataFrame(prediction_value).T
prediction = model.predict(query)

# evaluation and confirmation
if st.button("Evaluate"):
	with st.spinner('Predicting output...'):
		time.sleep(1)
		if symptoms:
			st.success("Prediction complete!")
			st.write("The diagnosis we have reached is: ")
			st.error(*prediction)
			out = ""
			st.write("Searching for Drugs For The Below illness")
			out +=(prediction)
			st.error(out)

			st.write("Fetching Recommended Drugs")
			# using pandas to read normlized file
			data=[]
			with open ("Grouped_Drug_Recommendation_Normalized.csv") as csvfile:
				reader = csv.reader(csvfile)
				for row in reader:
					data.append(row)

			name = (out)

			col = [x[0] for x in data]

			if name in col:
				for x in range(0,len(data)):
					if name == data[x][0]:
						st.write(data[x])

			else:
				st.write("No Drugs found for that illness")


			st.write("Recommendation is Over, Doctor! 🏥")

		else:
			st.info("Please enter at least one symptom before clicking evaluate!")
