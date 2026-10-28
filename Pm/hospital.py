patients = []

def add_patient():
    pid = int(input("Enter Patient ID: "))
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")

    patient = {
        "id": pid,
        "name": name,
        "age": age,
        "disease": disease
    }

    patients.append(patient)
    print("Patient added successfully!")


def update_patient():
    pid = int(input("Enter Patient ID to update: "))

    for patient in patients:
        if patient["id"] == pid:
            patient["name"] = input("Enter New Name: ")
            patient["age"] = int(input("Enter New Age: "))
            patient["disease"] = input("Enter New Disease: ")
            print("Patient updated successfully!")
            return

    print("Patient not found!")


def delete_patient():
    pid = int(input("Enter Patient ID to delete: "))

    for patient in patients:
        if patient["id"] == pid:
            patients.remove(patient)
            print("Patient deleted successfully!")
            return

    print("Patient not found!")


def display_patients():
    if len(patients) == 0:
        print("No patients available.")
    else:
        print("\nPatient Details:")
        for patient in patients:
            print("ID:", patient["id"])
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Disease:", patient["disease"])
            print("-------------------")


while True:
    print("\n--- Hospital Management System ---")
    print("1. Add Patient")
    print("2. Update Patient")
    print("3. Delete Patient")
    print("4. Display Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_patient()
    elif choice == 2:
        update_patient()
    elif choice == 3:
        delete_patient()
    elif choice == 4:
        display_patients()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")