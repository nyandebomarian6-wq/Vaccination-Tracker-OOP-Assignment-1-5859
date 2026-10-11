"""
Vaccination Tracker - PROG211 Object-Oriented Programming 1 (Individual)
Domain: Health

Records vaccine doses given to patients and shows who still needs doses.

DPG (Digital Public Goods) design:
- Open-source: shared on GitHub.
- Privacy-respecting: NO names, phone numbers or addresses are stored.
  Each patient has only an anonymous ID, an age and a clinic.
- Inclusive and simple: plain text menu and clear messages.
- Modular and reusable: each class does one job.

The sample patients are made-up test data, not real people.
"""

from datetime import date


class Vaccine:
    """A vaccine and the number of doses (shots) it needs."""

    def __init__(self, name, doses_needed):
        self.name = name
        self.doses_needed = doses_needed

    def display_info(self):
        print(f"Vaccine: {self.name} | Doses needed: {self.doses_needed}")


# A tuple (cannot be changed) with the vaccines the clinic offers.
VACCINES = (
    Vaccine("BCG", 1),
    Vaccine("Polio (OPV)", 4),
    Vaccine("Pentavalent", 3),
    Vaccine("Measles", 2),
    Vaccine("Yellow Fever", 1),
)


class Patient:
    """One anonymous patient record."""

    total_patients = 0  # class attribute: shared by all patients

    def __init__(self, patient_id, age, clinic):
        self.patient_id = patient_id
        self.age = age
        self.clinic = clinic
        self.doses_received = {}  # vaccine name -> doses given so far
        Patient.total_patients += 1

    # Instance methods: work on ONE patient
    def receive_dose(self, vaccine, date_given):
        """Gives one dose of a vaccine and returns a message."""
        given = self.doses_received.get(vaccine.name, 0)
        if given >= vaccine.doses_needed:
            return f"{vaccine.name}: all doses already given."
        self.doses_received[vaccine.name] = given + 1
        return (f"Dose {given + 1} of {vaccine.doses_needed} given: "
                f"{vaccine.name} on {date_given}")

    def is_fully_vaccinated(self, vaccine):
        """True if the patient has all doses of this vaccine."""
        return self.doses_received.get(vaccine.name, 0) >= vaccine.doses_needed

    def display_info(self):
        print(f"ID: {self.patient_id} | Age: {self.age} | "
              f"Clinic: {self.clinic}")
        print(f"   Doses: {self.doses_received}")

    def display_status(self):
        print(f"Status for {self.patient_id}:")
        for vaccine in VACCINES:
            given = self.doses_received.get(vaccine.name, 0)
            if self.is_fully_vaccinated(vaccine):
                note = "COMPLETE"
            else:
                note = f"needs {vaccine.doses_needed - given} more"
            print(f"  {vaccine.name:<13} {given}/{vaccine.doses_needed} {note}")

    # Class methods: work on the WHOLE class
    @classmethod
    def get_total_patients(cls):
        return cls.total_patients

    @classmethod
    def generate_id(cls):
        """Makes the next anonymous ID, e.g. VT-2026-0001."""
        return f"VT-2026-{cls.total_patients + 1:04d}"

    # Static method: needs no object and no class
    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 120


class VaccinationTracker:
    """The register. Keeps all patients in ONE dictionary."""

    def __init__(self, name):
        self.name = name
        self.patients = {}  # patient ID (key) -> Patient object (value)

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    def find_patient(self, patient_id):
        return self.patients.get(patient_id)

    def give_dose(self, patient_id, vaccine, date_given):
        patient = self.find_patient(patient_id)
        if patient is None:
            return "Patient ID not found."
        return patient.receive_dose(vaccine, date_given)

    def display_all(self):
        print("=" * 56)
        print(f"{self.name} - {len(self.patients)} patient(s)")
        print("=" * 56)
        for patient in self.patients.values():
            patient.display_info()


# ---------------------- Menu actions ----------------------
def register_patient(tracker):
    print("\n--- Register a new patient (do NOT type names) ---")
    age = input("Age in years (0 for a baby under 1): ").strip()
    if not age.isdigit() or not Patient.is_valid_age(int(age)):
        print("Invalid age. Please type a number from 0 to 120.")
        return
    clinic = input("Clinic name: ").strip() or "Unknown clinic"
    patient = Patient(Patient.generate_id(), int(age), clinic)
    tracker.add_patient(patient)
    print(f"Patient registered. Their ID is {patient.patient_id}")


