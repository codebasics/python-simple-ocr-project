import re


def extract_details(text):
    """Extract patient details from the text

    Parameters
    ----------
    text : str
        text to be searched for Details

    Returns
    -------
    patient: list(tuples)
        patient data extracted from text
    """
    name_regex = r"Patient Information\n*([a-zA-Z0-9, ]+)"
    name_search = re.search(name_regex, text)

    if name_search is not None:
        name_search = name_search.groups()
        name = str(name_search[0])
        name = " ".join(name.strip().split(",")[::-1]).strip()
    else:
        name = ""
    # gender_regex = r"Gender: ([M|F]?)([\s]*)Phone"
    # gender_search = re.search(gender_regex, text).groups()

    # if gender_search is not None:
    #     gender = str(gender_search[0])

    # gender = gender.strip()
    phone_search = re.search(r"(\([\d]+\) [\d]+\-[\d]+)", text)

    if phone_search is not None:
        phone_search = phone_search.groups()
        phone_search = str(phone_search[0])
        phone = phone_search.strip()
    else:
        phone = ""

    dob_regex = r"Birth Date\n*([A-Za-z0-9, ]+)"
    dob_search = re.search(dob_regex, text)

    if dob_search is not None:
        dob_search = dob_search.groups()
        dob = str(dob_search[0])
        dob = dob.strip()
    else:
        dob = ""

    height_search = re.search(r"Height:\n*([\d]+)", text)
    if height_search is not None:
        height_search = height_search.groups()
        height = str(height_search[0])
        height = height.strip()
    else:
        height = ""

    weight_search = re.search(r"Weight:\n*([\d]+)", text)
    if weight_search is not None:
        weight_search = weight_search.groups()
        weight = str(weight_search[0])
        weight = weight.strip()
    else:
        weight = ""

    address_search = re.search(
        r"\([\d]+\) [\d]+\-[\d]+\n\n([0-9A-Za-z\n\s\,]+)", text
        )
    address = ""
    if address_search is not None:
        address_search = address_search.groups()
        address = str(address_search[0])
        addr1 = address.split("\n\n")
        tempaddr = addr1[0]
        address = str(tempaddr)
        ' '.join(address.splitlines())
        address = address.strip()
    else:
        address = ""

    emr_name = re.search(r"Case of Emergency\n\n([a-zA-Z0-9, ]+)", text)
    if emr_name is not None:
        emr_name = emr_name.groups()
        emergency_name = str(emr_name[0])
        emergency_name = emergency_name.strip()
    else:
        emergency_name = ""

    emr_addr = re.search(r"Height:\n*[\d]+\n\n([0-9A-Za-z\n\s\,]+)", text)
    if emr_addr is not None:
        emr_addr = emr_addr.groups()
        emr_add = str(emr_addr[0])
        emr_add1 = emr_add.split("\n\n")
        tempemr = emr_add1[0]
        emr_addr = str(tempemr)
        emr_addr.replace("\n", " ")
        emr_addr = emr_addr.strip()
    else:
        emr_addr = ""

    home_phone = re.search(r"Home phone\n*(\([\d]+\) [\d]+\-[\d]+)", text)
    if home_phone is not None:
        home_phone = home_phone.groups()
        home = str(home_phone[0])
        home = home.strip()
    else:
        home = ""

    work_phone = re.search(r"Work phone\n*(\([\d]+\) [\d]+\-[\d]+)", text)
    if work_phone is not None:
        work_phone = work_phone.groups()
        work = str(work_phone[0])
        work = work.strip()
    else:
        work = ""

    chicken_pox_search = re.search(
        r"Chicken Pox \(Varicella\):\n*([a-zA-Z0-9, \/]+)", text
        )
    if chicken_pox_search is not None:
        chicken_pox_search = chicken_pox_search.groups()
        chicken_pox = str(chicken_pox_search[0])
        chicken_pox = chicken_pox.strip()
    else:
        chicken_pox = ""

    measles_search = re.search(r"Measles:\n*([a-zA-z0-9, \/]+)\n*", text)
    if measles_search is not None:
        measles_search = measles_search.groups()    
        measles = str(measles_search[0])
        measles = measles.strip()
    else:
        measles = ""

    hepa_search = re.search(
        r"Have you had the Hepatitis B vaccination\?\n\n([a-zA-z0-9, ]+)", text
                            )
    if hepa_search is not None:
        hepa_search = hepa_search.groups()
        hepatitis_b_vaccine = str(hepa_search[0])
        hepatitis_b_vaccine = hepatitis_b_vaccine.strip()
    else:
        hepatitis_b_vaccine = ""

    medical_problems_search1 = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*Page", text
        )
    medical_problems_search = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*Create*", text
        )
    medical_problems_search2 = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*€}", text
        )
    medical_problems_search3 = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*Name", text
        )

    if medical_problems_search is not None:
        medical_problems_search = medical_problems_search.groups()
        medical_problems = str(medical_problems_search[0])
        medical_problems = medical_problems.strip()
    elif medical_problems_search1 is not None:
        medical_problems_search1 = medical_problems_search1.groups()
        medical_problems = str(medical_problems_search1[0])
        medical_problems = medical_problems.strip()
    elif medical_problems_search2 is not None:
        medical_problems_search2 = medical_problems_search2.groups()
        med2 = str(medical_problems_search2[0])
        medical_problems = med2.strip()
    elif medical_problems_search3 is not None:
        medical_problems_search3 = medical_problems_search3.groups()
        med2 = str(medical_problems_search3[0])
        medical_problems = med2.strip()
    else:
        medical_problems = ""

    insurance_company_search = re.search(r"Name of Insurance Company:\n*([a-zA-Z, ]+)", text)
    if insurance_company_search is not None:
        insurance_company_search = insurance_company_search.groups()
        insurance_company = str(insurance_company_search[0])
        insurance_company = insurance_company.strip()
    else:
        insurance_company = ""

    policy_no_search = re.search(r"Policy Number:\n*[a-zA-Z\s, ]*([0-9]+)", text)
    if policy_no_search is not None:
        policy_no_search = policy_no_search.groups()
        policy_no = str(policy_no_search[0])
        policy_no = policy_no.strip()
    else:
        policy_no = ""

    expiry_date_search = re.search(r"Expiry Date:\n*([a-zA-Z0-9, ]+)", text)
    if expiry_date_search is not None:
        expiry_date_search = expiry_date_search.groups()
        expiry_date = str(expiry_date_search[0])
        expiry_date = expiry_date.strip()
    else:
        expiry_date = ""

    medical_insurance_flag_search = re.search(
        r"Do you have medical insurance\?\n*([a-zA-Z0-9, \/]+)", text
        )
    if medical_insurance_flag_search is not None:
        hm_search = medical_insurance_flag_search.groups()
        has_medical_insurance = str(hm_search[0])
        has_medical_insurance = has_medical_insurance.strip()
    else:
        has_medical_insurance = ""

    allergies_search = re.search(
        r"List any allergies:\n*([0-9A-Za-z\n\s,.\/]+)\n\n", text
        )
    if allergies_search is not None:
        allergies_search = allergies_search.groups()
        allergies = str(allergies_search[0])
        allergies1 = allergies.split("\n\n")
        temp_allergies = allergies1[0]
        allergies = str(temp_allergies)
        allergies.replace("\n", " ")
        allergies = allergies.strip()
    else:
        allergies = ""

    medication_search = re.search(r"List any medication taken regularly:\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*Create*", text) # noqa
    med = re.search(r"Expiry Date:\n*[a-zA-Z0-9, ]+\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*Create*", text) # noqa
    med2 = re.search(r"Expiry Date:\n*[a-zA-Z0-9, ]+\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*€}", text) # noqa
    med3 = re.search(r"List any medication taken regularly:\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*", text) # noqa

    if med is not None:
        med = med.groups()
        med = str(med[0])
        medication = med.strip()
    elif medication_search is not None:
        medication_search = medication_search.groups()
        medication_temp = str(medication_search[0])
        medication = medication_temp.strip()
    elif med2 is not None:
        med2 = med2.groups()
        med2 = str(med2[0])
        medication = med2.strip()
    elif med3 is not None:
        med3 = med3.groups()
        med2 = str(med3[0])
        medication = med2.strip()
    else:
        medication = ""

