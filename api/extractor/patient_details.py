import re

def get_name(text):
    name_regex = r"Patient Information\n*([a-zA-Z0-9, ]+)"
    name_search = re.search(name_regex, text)
    name=""
    if name_search is not None:
        name_search = name_search.groups()
        name = str(name_search[0])
        name = " ".join(name.strip().split(",")[::-1]).strip()
    else:
        name = ""
    return name
    
def get_phone(text):
    phone_search = re.search(r"(\([\d]+\) [\d]+\-[\d]+)", text)
    phone=""
    if phone_search is not None:
        phone_search = phone_search.groups()
        phone_search = str(phone_search[0])
        phone = phone_search.strip()
    else:
        phone = ""
    return phone
    
def get_date_of_birth(text):
    dob_regex = r"Birth Date\n*([A-Za-z0-9, ]+)"
    dob_search = re.search(dob_regex, text)
    dob=""
    if dob_search is not None:
        dob_search = dob_search.groups()
        dob = str(dob_search[0])
        dob = dob.strip()
    else:
        dob = ""
    return dob

def get_height(text):
    height=""
    height_search = re.search(r"Height:\n*([\d]+)", text)
    if height_search is not None:
        height_search = height_search.groups()
        height = str(height_search[0])
        height = height.strip()
    else:
        height = ""
    return height

def get_weight(text):
    weight=""
    weight_search = re.search(r"Weight:\n*([\d]+)", text)
    if weight_search is not None:
        weight_search = weight_search.groups()
        weight = str(weight_search[0])
        weight = weight.strip()
    else:
        weight = ""
    return weight
    
def get_address(text):
    address="12"
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
    return address
        
def get_emergency_name(text):
    emergency_name=""
    emr_name = re.search(r"Case of Emergency\n\n([a-zA-Z0-9, ]+)", text)
    if emr_name is not None:
        emr_name = emr_name.groups()
        emergency_name = str(emr_name[0])
        emergency_name = emergency_name.strip()
    else:
        emergency_name = ""
    return emergency_name
    
def get_emr_addr(text):
    emr_addr=""
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
        
    return emr_addr

def get_home(text):
    home=""
    home_phone = re.search(r"Home phone\n*(\([\d]+\) [\d]+\-[\d]+)", text)
    if home_phone is not None:
        home_phone = home_phone.groups()
        home = str(home_phone[0])
        home = home.strip()
    else:
        home = ""
    return home
    
def get_work_phone(text):
    work=""
    work_phone = re.search(r"Work phone\n*(\([\d]+\) [\d]+\-[\d]+)", text)
    if work_phone is not None:
        work_phone = work_phone.groups()
        work = str(work_phone[0])
        work = work.strip()
    else:
        work = ""
    return work
    
def get_chicken_pox(text):
    chicken_pox=""
    chicken_pox_search = re.search(
        r"Chicken Pox \(Varicella\):\n*([a-zA-Z0-9, \/]+)", text
        )
    if chicken_pox_search is not None:
        chicken_pox_search = chicken_pox_search.groups()
        chicken_pox = str(chicken_pox_search[0])
        chicken_pox = chicken_pox.strip()
    else:
        chicken_pox = ""
    return chicken_pox

def get_measles(text):
    measles=""
    measles_search = re.search(r"Measles:\n*([a-zA-z0-9, \/]+)\n*", text)
    if measles_search is not None:
        measles_search = measles_search.groups()    
        measles = str(measles_search[0])
        measles = measles.strip()
    else:
        measles = ""
    return measles
    
def  get_hepatitis_b_vaccine(text):
    hepatitis_b_vaccine=""
    hepa_search = re.search(
        r"Have you had the Hepatitis B vaccination\?\n\n([a-zA-z0-9, ]+)", text
                            )
    if hepa_search is not None:
        hepa_search = hepa_search.groups()
        hepatitis_b_vaccine = str(hepa_search[0])
        hepatitis_b_vaccine = hepatitis_b_vaccine.strip()
    else:
        hepatitis_b_vaccine = ""
    return hepatitis_b_vaccine
    
