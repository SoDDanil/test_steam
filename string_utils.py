import re

class StringUtils():
    def get_replace(string):
        return int(string.replace(',',''))
    def get_regular(string):
        return re.findall('\d{1,3},\d{1,3},\d{1,3}',string)