#     Date of Birth: 12/10/1948 Age: 70 y.o.
    # address_regex = r"
    # Date of Birth:[ ]+[0-9\/]+[ ]*Age:[ ]*[0-7 ]+y.o.[\n]+Address:[ ]+
    # ([0-9A-Za-z\n\s]+)"
    # address_search = re.search(address_regex, text).groups()

    # if address_search is not None:
    #     address = str(address_search[0])

    # address = address.strip()
    patient = [
        ("Patient Information",
         [
            ("name", name),
            # "gender"), gender),o
            ("phone", phone),
            ("dob", dob),
            ("height", height),
            ("weight", weight),
            ("address", address)
            ]
         ),
        ("Emergency Information",
         [
             ("Name", emergency_name),
             ("Address", emr_addr),
             ("home phone", home_phone),
             ("work phone", work)
             ]
         ),

        ("General Medical History",
         [
            ("Chicken Pox (Varicella)", chicken_pox),
            ("Measles", measles),
            ("Have you had the Hepatitis B vaccination?", hepatitis_b_vaccine),
            ("Medical Problems", medical_problems),
            ("Name of Insuarance Company", insurance_company),
            ("Policy Number", policy_no),
            ("Expiry Date", expiry_date),
            ("Have medical insurance?", has_medical_insurance),
            ("Any Allergies", allergies),
            ("Any Medications Regularly", medication)
            ]
         )
    ]
    return patient
