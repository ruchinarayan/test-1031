select * from patient;
select * from encounter;
select * from encounter_diagnosis;
select * from lab_result;
select * from diagnosis;

-- Data Exercise 1: Provide a list of male patients in the database and the counts of patients by gender.
-- Data Exercise 1 Response: Male- 1800, Female- 3483, NULL- 1
select gender, count(*) from patient group by 1 order by 1; -- Uploaded a csv file named "CountByGender.csv"
select * from patient where gender = 'M'; -- Uploaded the list seperately named "MalePatientsList.csv"


-- Data Exercise 2: Count patients in database diagnosed with DERMITITIS at an encounter.
-- Doubt: Does that mean DERMATITIS instead of DERMITITIS
-- Data Exercise 2 Response: Count = 159
select count(distinct patient.id)
from patient left join encounter
on patient.id = encounter.patient_id
left join encounter_diagnosis
on encounter.id = encounter_diagnosis.encounter_id
left join diagnosis 
on encounter_diagnosis.diagnosis_id = diagnosis.id
where diagnosis.name  like '%DERMATITIS%';


-- Data Exercise 3: Provide a list patients, by MRN, who have had a CD4 count of less than 300.
-- Data Exercise 3 Response: Uploaded the list seperately named "Patient_CD4_Less300.csv"
select patient.id, patient.MRN, patient.gender, patient.birthdate, patient.birthdate_estimated from
patient left join encounter
on patient.id = encounter.patient_id
left join lab_result
on encounter.id = lab_result.encounter_id
where lab_result.cd4 < 300
order by patient.mrn;


-- Data Exercise 4: Count all female patients above the age of 30 in the database as of today’s date
-- Data Exercise 3 Response: Count- 2857
select count(*) from patient 
where gender = 'F'
and (Date('now') - birthdate) > 30;

-- Bonus Data Exercise: Describe any potential concerns with either the data itself or the design of the database.
-- Bonus Data Exercise Response:
--1. The diagnosis values in diagnosis table can be split into multiple columns instead of comma-separating them. Having diagnosis in separate columns would result in better analysis for encounter.
--2. The IDs in each tables can be named with a better naming convention to identify those correctly in case of multiple IDs being present in a table.
