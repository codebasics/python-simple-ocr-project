import re


def extract_details(text):
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
    addr = ""
    if address_search is not None:
        address_search = address_search.groups()
        address = str(address_search[0])
        addr1 = address.split("\n\n")
        tempaddr = addr1[0]
        addr = str(tempaddr)
        ' '.join(addr.splitlines())
        addr = addr.strip()
    else:
        addr = ""

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

    chicken_search = re.search(
        r"Chicken Pox \(Varicella\):\n*([a-zA-Z0-9, \/]+)", text
        )
    if chicken_search is not None:
        chicken_search = chicken_search.groups()
        chicken = str(chicken_search[0])
        chicken = chicken.strip()
    else:
        chicken = ""

    measles_search = re.search(r"Measles:\n*([a-zA-z0-9, \/]+)\n*", text)
    if measles_search is not None:
        measles_search = measles_search.groups()    
        meas = str(measles_search[0])
        meas = meas.strip()
    else:
        meas = ""

    hepa_search = re.search(
        r"Have you had the Hepatitis B vaccination\?\n\n([a-zA-z0-9, ]+)", text
                            )
    if hepa_search is not None:
        hepa_search = hepa_search.groups()
        hepa = str(hepa_search[0])
        hepa = hepa.strip()
    else:
        hepa = ""

    med_search1 = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*Page", text
        )
    med_search = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*Create*", text
        )
    med_search2 = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*€}", text
        )
    med_search3 = re.search(
        r"headaches\)\:\n*([0-9A-Za-z\n\s,.\/]+)\n*Name", text
        )

    if med_search is not None:
        med_search = med_search.groups()
        medess = str(med_search[0])
        med = medess.strip()
    elif med_search1 is not None:
        med_search1 = med_search1.groups()
        medess = str(med_search1[0])
        med = medess.strip()
    elif med_search2 is not None:
        med_search2 = med_search2.groups()
        med2 = str(med_search2[0])
        med = med2.strip()
    elif med_search3 is not None:
        med_search3 = med_search3.groups()
        med2 = str(med_search3[0])
        med = med2.strip()
    else:
        med = ""

    ins_search = re.search(r"Name of Insurance Company:\n*([a-zA-Z, ]+)", text)
    if ins_search is not None:
        ins_search = ins_search.groups()
        insurance = str(ins_search[0])
        insurance = insurance.strip()
    else:
        insurance = ""

    pol_search = re.search(r"Policy Number:\n*[a-zA-Z\s, ]*([0-9]+)", text)
    if pol_search is not None:
        pol_search = pol_search.groups()
        policyno = str(pol_search[0])
        policyno = policyno.strip()
    else:
        policyno = ""

    exp_search = re.search(r"Expiry Date:\n*([a-zA-Z0-9, ]+)", text)
    if exp_search is not None:
        exp_search = exp_search.groups()
        expdate = str(exp_search[0])
        expdate = expdate.strip()
    else:
        expdate = ""

    hm_search = re.search(
        r"Do you have medical insurance\?\n*([a-zA-Z0-9, \/]+)", text
        )
    if hm_search is not None:
        hm_search = hm_search.groups()
        havemed = str(hm_search[0])
        havemed = havemed.strip()
    else:
        havemed = ""

    allergies_search = re.search(
        r"List any allergies:\n*([0-9A-Za-z\n\s,.\/]+)\n\n", text
        )
    if allergies_search is not None:
        allergies_search = allergies_search.groups()
        allergies = str(allergies_search[0])
        alrg1 = allergies.split("\n\n")
        temp_alrg = alrg1[0]
        alrg = str(temp_alrg)
        alrg.replace("\n", " ")
        alrg = alrg.strip()
    else:
        alrg = ""

    madication_search = re.search(r"List any medication taken regularly:\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*Create*", text) # noqa
    mad = re.search(r"Expiry Date:\n*[a-zA-Z0-9, ]+\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*Create*", text) # noqa
    mad2 = re.search(r"Expiry Date:\n*[a-zA-Z0-9, ]+\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*€}", text) # noqa
    mad3 = re.search(r"List any medication taken regularly:\n*([0-9A-Za-z\n\n\s,. \/\:]+)\n*", text) # noqa

    if mad is not None:
        mad = mad.groups()
        mad = str(mad[0])
        madication = mad.strip()
    elif madication_search is not None:
        madication_search = madication_search.groups()
        madication_temp = str(madication_search[0])
        madication = madication_temp.strip()
    elif mad2 is not None:
        mad2 = mad2.groups()
        mad2 = str(mad2[0])
        madication = mad2.strip()
    elif mad3 is not None:
        mad3 = mad3.groups()
        mad2 = str(mad3[0])
        madication = mad2.strip()
    else:
        madication = ""

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
            ("address", addr)
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
            ("Chicken Pox (Varicella)", chicken),
            ("Measles", meas),
            ("Have you had the Hepatitis B vaccination?", hepa),
            ("Medical Problems", med),
            ("Name of Insuarance Company", insurance),
            ("Policy Number", policyno),
            ("Expiry Date", expdate),
            ("Have medical insurance?", havemed),
            ("Any Allergies", alrg),
            ("Any Medications Regularly", madication)
            ]
         )
    ]
    return patient
