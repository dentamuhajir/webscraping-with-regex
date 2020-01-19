import requests
import re
import string

r = requests.get('http://sample.dentamuhajir.com/scrape')
c = r.content

content_one_line = c.replace('\r\n', '')

product_div_pattern = re.compile(r'product-item(.*?)\/span', flags = re.M)
category_name_pattern = re.compile(r'catagory-name">(.*?)<', flags = re.M)

get_product_div = product_div_pattern.findall(content_one_line)

num = 0
print "| No| Category\t| "
print " ----------------"
for x in get_product_div:
    num = num + 1
    get_category_name = category_name_pattern.findall(x)

    print "|",num,"|",string.join(get_category_name, " "),"\t|"

