import re


def extract_details_format4(text):
    name_regex = r"Patient:[ ]*([a-zA-Z, -]+)[ ]*DOB"
    name_search = re.search(name_regex, text).groups()

    if name_search != None:
        name = str(name_search[0])

    name = " ".join(name.strip().split(",")[::-1]).strip()

    dob_regex = r"DOB:[ ]*([0-9\/]+)[ ]*Visit"
    dob_search = re.search(dob_regex, text).groups()

    if dob_search != None:
        dob = str(dob_search[0])

    dob = dob.strip()

    gender_regex = f"(sex|gender|SEX|Sex|Gender|GENDER):[ ]*(male|female|Male|Female|M|F|m|f)"
    gender_search = re.search(gender_regex, text).groups()
    gender = gender_search[-1]
    if gender.lower()[0] == "m":
        gender = "M"
    else:
        gender = "F"

    address_regex = r"Address:[ ]*([0-9A-Za-z\n\s\- ,]+) Pref."
    address_search = re.search(address_regex, text).groups()

    if address_search != None:
        address = str(address_search[0])

    address = address.strip()

    phone_regex = "Pref.[ ]*Phone\([A-Za-z]+\):[ ]*([0-9\-]*)"
    phone_search = re.search(phone_regex, text).groups()
    if phone_search != None:
        print(phone_search)
        phone = str(phone_search[-1])

    phone = phone.strip()

    referred_by_regex = r"Referred[ ]*By:[ ]*([a-zA-Z, -]+)"
    referred_by_search = re.search(referred_by_regex, text).groups()

    if referred_by_search != None:
        referred_by = str(referred_by_search[0])

    referred_by = " ".join(referred_by.strip().split(",")[::-1]).strip()

    patient = [
        {
            "name": name,
            "gender": gender,
            "phone": phone,
            "dob": dob,
            "address": address,
            "referred_by": referred_by
        }
    ]

    return patient
