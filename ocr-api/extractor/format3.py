import re


def extract_details_format3(text):
    name_regex = r"Name:[ ]*([a-zA-Z, -]+)"
    name_search = re.search(name_regex, text).groups()

    if name_search != None:
        name = str(name_search[0])

    name = " ".join(name.strip().split(",")[::-1]).strip()

#     gender_regex = r"Gender: ([M|F]?)([\s]*)Phone"
#     gender_search = re.search(gender_regex, text).groups()

#     if gender_search != None:
#         gender =  str(gender_search[0])

#     gender = gender.strip()

#     phone_regex = r"Phone:[ ]+([0-9\-]+)"
#     phone_search = re.search(phone_regex, text).groups()

#     if phone_search != None:
#         phone =  str(phone_search[0])

#     phone = phone.strip()

    dob_regex = r"DOB:[ ]*([0-9\/]+)"
    dob_search = re.search(dob_regex, text).groups()

    if dob_search != None:
        dob = str(dob_search[0])

    dob = dob.strip()

    gender_regex = f"{name} is (a|an) ([0-9]+) (year old|y.o.) (male|female|Male|Female|M|F|m|f)"
    gender_search = re.search(gender_regex, text).groups()
    gender = gender_search[-1]
    if gender.lower()[0] == "m":
        gender = "M"
    else:
        gender = "F"

    patient = [
        {
            "name": name,
            "gender": gender,
            #             "phone": phone,
            "dob": dob,
            #             "address": address
        }
    ]
    return patient
