import re


def extract_details_format1(text):
    name_regex = r"Patient Information\n([a-zA-Z0-9, ]+)"
    name_search = re.search(name_regex, text).groups()

    if name_search != None:
        name = str(name_search[0])
    
    name = " ".join(name.strip().split(",")[::-1]).strip()
    # gender_regex = r"Gender: ([M|F]?)([\s]*)Phone"
    # gender_search = re.search(gender_regex, text).groups()

    # if gender_search != None:
    #     gender = str(gender_search[0])

    # gender = gender.strip()
    phone_search = re.search(r"(\([\d]+\) [\d]+\-[\d]+)", text).groups()
    print(phone_search)
    if phone_search != None:
        phone = str(phone_search[0])
        

    phone = phone.strip()


    dob_regex = r"Birth Date\n([A-Za-z0-9, ]+)"
    dob_search = re.search(dob_regex, text).groups()

    if dob_search != None:
        dob = str(dob_search[0])

    dob = dob.strip()

    height_search=re.search(r"Height:\n([\d]+)", text).groups()
    if height_search != None:
        height = str(height_search[0])
    height = height.strip()

    weight_search=re.search(r"Weight:\n([\d]+)", text).groups()
    if weight_search != None:
        weight = str(weight_search[0])
    weight = weight.strip()

    address_search=re.search(r"\([\d]+\) [\d]+\-[\d]+\n\n([0-9A-Za-z\n\s\,]+)", text).groups()
    addr=""
    if address_search != None:
        address = str(address_search[0])
        addr1=address.split("\n\n")
        tempaddr=addr1[0]
        addr=str(tempaddr)
    addr.replace("\n"," ")
    addr = addr.strip()


    emr_name=re.search(r"Case of Emergency\n\n([a-zA-Z0-9, ]+)", text).groups()
    if emr_name != None:
        ename = str(emr_name[0])
    ename = ename.strip()

    emr_addr=re.search(r"Height:\n[\d]+\n\n([0-9A-Za-z\n\s\,]+)", text).groups()
    if emr_addr != None:
        emr_add = str(emr_addr[0])
        emr_add1=emr_add.split("\n\n")
        tempemr=emr_add1[0]
        emr_addr=str(tempemr)
    emr_addr.replace("\n"," ")
    emr_addr = emr_addr.strip()
    
    home_phone=re.search(r"Home phone\n(\([\d]+\) [\d]+\-[\d]+)", text).groups()
    if home_phone != None:
        home = str(home_phone[0])
    home = home.strip()

    work_phone=re.search(r"Work phone\n(\([\d]+\) [\d]+\-[\d]+)", text).groups()
    if work_phone != None:
        work = str(work_phone[0])
    work = work.strip()

    chicken_search=re.search(r"Chicken Pox \(Varicella\):\n*([a-zA-Z0-9, ]+)", text).groups()
    if chicken_search != None:
        chicken = str(chicken_search[0])
    chicken = chicken.strip()

    measles_search=re.search(r"Measles:\n\n([a-zA-z0-9, ]+)", text).groups()
    if measles_search != None:
        meas = str(measles_search[0])
    meas = meas.strip()

    hepa_search=re.search(r"Have you had the Hepatitis B vaccination\?\n\n([a-zA-z0-9, ]+)", text).groups()
    if hepa_search != None:
        hepa = str(hepa_search[0])
    hepa = hepa.strip()

    med_search=re.search(r"headaches\)\:\n([0-9A-Za-z\n\n\s,.]+)\n\nPage", text).groups()
    if med_search != None:
        medess = str(med_search[0])
    med=medess.strip()


    ins_search=re.search(r"Name of Insurance Company:\n*([a-zA-Z0-9, ]+)", text).groups()
    if ins_search != None:
        insurance = str(ins_search[0])
    insurance = insurance.strip()
    
    pol_search=re.search(r"Policy Number:\n*([0-9]+)", text).groups()
    if pol_search != None:
        policyno = str(pol_search[0])
    policyno = policyno.strip()

    exp_search=re.search(r"Expiry Date:\n*([a-zA-Z0-9, ]+)", text).groups()
    if pol_search != None:
        expdate = str(exp_search[0])
    expdate = expdate.strip()

    hm_search=re.search(r"Do you have medical insurance\?\n*([a-zA-Z0-9, ]+)", text).groups()
    if pol_search != None:
        havemed = str(hm_search[0])
    havemed = havemed.strip()
    
  

    

    alrgess_search=re.search(r"List any allergies:\n*([0-9A-Za-z\n\s\,]+)", text).groups()
    if alrgess_search != None:
        alrgess = str(alrgess_search[0])
        alrg1=alrgess.split("\n\n")
        tempalrg=alrg1[0]
        alrg=str(tempalrg)
    alrg.replace("\n"," ")
    alrg=alrg.strip()


    madicationess_search=re.search(r"List any medication taken regularly:\n*([0-9A-Za-z\n\n\s,.]+)\n\n", text).groups()
    if madicationess_search != None:
        madicationess = str(madicationess_search[0])

    madication=madicationess.strip()


    
    
#     Date of Birth: 12/10/1948 Age: 70 y.o.
    # address_regex = r"Date of Birth:[ ]+[0-9\/]+[ ]*Age:[ ]*[0-7 ]+y.o.[\n]+Address:[ ]+([0-9A-Za-z\n\s]+)"
    # address_search = re.search(address_regex, text).groups()

    # if address_search != None:
    #     address = str(address_search[0])

    # address = address.strip()
    patient ={
            "name": name,
            # "gender": gender,
            "phone": phone,
            "dob": dob,
            "height": height,
            "weight": weight,
            "address": addr,
            "Emergency(name)": ename,
            "Emergency(Emergency Address)": emr_addr,
            "Emergency(home phone)": home,
            "Emergency(work phone)": work,
            "Chicken Pox (Varicella)" :chicken,
            "Measles": meas,
            "Have you had the Hepatitis B vaccination?":hepa,
            "Medical Problems":med,
            "Name of Insuarance Company":insurance,
            "Policy Number":policyno,
            "Expiry Date":expdate,
            "Have medical insurance?":havemed,
            "Any Allergies":alrg,
            "Any Medications Regularly":madication
            
           }

    
    return patient
