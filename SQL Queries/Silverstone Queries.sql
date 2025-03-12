--Readmission rate over time
select a.admission_month as "Month", round(avg(a.readmission_flag::numeric) * 100, 1) as "Readmission Rate (%)" 
from admissions a 
group by a.admission_month 
order by a.admission_month;

--Readmission rate vs length of stay
select a.admission_month as "Month", round(avg(a.readmission_flag::numeric) * 100, 1) as "Readmission Rate (%)", 
round(avg(a.length_of_stay)::numeric, 1) as "Avg. Length of Stay (Days)" 
from admissions a 
group by a.admission_month 
order by a.admission_month;

--Readmission rate vs bed occupancy
select a.admission_month as "Month", round(avg(a.readmission_flag::numeric) * 100, 1) as "Readmission Rate (%)", 
round((avg(h.occupied_beds::numeric) / avg(h.total_beds::numeric)) * 100, 1) as "Bed Occupancy Rate (%)" 
from admissions a 
join hospital_capacity h on to_char(h.date, 'YYYY-MM') = a.admission_month 
group by a.admission_month 
order by a.admission_month;

--Readmission rate by diagnosis
select a.diagnosis_code as "Diagnosis Code", round(avg(a.readmission_flag::numeric) * 100, 1) as "Readmission Rate (%)" 
from admissions a 
group by a.diagnosis_code 
order by "Readmission Rate (%)" desc;

--Readmissions by discharge type
select a.discharge_type as "Discharge Type", round(avg(a.readmission_flag::numeric) * 100, 1) as "Readmission Rate (%)" 
from admissions a 
group by a.discharge_type 
order by "Readmission Rate (%)" desc;
