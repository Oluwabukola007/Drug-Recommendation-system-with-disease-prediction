# This file consist of streamlit app template

# importing necessary modules
import streamlit as st
##import joblib
import pandas as pd
import time
import csv
import sys


disease_list = ['condition', 'ADHD', 'AIDS Related Wasting', 'AV Heart Block', 'Abdominal Distension', 'Abnormal Uterine Bleeding', 'Abortion', 'Acetaminophen Overdose', 'Acne', 'Actinic Keratosis', 'Acute Coronary Syndrome', 'Acute Lymphoblastic Leukemia', 'Acute Nonlymphocytic Leukemia', 'Acute Promyelocytic Leukemia', 'Addisons Disease', 'Adrenocortical Insufficiency', 'Adult Human Growth Hormone Deficiency', 'Aggressive Behaviour', 'Agitated State', 'Agitation', 'Alcohol Dependence', 'Alcohol Withdrawal', 'Allergic Reactions', 'Allergic Rhinitis', 'Allergic Urticaria', 'Allergies', 'Alopecia', 'Alpha-1 Proteinase Inhibitor Deficiency', 'Alzheimers Disease', 'Amenorrhea', 'Amyotrophic Lateral Sclerosis', 'Anal Fissure and Fistula', 'Anaphylaxis', 'Anaplastic Astrocytoma', 'Anaplastic Oligodendroglioma', 'Androgenetic Alopecia', 'Anemia', 'Anemia Associated with Chronic Renal Failure', 'Anemia,  Chemotherapy Induced', 'Anemia,  Sickle Cell', 'Anesthesia', 'Anesthetic Adjunct', 'Angina', 'Angina Pectoris Prophylaxis', 'Ankylosing Spondylitis', 'Anorexia', 'Anorexia/Feeding Problems', 'Anthrax', 'Anti NMDA Receptor Encephalitis', 'Antiphospholipid Syndrome', 'Anxiety', 'Anxiety and Stress', 'Arrhythmia', 'Ascariasis', 'Asperger Syndrome', 'Aspergillosis,  Aspergilloma', 'Asthma', 'Asthma,  Maintenance', 'Asthma,  acute', 'Asystole', 'Atherosclerosis', 'Atopic Dermatitis', 'Atrial Fibrillation', 'Atrial Flutte', 'Atrophic Urethritis', 'Atrophic Vaginitis', 'Auditory Processing Disorde', 'Autism', 'Autoimmune Hepatitis', 'Avian Influenza', 'B12 Nutritional Deficiency', 'Babesiosis', 'Back Pain', 'Bacterial Endocarditis Prevention', 'Bacterial Infection', 'Bacterial Skin Infection', 'Bacterial Vaginitis', 'Barretts Esophagus', 'Bartonellosis', 'Basal Cell Carcinoma', 'Behcets Disease', 'Benign Essential Trem', 'Benign Prostatic Hyperplasia', 'Benzodiazepine Withdrawal', 'Biliary Cirrhosis', 'Binge Eating Disorde', 'Bipolar Disorde', 'Birth Control', 'Bladder Infection', 'Bleeding Disorde', 'Blepharitis', 'Body Dysmorphic Disorde', 'Body Imaging', 'Bone infection', 'Borderline Personality Disorde', 'Bowel Preparation', 'Brain Tum', 'Breakthrough Pain', 'Breast Cance', 'Breast Cancer,  Adjuvant', 'Breast Cancer,  Metastatic', 'Breast Cancer,  Palliative', 'Breast Cancer,  Prevention', 'Bronchiectasis', 'Bronchitis', 'Bronchospasm Prophylaxis', 'Bulimia', 'Bullous Pemphigoid', 'Burning Mouth Syndrome', 'Burns,  External', 'Bursitis', 'CMV Prophylaxis', 'CNS Magnetic Resonance Imaging', 'COPD', 'COPD,  Acute', 'COPD,  Maintenance', 'Cachexia', 'Campylobacter Gastroenteritis', 'Cance', 'Candida Urinary Tract Infection', 'Candidemia', 'Carcinoid Tum', 'Cataplexy', 'Cerebral Edema', 'Cerebrovascular Insufficiency', 'Cervical Dystonia', 'Chlamydia Infection', 'Cholera', 'Chronic Eosinophilic Leukemia', 'Chronic Fatigue Syndrome', 'Chronic Idiopathic Constipation', 'Chronic Inflammatory Demyelinating Polyradiculoneuropathy', 'Chronic Lymphocytic Leukemia', 'Chronic Myelogenous Leukemia', 'Chronic Myofascial Pain', 'Chronic Pain', 'Chronic Pancreatitis', 'Chronic Spasticity', 'Clostridial Infection', 'Cluster Headaches', 'Cluster-Tic Syndrome', 'Coccidioidomycosis', 'Cogans Syndrome', 'Cold Sores', 'Cold Symptoms', 'Colorectal Cance', 'Computed Tomography', 'Condylomata Acuminata', 'Conjunctivitis', 'Conjunctivitis,  Allergic', 'Conjunctivitis,  Bacterial', 'Constipation', 'Constipation,  Acute', 'Constipation,  Chronic', 'Constipation,  Drug Induced', 'Coronary Artery Disease', 'Costochondritis', 'Cough', 'Cough and Nasal Congestion', 'Crohns Disease', 'Crohns Disease,  Acute', 'Crohns Disease,  Maintenance', 'Croup', 'Cutaneous Candidiasis', 'Cutaneous Larva Migrans', 'Cutaneous T-cell Lymphoma', 'Cyclic Vomiting Syndrome', 'Cyclitis', 'Cyclothymic Disorde', 'Cystic Fibrosis', 'Dandruff', 'Deep Neck Infection', 'Deep Vein Thrombosis', 'Deep Vein Thrombosis Prophylaxis after Hip Replacement Surgery', 'Deep Vein Thrombosis Prophylaxis after Knee Replacement Surgery', 'Deep Vein Thrombosis,  First Event', 'Deep Vein Thrombosis,  Prophylaxis', 'Deep Vein Thrombosis,  Recurrent Event', 'Delayed Puberty,  Male', 'Dementia', 'Dental Abscess', 'Depression', 'Dermatitis', 'Dermatitis Herpeti', 'Dermatitis Herpetiformis', 'Dermatologic Lesion', 'Dermatological Disorders', 'Dermatomyositis', 'Dermatophytosis', 'Diabetes Insipidus', 'Diabetes,  Type 1', 'Diabetes,  Type 2', 'Diabetic Kidney Disease', 'Diabetic Macular Edema', 'Diabetic Peripheral Neuropathy', 'Diagnosis and Investigation', 'Diagnostic Bronchograms', 'Diaper Rash', 'Diarrhea', 'Diarrhea,  Acute', 'Diarrhea,  Chronic', 'Dientamoeba fragilis', 'Dietary Fiber Supplementation', 'Dietary Supplementation', 'Dissociative Identity Disorde', 'Diverticulitis', 'Dry Eye Disease', 'Dry Skin', 'Duodenal Ulce', 'Duodenal Ulcer Prophylaxis', 'Dupuytrens contracture', 'Dysautonomia', 'Dyspareunia', 'Dysuria', 'Ear Wax Impaction', 'Eczema', 'Edema', 'Ehrlichiosis', 'Emergency Contraception', 'Endometrial Cance', 'Endometrial Hyperplasia', 'Endometrial Hyperplasia,  Prophylaxis', 'Endometriosis', 'Endoscopy or Radiology Premedication', 'Enterocolitis', 'Eosinophilic Esophagitis', 'Epicondylitis,  Tennis Elbow', 'Epididymitis,  Sexually Transmitted', 'Epilepsy', 'Erectile Dysfunction', 'Erosive Esophagitis', 'Esophageal Candidiasis', 'Euvolemic Hyponatremia', 'Expectoration', 'Extrapyramidal Reaction', 'Eye Redness', 'Eye Redness/Itching', 'Eyelash Hypotrichosis', 'GERD', 'Gas', 'Gastric Cance', 'Gastric Ulcer Maintenance Treatment', 'Gastroenteritis', 'Gastrointestinal Decontamination', 'Gastrointestinal Stromal Tum', 'Gastroparesis', 'Gaucher Disease', 'Gender Dysphoria', 'Generalized Anxiety Disorde', 'Gestational Diabetes', 'Giant Cell Tumor of Bone', 'Giardiasis', 'Gingivitis', 'Glaucoma', 'Glaucoma,  Open Angle', 'Glaucoma/Intraocular Hypertension', 'Glioblastoma Multi', 'Glioblastoma Multiforme', 'Gonadotropin Inhibition', 'Gonococcal Infection,  Disseminated', 'Gonococcal Infection,  Uncomplicated', 'Gout', 'Gout,  Acute', 'Gout,  Prophylaxis', 'Gouty Arthritis', 'Granuloma Annulare', 'HIV Infection', 'Hairy Cell Leukemia', 'Hashimotos disease', 'Head Injury', 'Head Lice', 'Head and Neck Cance', 'Headache', 'Heart Attack', 'Heart Failure', 'Helicobacter Pylori Infection', 'Hemangioma', 'Hemophilia A', 'Hemophilia B', 'Hemorrhoids', 'Hepatic Encephalopathy', 'Hepatic Tum', 'Hepatitis B', 'Hepatitis B Prevention', 'Hepatitis C', 'Hepatocellular Carcinoma', 'Herbal Supplementation', 'Hereditary Angioedema', 'Herpes Simplex', 'Herpes Simplex Dendritic Keratitis', 'Herpes Simplex,  Mucocutaneous/Immunocompetent Host', 'Herpes Simplex,  Mucocutaneous/Immunocompromised Host', 'Herpes Simplex,  Suppression', 'Herpes Zoste', 'Herpes Zoster,  Prophylaxis', 'Hiccups', 'Hidradenitis Suppurativa', 'High Blood Pressure', 'High Cholesterol', 'High Cholesterol,  Familial Heterozygous', 'High Cholesterol,  Familial Homozygous', 'Hirsutism', 'Histoplasmosis', 'Hodgkins Lymphoma', 'Hot Flashes', 'Human Papilloma Virus', 'Human Papillomavirus Prophylaxis', 'Hydrocephalus', 'Hyperbilirubinemia', 'Hypercalcemia of Malignancy', 'Hyperekplexia', 'Hyperhidrosis', 'Hyperkalemia', 'Hyperlipoproteinemia', 'Hyperlipoproteinemia Type III,  Elevated beta-VLDL   IDL', 'Hyperlipoproteinemia Type IIa,  Elevated LDL', 'Hyperlipoproteinemia Type IV,  Elevated VLDL', 'Hyperparathyroidism Secondary to Renal Impairment', 'Hyperphosphatemia', 'Hyperphosphatemia of Renal Failure', 'Hyperprolactinemia', 'Hypersomnia', 'Hypertensive Emergency', 'Hyperthyroidism', 'Hypertriglyceridemia', 'Hyperuricemia Secondary to Chemotherapy', 'Hypoactive Sexual Desire Disorde', 'Hypocalcemia', 'Hypodermoclysis', 'Hypoestrogenism', 'Hypoglycemia', 'Hypogonadism,  Male', 'Hypokalemia', 'Hypokalemic Periodic Paralysis', 'Hypoparathyroidism', 'Hypothyroidism,  After Thyroid Removal', 'ICU Agitation', 'Ichthyosis', 'Idiopathic Thrombocytopenic Purpura', 'Immunosuppression', 'Impetig', 'Indigestion', 'Infection Prophylaxis', 'Infectious Diarrhea', 'Inflammatory Bowel Disease', 'Inflammatory Conditions', 'Influenza', 'Influenza Prophylaxis', 'Insomnia', 'Insomnia,  Stimulant-Associated', 'Insulin Resistance Syndrome', 'Intermittent Claudication', 'Interstitial Cystitis', 'Intraabdominal Infection', 'Intraocular Hypertension', 'Iritis', 'Iron Deficiency Anemia', 'Irritable Bowel Syndrome', 'Ischemic Stroke', 'Ischemic Stroke,  Prophylaxis', 'Joint Infection', 'Juvenile Idiopathic Arthritis', 'Juvenile Rheumatoid Arthritis', 'Keratitis', 'Keratoconjunctivitis Sicca', 'Keratosis', 'Kidney Infections', 'Klinefelter Syndrome', 'Labor Induction', 'Labor Pain', 'Lactation Augmentation', 'Lactose Intolerance', 'Left Ventricular Dysfunction', 'Legionella Pneumonia', 'Lennox-Gastaut Syndrome', 'Leukemia', 'Lichen Planus', 'Lichen Sclerosus', 'Light Anesthesia', 'Light Sedation', 'Linear IgA Disease', 'Lipodystrophy', 'Liver Magnetic Resonance Imaging', 'Local Anesthesia', 'Lyme Disease', 'Lyme Disease,  Arthritis', 'Lyme Disease,  Neurologic', 'Lymphocytic Colitis', 'Macular Degeneration', 'Macular Edema', 'Major Depressive Disorde', 'Malaria Prevention', 'Malignant Glioma', 'Mania', 'Manscaping Pain', 'Melanoma,  Metastatic', 'Melasma', 'Menieres Disease', 'Meningitis,  Meningococcal', 'Meningococcal Meningitis Prophylaxis', 'Menopausal Disorders', 'Menorrhagia', 'Menstrual Disorders', 'Methicillin-Resistant Staphylococcus Aureus Infection', 'Microscopic polyangiitis', 'Migraine', 'Migraine Prevention', 'Mild Cognitive Impairment', 'Mitral Valve Prolapse', 'Mixed Connective Tissue Disease', 'Motion Sickness', 'Mountain Sickness / Altitude Sickness', 'Mucositis', 'Multiple Endocrine Adenomas', 'Multiple Myeloma', 'Multiple Sclerosis', 'Mumps Prophylaxis', 'Muscle Pain', 'Muscle Spasm', 'Myasthenia Gravis', 'Mycobacterium avium-intracellulare,  Treatment', 'Mycoplasma Pneumonia', 'Myelodysplastic Syndrome', 'Myelofibrosis', 'Myeloproliferative Disorders', 'Myxedema Coma', 'NSAID-Induced Gastric Ulce', 'NSAID-Induced Ulcer Prophylaxis', 'Narcolepsy', 'Nasal Carriage of Staphylococcus aureus', 'Nasal Congestion', 'Nasal Polyps', 'Nausea/Vomiting', 'Nausea/Vomiting of Pregnancy', 'Nausea/Vomiting,  Chemotherapy Induced', 'Nausea/Vomiting,  Postoperative', 'Nausea/Vomiting,  Radiation Induced', 'Neck Pain', 'Neoplastic Diseases', 'Nephrotic Syndrome', 'Neuralgia', 'Neuritis', 'Neuropathic Pain', 'Neurosurgery', 'Neurotic Depression', 'Neutropenia', 'Neutropenia Associated with Chemotherapy', 'New Daily Persistent Headache', 'Niacin Deficiency', 'Night Terrors', 'Nightmares', 'Nocardiosis', 'Nocturnal Leg Cramps', 'Non-Hodgkins Lymphoma', 'Non-Small Cell Lung Cance', 'Nonoccupational Exposure', 'Not Listed / Othe', 'Obesity', 'Obsessive Compulsive Disorde', 'Obstructive Sleep Apnea/Hypopnea Syndrome', 'Ocular Rosacea', 'Oligospermia', 'Onychomycosis,  Fingernail', 'Onychomycosis,  Toenail', 'Oophorectomy', 'Ophthalmic Surgery', 'Opiate Adjunct', 'Opiate Dependence', 'Opiate Withdrawal', 'Opioid Overdose', 'Opioid-Induced Constipation', 'Oppositional Defiant Disorde', 'Oral Thrush', 'Oral and Dental Conditions', 'Organ Transplant,  Rejection Prophylaxis', 'Organ Transplant,  Rejection Reversal', 'Osteoarthritis', 'Osteolytic Bone Lesions of Multiple Myeloma', 'Osteolytic Bone Metastases of Solid Tumors', 'Osteoporosis', 'Otitis Externa', 'Otitis Media', 'Ovarian Cance', 'Ovarian Cysts', 'Overactive Bladde', 'Ovulation Induction', 'Pagets Disease', 'Pain', 'Pain/Feve', 'Pancreatic Cance', 'Pancreatic Exocrine Dysfunction', 'Panic Disorde', 'Paragonimus westermani,  Lung Fluke', 'Paranoid Disorde', 'Parkinsons Disease', 'Parkinsonian Trem', 'Parkinsonism', 'Patent Ductus Arteriosus', 'Pathological Hypersecretory Conditions', 'Pediatric Growth Hormone Deficiency', 'Pemphigus', 'Peptic Ulce', 'Percutaneous Coronary Intervention', 'Perimenopausal Symptoms', 'Period Pain', 'Periodic Limb Movement Disorde', 'Periodontitis', 'Peripheral Arterial Disease', 'Peripheral Neuropathy', 'Peripheral T-cell Lymphoma', 'Persistent Depressive Disorde', 'Pertussis', 'Peyronies Disease', 'Pharyngitis', 'Photoaging of the Skin', 'Pinworm Infection (Enterobius vermicularis)', 'Pityriasis rubra pilaris', 'Plaque Psoriasis', 'Platelet Aggregation Inhibition', 'Pneumococcal Disease Prophylaxis', 'Pneumonia', 'Polycystic Ovary Syndrome', 'Polycythemia Vera', 'Porphyria', 'Portal Hypertension', 'Post Traumatic Stress Disorde', 'Postherpetic Neuralgia', 'Postmenopausal Symptoms', 'Postoperative Increased Intraocular Pressure', 'Postoperative Ocular Inflammation', 'Postoperative Pain', 'Postpartum Breast Pain', 'Postpartum Depression', 'Postural Orthostatic Tachycardia Syndrome', 'Pre-Exposure Prophylaxis', 'Precocious Puberty', 'Premature Lab', 'Premature Ventricular Depolarizations', 'Premenstrual Dysphoric Disorde', 'Prevention of Atherothrombotic Events', 'Prevention of Bladder infection', 'Prevention of Cardiovascular Disease', 'Prevention of Dental Caries', 'Prevention of Hypokalemia', 'Prevention of Osteoporosis', 'Prevention of Perinatal Group B Streptococcal Disease', 'Prevention of Thromboembolism in Atrial Fibrillation', 'Primary Hyperaldosteronism', 'Primary Hyperaldosteronism Diagnosis', 'Primary Immunodeficiency Syndrome', 'Primary Nocturnal Enuresis', 'Primary Ovarian Failure', 'Progesterone Insufficiency', 'Prostate Cance', 'Prostatitis', 'Prosthetic Heart Valves,  Tissue Valves - Thrombosis Prophylaxis', 'Pruritus', 'Pseudobulbar Affect', 'Pseudogout,  Prophylaxis', 'Pseudomembranous Colitis', 'Pseudotumor Cerebri', 'Psoriasis', 'Psoriatic Arthritis', 'Psychosis', 'Pulmonary Embolism', 'Pulmonary Embolism,  First Event', 'Pulmonary Embolism,  Recurrent Event', 'Pulmonary Hypertension', 'Q Feve', 'Rabies Prophylaxis', 'Radionuclide Myocardial Perfusion Study', 'Ramsay Hunt Syndrome', 'Raynauds Syndrome', 'Reflex Sympathetic Dystrophy Syndrome', 'Reiters Syndrome', 'Renal Cell Carcinoma', 'Renal Transplant', 'Restless Legs Syndrome', 'Reversal of Nondepolarizing Muscle Relaxants', 'Reversal of Opioid Sedation', 'Rheumatoid Arthritis', 'Rhinitis', 'Rhinorrhea', 'Rosacea', 'SIADH', 'STD Prophylaxis', 'Salivary Gland Cance', 'Scabies', 'Schilling Test', 'Schistosoma japonicum', 'Schizoaffective Disorde', 'Schizophrenia', 'Schnitzler Syndrome', 'Sciatica', 'Scleroderma', 'Seasonal Affective Disorde', 'Seasonal Allergic Conjunctivitis', 'Seborrheic Dermatitis', 'Secondary Cutaneous Bacterial Infections', 'Secondary Hyperparathyroidism', 'Sedation', 'Seizure Prevention', 'Seizures', 'Sepsis', 'Sexual Dysfunction,  SSRI Induced', 'Shift Work Sleep Disorde', 'Sinus Symptoms', 'Sinusitis', 'Sjogrens Syndrome', 'Skin Cance', 'Skin Rash', 'Skin and Structure Infection', 'Skin or Soft Tissue Infection', 'Sleep Paralysis', 'Small Bowel Bacterial Overgrowth', 'Small Bowel or Pancreatic Fistula', 'Smoking Cessation', 'Social Anxiety Disorde', 'Soft Tissue Sarcoma', 'Solid Tumors', 'Sore Throat', 'Spondyloarthritis', 'Sporotrichosis', 'Squamous Cell Carcinoma', 'Status Epilepticus', 'Stills Disease', 'Stomach Cance', 'Stomach Ulce', 'Strabismus', 'Strep Throat', 'Streptococcal Infection', 'Stress Ulcer Prophylaxis', 'Strongyloidiasis', 'Subarachnoid Hemorrhage', 'Submental Fullness', 'Sunburn', 'Supraventricular Tachycardia', 'Swine Flu', 'Syringomyelia', 'Systemic Candidiasis', 'Systemic Lupus Erythematosus', 'Systemic Mastocytosis', 'TSH Suppression', 'Tardive Dyskinesia', 'Temporomandibular Joint Disorde', 'Tendonitis', 'Testicular Cance', 'Tetanus', 'Thrombocythemia', 'Thrombocytopenia', 'Thromboembolic Stroke Prophylaxis', 'Thyroid Cance', 'Thyrotoxicosis', 'Tinea Barbae', 'Tinea Capitis', 'Tinea Corporis', 'Tinea Cruris', 'Tinea Pedis', 'Tinea Versicol', 'Tinnitus', 'Tonsillitis/Pharyngitis', 'Toothache', 'Topical Disinfection', 'Tourettes Syndrome', 'Transverse Myelitis', 'Travelers Diarrhea', 'Trichomoniasis', 'Trichotillomania', 'Trigeminal Neuralgia', 'Tuberculosis,  Latent', 'Turners Syndrome', 'Typhoid Feve', 'Ulcerative Colitis', 'Ulcerative Colitis,  Active', 'Ulcerative Colitis,  Maintenance', 'Ulcerative Proctitis', 'Underactive Thyroid', 'Undifferentiated Connective Tissue Disease', 'Upper Limb Spasticity', 'Upper Respiratory Tract Infection', 'Urinary Incontinence', 'Urinary Tract Infection', 'Urinary Tract Stones', 'Urticaria', 'Uterine Bleeding', 'Uterine Fibroids', 'Uveitis', 'Vaginal Yeast Infection', 'Varicella-Zoste', 'Ventricular Arrhythmia', 'Ventricular Tachycardia', 'Vertig', 'Vitamin B12 Deficiency', 'Vitamin D Deficiency', 'Vitamin K Deficiency', 'Vitamin/Mineral Supplementation and Deficiency', 'Vitamin/Mineral Supplementation during Pregnancy/Lactation', 'Vulvodynia', 'Wegeners Granulomatosis', 'Weight Loss', 'Wilsons Disease', 'Wolff-Parkinson-White Syndrome', 'Wound Cleansing', 'Xerostomia', 'Zollinger-Ellison Syndrome', 'acial Lipoatrophy', 'acial Wrinkles', 'actor IX Deficiency', 'amilial Cold Autoinflammatory Syndrome', 'amilial Mediterranean Feve', 'fatigue', 'cal Segmental Glomerulosclerosis', 'emale Infertility', 'eve', 'ibrocystic Breast Disease', 'ibromyalgia', 'lic Acid Deficiency', 'llicular Lymphoma', 'm Pain Disorde', 'unctional Gastric Disorde', 'ungal Infection Prophylaxis', 'ungal Pneumonia', 'von Willebrands Disease', 'zen Shoulde']


# start of streamlit UI
st.title("Oluwabukola's Health Diagnosis & Drug Recommendation Portal")
st.header("Please enter your symptoms 🩺")

disease = st.multiselect('Enter your symptoms so that we can get you a primary diagnosis:',[*disease_list],key='disease')

# evaluation and confirmation
if st.button("Evaluate"):
	with st.spinner('Predicting output...'):
		time.sleep(1)
		if disease:
			st.write("Searching for Drugs For Selected Disease")
			out = (disease)
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
			

# using pandas to read normlized file
data=[]
with open ("Grouped_Drug_Recommendation_Normalized.csv") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		data.append(row)

name = (disease)

col = [x[0] for x in data]

if name in col:
	for x in range(0,len(data)):
		if name == data[x][0]:
			st.write(data[x])

		else:
			st.write("No Drugs found for that illness")
