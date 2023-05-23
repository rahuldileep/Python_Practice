import slate
import re
import datefinder
from datetime import datetime, timedelta, date

def phone_num(name):
  num=re.compile(r'(\d{10})')
  if num.search(name) is not None:
    clean = num.search(name).group()
  else:
    clean = ""
  return(clean)  

def email_id(name):
  id=re.compile(r'[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-z]{2,4})')
  if id.search(name) is not None:
    clean =  id.search(name).group()
  else:
    clean = ""
  return(clean)

def college_univ(name):
  id=re.compile(r'([A-Za-z," ]+(college)+[A-Za-z," ]+)')
  #id = re.compile(r'[^.]* college [^.]*\.')
  if id.search(name) is not None:
    clean =  id.search(name).group()
    return(clean)


def tools(name):
  tool_list = ['sas', 'sql', 'tableau','html','sitecatalyst','python']
  tool = re.compile(r'\b(?:%s)\b' % '|'.join(tool_list))
  ls = []
  if tool.search(name) is not None:
    for match in tool.finditer(name):
        ls.append(match.group())
        #print(ls)
  return(ls)    
  
def dob(name):
    matches = datefinder.find_dates(name)
    for match in matches:
        if match < (datetime.today() - timedelta(days=7300)):
            return match

def calculate_age(born):
    today = date.today()
    years_difference = today.year - born.year
    is_before_birthday = (today.month, today.day) < (born.month, born.day)
    elapsed_years = years_difference - int(is_before_birthday)
    return elapsed_years


#/^(\d{1,4})-(\d{1,2})-(\d{1,2})$/

#opening the pdf in read-binary mode
with open('resume.pdf','rb') as f:
    doc = slate.PDF(f)

toolsl = []

#printing the doc

for page in doc:
    #type(page)
    if len(phone_num(page)) > 3:
        print('Phone Number: ' + phone_num(page))

    if len(email_id(page)) > 3:
        print('Email ID: ' + email_id(page))

    if dob(page) is not None:
        print('DOB: ' + str(dob(page).date()))
        print('Age: ' + str(calculate_age(dob(page).date())))

    if college_univ(page.lower()) is not None:
        print('Education: ' + str(college_univ(page.lower())))
    #print(page)
    if len(tools(page.lower())) > 1:
        #print('Tools: ')
        toolsl.append(list(set(tools(page.lower()))))
    
tools2 = sum(toolsl,[])
print('Tools:')
print(list(set(tools2)))