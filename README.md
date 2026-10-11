# Vaccination Tracker

**Course:** PROG211 Object-Oriented Programming 1 (Individual Assignment)
**University:** Limkokwing University of Creative Technology, Sierra Leone
**Domain:** Health - Vaccination Tracker
**Language:** Python 3

## 1. What this project does

Vaccination Tracker is a small Python program that helps a clinic record the
vaccine doses given to patients. It shows how many doses each patient has
received and whether they are fully vaccinated or still need more doses.

## 2. The real-world problem

Clinics often track vaccines on paper, so records get lost and missed doses go
unnoticed. This program keeps simple digital records so health workers can
quickly see who still needs a dose.

## 3. How it works (Object-Oriented Programming)

| Class | Job | Main attributes | Main methods |
|---|---|---|---|
| `Vaccine` | Describes one vaccine | `name`, `doses_needed` | `display_info()` |
| `Patient` | One anonymous patient record | `patient_id`, `age`, `clinic`, `doses_received` | `receive_dose()`, `is_fully_vaccinated()`, `display_info()`, `display_status()` |
| `VaccinationTracker` | The register that holds all patients | `name`, `patients` | `add_patient()`, `find_patient()`, `give_dose()`, `display_all()` |

**Object interaction:** the tracker stores many `Patient` objects, and a
`Patient` receives a dose by working with a `Vaccine` object.

**Data structure:** one **dictionary** (`self.patients`) stores patients, with
the patient ID as the key and the `Patient` object as the value.
A **tuple** (`VACCINE_CATALOGUE`) holds the fixed list of vaccines offered.

**Methods used**
- Instance methods: `receive_dose()`, `is_fully_vaccinated()`, `display_status()`
- Class methods (`@classmethod`): `get_total_patients()`, `generate_id()`
- Static method (`@staticmethod`): `is_valid_age()`

## 4. How this project meets Digital Public Goods (DPG) standards

| DPG principle | How this project follows it |
|---|---|
| **Open-source** | All source code is published openly on GitHub so anyone can use, study and improve it. |
| **Inclusive and accessible design** | Simple numbered text menu, plain-language messages, clear error messages, and no internet or special hardware needed. |
| **Privacy-respecting** | No names, phone numbers or home addresses are stored. Each patient has only an anonymous ID (for example `VT-2026-0001`), an age and a clinic. The program reminds the user not to type personal details. |
| **Modular and reusable** | Each class does one job. `Vaccine`, `Patient` and `VaccinationTracker` can be reused or extended in other health programs. |

**Note:** the 10 patients that appear when the program starts are **made-up test
data**, not real people.

## 5. How to run

1. Install Python 3 from https://www.python.org
2. Download `vaccination_tracker.py` from this repository.
3. Open a terminal in that folder and run:

```
python vaccination_tracker.py
```

## 6. Example usage (sample input and output)

**Menu**

```
========================================
       VACCINATION TRACKER
========================================
1. Register a new patient
2. Give a vaccine dose
3. Check vaccination status
4. Display all patients
5. Show total number of patients
0. Exit
Enter your choice (0-5):
```

**Sample input:** `2` (give a dose), patient ID `VT-2026-0001`, vaccine `3`
(Pentavalent), date `2026-10-01`

**Sample output**

```
Dose 2 of 3 given: Pentavalent on 2026-10-01
```

**Sample input:** `3` (check status), patient ID `VT-2026-0001`

**Sample output**

```
Vaccination status for VT-2026-0001:
  BCG            1/1  COMPLETE
  Polio (OPV)    2/4  needs 2 more
  Pentavalent    2/3  needs 1 more
  Measles        0/2  needs 2 more
  Yellow Fever   0/1  needs 1 more
```

**Sample input:** `4` (display all patients)

**Sample output (first record)**

```
Community Immunisation Register - 10 patient(s)
--------------------------------------------------------
ID: VT-2026-0001 | Age: 1 | Clinic: Central Health Centre
   Doses: {'BCG': 1, 'Polio (OPV)': 2, 'Pentavalent': 1}
```

## 7. Files

- `vaccination_tracker.py` - the full program
- `README.md` - this file
- `LICENSE` - MIT open-source license

## 8. Author

Student, Limkokwing University of Creative Technology, Sierra Leone
Lecturer: Amandus Benjamin Coker

## 9. License

This project is open-source under the MIT License. See the `LICENSE` file.
