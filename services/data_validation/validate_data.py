import ipaddress 

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

def validate_ip_abuse(abuse_jdata):
    if "data" in abuse_jdata and "ipAddress" in abuse_jdata["data"]\
        and "abuseCategories" in abuse_jdata["data"]and abuse_jdata["ipAddress"]\
            and len(abuse_jdata["abuseCategories"])>0 and validate_ip_address(abuse_jdata["data"]["ipAddress"]):
        return True
    return False

