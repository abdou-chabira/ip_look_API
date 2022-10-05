from faker import Faker
from db.ip_address_db import save_abuse_category
import random
fake=Faker()
print(fake.ipv4_public())

def lookup_ip_address(ip_address):
    location=fake.local_latlng()
    response={
        "id":str(fake.random_number(fix_len=False)),
        "ipAddress":ip_address,
        "location":{
            "country":location[3],
            "region":location[2],
            "city":fake.city(),
            "lat":float(location[0]),
            "lng":float(location[1]),
            "postalCode":fake.postcode(),
            "timezone":"-07:00"
        },
        "domains":[
            fake.domain_name(),
            fake.domain_name()
        ],
        "as":{
            "asn":fake.iana_id(),
            "name":fake.company(),
            "route":fake.ipv4_public()+"/24",
            "domain":fake.uri()
        },
        "isp":"Google LLC"
    }
    
    return response


def save_report_ip_abuse(abuse_jdata):
    abuse_report_data=[]
    for category in abuse_jdata["data"]["abuseCategories"]:
        ip_abuse_report_resp=save_abuse_category(abuse_jdata["data"]["ipAddress"],int(category))
        abuse_report_data.append(ip_abuse_report_resp)
    return abuse_report_data



    