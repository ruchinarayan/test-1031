select * from patient;
select * from encounter;
select * from encounter_diagnosis;
select * from lab_result;
select * from diagnosis;

--Data Exercise 1
--Provide a list of male patients in the database and the counts of patients by gender.
select gender, count(*) from patient group by 1 order by 1;
select * from patient where gender = 'M';


--Data Exercise 2
--Count patients in database diagnosed with DERMITITIS at an encounter.
-- Does that mean DERMATITIS instead of DERMITITIS

select count(distinct patient.id)
from patient left join encounter
on patient.id = encounter.patient_id
left join encounter_diagnosis
on encounter.id = encounter_diagnosis.encounter_id
left join diagnosis 
on encounter_diagnosis.diagnosis_id = diagnosis.id
where diagnosis.name  like '%DERMATITIS%';

select * from diagnosis where diagnosis.name  like '%DERMATITIS%';

--Data Exercise 3
--Provide a list patients, by MRN, who have had a CD4 count of less than 300.

select patient.id, patient.MRN, patient.gender, patient.birthdate, patient.birthdate_estimated from
patient left join encounter
on patient.id = encounter.patient_id
left join lab_result
on encounter.id = lab_result.encounter_id
where lab_result.cd4 < 300
order by patient.mrn;


--Data Exercise 4
--Count all female patients above the age of 30 in the database as of today’s date

select count(*) from patient 
where gender = 'F'
and (Date('now') - birthdate) > 30;

--Bonus Data Exercise
--Describe any potential concerns with either the data itself or the design of the database.