def give_vaccine_dose(tracker):
    print("\n--- Give a vaccine dose ---")
    patient_id = input("Patient ID (e.g. VT-2026-0001): ").strip().upper()
    if tracker.find_patient(patient_id) is None:
        print("Patient ID not found.")
        return
    for number, vaccine in enumerate(VACCINES, start=1):
        print(f"  {number}. {vaccine.name} ({vaccine.doses_needed} dose(s))")
    choice = input("Vaccine number: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(VACCINES)):
        print("Invalid vaccine number.")
        return
    date_given = input("Date (YYYY-MM-DD, Enter for today): ").strip()
    date_given = date_given or date.today().isoformat()
    print(tracker.give_dose(patient_id, VACCINES[int(choice) - 1], date_given))


def check_status(tracker):
    print("\n--- Check vaccination status ---")
    patient_id = input("Patient ID (e.g. VT-2026-0001): ").strip().upper()
    patient = tracker.find_patient(patient_id)
    if patient is None:
        print("Patient ID not found.")
    else:
        patient.display_status()


def show_menu():
    print("\n" + "=" * 40)
    print("       VACCINATION TRACKER")
    print("=" * 40)
    print("1. Register a new patient")
    print("2. Give a vaccine dose")
    print("3. Check vaccination status")
    print("4. Display all patients")
    print("5. Show total number of patients")
    print("0. Exit")


# ---------------------- Made-up sample data ----------------------
def add_sample(tracker, age, clinic, *doses):
    """Makes one made-up patient and gives the doses listed (vaccine, date)."""
    patient = Patient(Patient.generate_id(), age, clinic)
    for vaccine, date_given in doses:
        patient.receive_dose(vaccine, date_given)
    tracker.add_patient(patient)


def load_sample_data(tracker):
    bcg, polio, penta, measles, yellow = VACCINES
    add_sample(tracker, 1, "Central Health Centre",
               (bcg, "2026-01-10"), (polio, "2026-01-10"),
               (polio, "2026-02-14"), (penta, "2026-02-14"))
    add_sample(tracker, 2, "Eastern Community Clinic",
               (bcg, "2025-03-05"), (measles, "2025-12-01"),
               (measles, "2026-06-01"))
    add_sample(tracker, 0, "Waterloo Health Post",
               (bcg, "2026-08-20"), (polio, "2026-08-20"))
    add_sample(tracker, 5, "Hastings Health Post", (yellow, "2026-04-18"))
    add_sample(tracker, 3, "Regent Community Clinic",
               (penta, "2025-11-02"), (penta, "2025-12-07"),
               (penta, "2026-01-11"), (measles, "2026-07-09"))
    add_sample(tracker, 0, "Central Health Centre", (bcg, "2026-09-02"))
    add_sample(tracker, 4, "Goderich Health Post",
               (bcg, "2022-09-14"), (yellow, "2023-03-10"),
               (measles, "2023-06-21"))
    add_sample(tracker, 6, "Murray Town Health Centre",
               (measles, "2021-05-12"), (measles, "2021-11-12"),
               (yellow, "2021-05-12"))
    add_sample(tracker, 1, "Lumley Community Clinic",
               (bcg, "2025-11-12"), (polio, "2025-11-12"),
               (penta, "2025-12-17"))
    add_sample(tracker, 8, "Hastings Health Post", (measles, "2019-09-10"))


def main():
    tracker = VaccinationTracker("Community Immunisation Register")
    load_sample_data(tracker)
    while True:
        show_menu()
        choice = input("Enter your choice (0-5): ").strip()
        if choice == "1":
            register_patient(tracker)
        elif choice == "2":
            give_vaccine_dose(tracker)
        elif choice == "3":
            check_status(tracker)
        elif choice == "4":
            tracker.display_all()
        elif choice == "5":
            print(f"\nTotal patients: {Patient.get_total_patients()}")
        elif choice == "0":
            print("Thank you for using Vaccination Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please type a number from 0 to 5.")


if __name__ == "__main__":
    main()
