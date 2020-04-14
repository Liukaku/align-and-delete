from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


gjArray = [
    "Administration", 
    "Adult Services", 
    "Apprenticeship", 
    "Asset Management", 
    "Before and After School Clubs", 
    "Behavioural Support Services", 
    "Building Maintenance", 
    "Bus", 
    "Business Analysis", 
    "Career Guidance & Support", 
    "Caretaking, Cleaning" ,
    "Catering", 
    "Catering, Cleaning", 
    "Children's Services", 
    "Commissioning, Contracts", 
    "Communications, Marketing, PR", 
    "Community Safety", 
    "Coroner, Registrar", 
    "Customer Service", 
    "Democratic Services, Political", 
    "Driving", 
    "Early Years", 
    "Economic Development", 
    "Educational Psychology", 
    "Emergency Planning", 
    "Emergency Response", 
    "Engineering", 
    "Environmental Health", 
    "Events", 
    "Examinations", 
    "Family Work", 
    "Finance, Audit", 
    "Fire and Rescue", 
    "Fostering", 
    "Governor Services", 
    "Graduate", 
    "Health & Safety, Well-being", 
    "Highways", 
    "Highways, Transport, Traffic", 
    "Hospital Social Work", 
    "Hospitality", 
    "Human Resources", 
    "ICT", 
    "Information Governance, Data Protection, Freedom of Information", 
    "Leadership", 
    "Learning Disability", 
    "Learning, Training & Development", 
    "Learning, Training & Development", 
    "Legal Services", 
    "Library", 
    "Medical", 
    "Mental Health", 
    "Museum & Gallery", 
    "Older People", 
    "Organisation Development", 
    "Outdoor Adventure", 
    "Parks & Open Spaces", 
    "Passenger Assistants", 
    "Payroll, Pensions", 
    "Planning", 
    "Police", 
    "Policy, Business Analysis, Change & Transformation", 
    "Prevention & Protection", 
    "Project Management", 
    "Property Management", 
    "Public Health", 
    "Purchasing, Procurement", 
    "Quality Assurance", 
    "Rail/Light Rail", 
    "Regeneration", 
    "Revenues, Benefits", 
    "Safeguarding", 
    "School Admissions", 
    "School Business Management", 
    "School Crossing Patrol", 
    "School Improvement", 
    "School Leadership Teaching", 
    "School Support Staff", 
    "Schools Admissions", 
    "SEN Support", 
    "Sensory Service", 
    "Social Care Investigations", 
    "Sport & Fitness Instruction", 
    "Street Cleaning", 
    "Teacher", 
    "Teaching Assistant", 
    "Tenant Support", 
    "Theatre", 
    "Trading Standards", 
    "Traineeship", 
    "Transport", 
    "Tutor", 
    "Vehicle Maintenance", 
    "Volunteer", 
    "Waste Management", 
    "Work Experience", 
    "Work Placements", 
    "Youth Work"
]

categoryArray = [
    "Apprenticeships & Early Careers",
    "Blue Light",
    "Business & Corporate Services",
    "Consultants & Freelance",
    "Culture & Leisure",
    "Customer & Public Services",
    "Education - Non School",
    "Education - School",
    "Environment",
    "Health",
    "Housing",
    "Social Care",
    "Transport",
    "Volunteering"
]


siteAddress = ""
region = ""

userName = ""
pw = ""

catNumb = 0

#this is the council/employer/schools
employer = ""

jobCat = categoryArray[catNumb]

numb = 0


    
print(gjArray[numb])
#make a for or while loop that just goes through the array, and adds 1 to the end while numb < 98 loop

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=chrome_options)


driver.get( siteAddress + '/VacancyCategoryPaths.aspx')
    #you have to make sure that the siteAddress is an acual URL if you just put  then it wont work, INCLUDE HTTPS://
time.sleep(3)
driver.find_element_by_xpath('//*[@id="LoginCtrl_LoginCtrl_Login1_UserName"]').click()
driver.find_element_by_id('LoginCtrl_LoginCtrl_Login1_UserName').send_keys(userName, Keys.TAB)
driver.find_element_by_id('LoginCtrl_LoginCtrl_Login1_Password').send_keys(pw, Keys.ENTER)
time.sleep(10)



print("I'm working on the category " + categoryArray[catNumb])

while numb < 98 :
    driver.find_element_by_xpath('//*[@id="ctl00_ctl00_ctl00_Cph1_Cph1_rd2_T_AddAnchor"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ctl00_ctl00_ctl00_Access_FontCbo_Input"]').send_keys(Keys.TAB, Keys.TAB, Keys.TAB, region, Keys.TAB, employer, Keys.TAB, categoryArray[catNumb], Keys.TAB, gjArray[numb], Keys.TAB, Keys.ENTER)
    print(gjArray[numb])
    print(numb)
    numb += 1
    time.sleep(20)
    if numb == 98:
        if catNumb < 14:
            catNumb += 1
            print(categoryArray[catNumb])
            numb = 0


print("*************************************")
print("|                                   |")
print("|                                   |")
print("|                i                  |")
print("|               a m                 |")
print("|             ~done!~               |")
print("|                                   |")
print("|                                   |")
print("*************************************")