def get_medical_problems(text):
    medical_problems=""
    
    medical_problems_pattern = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*Create*", text
        )
    medical_problems_pattern1 = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*Page", text
        )
    medical_problems_pattern2 = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*€}", text
        )
    medical_problems_pattern3 = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*Name", text
        )

    if medical_problems_pattern is not None:
        medical_problems_pattern = medical_problems_pattern.groups()
        medical_problems = str(medical_problems_pattern[0])
        medical_problems = medical_problems.strip()
    elif medical_problems_pattern1 is not None:
        medical_problems_pattern1 = medical_problems_pattern1.groups()
        medical_problems = str(medical_problems_pattern1[0])
        medical_problems = medical_problems.strip()
    elif medical_problems_pattern2 is not None:
        medical_problems_pattern2 = medical_problems_pattern2.groups()
        med2 = str(medical_problems_pattern2[0])
        medical_problems = med2.strip()
    elif medical_problems_pattern3 is not None:
        medical_problems_pattern3 = medical_problems_pattern3.groups()
        med2 = str(medical_problems_pattern3[0])
        medical_problems = med2.strip()
    else:
        medical_problems = ""
    return medical_problems

def get_insurance_company(text):
    insurance_company=""
    insurance_company_search = re.search(r"Name of Insurance Company:\n*([a-zA-Z, ]+)", text)
    if insurance_company_search is not None:
        insurance_company_search = insurance_company_search.groups()
        insurance_company = str(insurance_company_search[0])
        insurance_company = insurance_company.strip()
    else:
        insurance_company = ""
        
    return insurance_company

def get_policy_no(text):
    policy_no=""
    policy_no_search = re.search(r"Policy Number:\n*[a-zA-Z\s, ]*([0-9]+)", text)
    if policy_no_search is not None:
        policy_no_search = policy_no_search.groups()
        policy_no = str(policy_no_search[0])
        policy_no = policy_no.strip()
    else:
        policy_no = ""
    return policy_no

def get_expiry_date(text):
    expiry_date=""
    expiry_date_search = re.search(r"Expiry Date:\n*([a-zA-Z0-9, ]+)", text)
    if expiry_date_search is not None:
        expiry_date_search = expiry_date_search.groups()
        expiry_date = str(expiry_date_search[0])
        expiry_date = expiry_date.strip()
    else:
        expiry_date = ""
    return expiry_date
    
def get_has_medical_insurance(text):
    has_medical_insurance=""
    medical_insurance_flag_search = re.search(
        r"Do you have medical insurance\?\n*([a-zA-Z0-9, \/]+)", text
        )
    if medical_insurance_flag_search is not None:
        hm_search = medical_insurance_flag_search.groups()
        has_medical_insurance = str(hm_search[0])
        has_medical_insurance = has_medical_insurance.strip()
    else:
        has_medical_insurance = ""
    return has_medical_insurance
    
def get_allergies(text):
    allergies=""
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
    return allergies

def get_medication(text):
    medication=""
    medication_pattern1 = re.search(r"Expiry Date:\n*[a-zA-Z0-9, ]+\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*Create*", text) # noqa
    medication_pattern2 = re.search(r"List any medication taken regularly:\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*Create*", text) # noqa
    medication_pattern3 = re.search(r"Expiry Date:\n*[a-zA-Z0-9, ]+\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*€}", text) # noqa
    medication_pattern4 = re.search(r"List any medication taken regularly:\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*", text) # noqa

    if medication_pattern1 is not None:
        medication_pattern1 = medication_pattern1.groups()
        medication_pattern1 = str(medication_pattern1[0])
        medication = medication_pattern1.strip()
    elif medication_pattern2 is not None:
        medication_pattern2 = medication_pattern2.groups()
        medication_temp = str(medication_pattern2[0])
        medication = medication_temp.strip()
    elif medication_pattern3 is not None:
        med3 = medication_pattern3.groups()
        med3 = str(med3[0])
        medication = med3.strip()
    elif medication_pattern4 is not None:
        med4 = medication_pattern4.groups()
        med4 = str(med4[0])
        medication = med4.strip()
    else:
        medication = ""
    return medication
    

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
    name=get_name(text)
    
    phone=get_phone(text)
    
    dob=get_date_of_birth(text)

    height=get_height(text)

    weight=get_weight(text)
    
    address=get_address(text)

    emergency_name=get_emergency_name(text)

    emr_addr=get_emr_addr(text)
    
    home_phone=get_home(text)

    work=get_work_phone(text)
    
    chicken_pox=get_chicken_pox(text)

    measles=get_measles(text)
    
    hepatitis_b_vaccine=get_hepatitis_b_vaccine(text)
    
    medical_problems=get_medical_problems(text)

    insurance_company=get_insurance_company(text)

    policy_no=get_policy_no(text)

    expiry_date=get_expiry_date(text)

    has_medical_insurance=get_has_medical_insurance(text)

    allergies=get_allergies(text)

    medication=get_medication(text)

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
