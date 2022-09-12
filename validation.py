import re

re_pkpvd = r'(PKPVD\-\d{4,4}\-\d{2,2}\-\d{2,2}\-\d+)'
re_pkpvdmfc = r'(PKPVDMFC\-\d{4,4}\-\d{2,2}\-\d{2,2}\-\d+)'
re_ofsite = r'(OfSite\-\d{4,4}\-\d{2,2}\-\d{2,2}\-\d+)'
re_other = r'(Other\-\d{4,4}\-\d{2,2}\-\d{2,2}\-\d+)'
re_vedomstvo = r'(Vedomstvo\-\d{4,4}\-\d{2,2}\-\d{2,2}\-\d+)'

def validate(str):
    return re.search(re_pkpvd, str) or re.search(re_pkpvdmfc, str) or re.search(re_ofsite, str) or re.search(re_other, str) or re.search(re_vedomstvo, str)