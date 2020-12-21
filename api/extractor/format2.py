import re


def extract_details_format2(text):
    regex = "Preoperative History and Physical Exam([\n\r]*)([0-9/]+)([\n\r])+([a-zA-Z\- ]+)([\n\r]*)([0-9/]+)"
    search = re.search(regex, text).groups()
    name = search[3]
    name = " ".join(name.strip().split(",")[::-1]).strip()
    dob = search[-1]

    gender_regex = f"{name} is (a|an) ([0-9]+) y.o. (male|female|Male|Female|M|F|m|f)"
    gender_search = re.search(gender_regex, text).groups()
    gender = gender_search[2]
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
        }]
    return patient
