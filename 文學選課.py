import requests
from requests import status_codes
from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import schedule
import time
token="ZQTEJubMouLuf9MgHLoXrhnu0OyIXiZbruIiLP4PWWP"
drivePath="C:\\Users\a8911\Downloads\chromedriver.exe"

browser=webdriver.Chrome()
url='https://webapp.yuntech.edu.tw/AAXCCS/CourseSelectionRegister.aspx'

def lineNotifyMessage_text(token,msg):
    headers={
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload={'message':msg}
    print("[System]Line Notify connect complete")
    if(not msg ==''): 
        r=requests.post("https://notify-api.line.me/api/notify",headers=headers,params=payload)
  
    return r.status_code

def course(status):
    ans=''
    course_name_list=[]
    number_list=[]
    teacher_list=[]
    current_student_list=[]
    limit_student_list=[]
    browser.get(url)
    # browser.maximize_window()
    
    courseclass=Select(browser.find_element_by_id('ContentPlaceHolder1_MajOpDDL'))
    courseclass.select_by_visible_text("文學與創新興趣選項")

    button=browser.find_element_by_class_name("buttonGreen")
    button.click()
    # time.sleep(1)
    for  a in range(28):#to27
        course_name_ID=str("ContentPlaceHolder1_QueryCourseGridView_CourseEnameLabel_"+str(a))
        course_number_ID=str("ContentPlaceHolder1_QueryCourseGridView_ClassRoomLabel_"+str(a))
        course_teacher_ID=str("ContentPlaceHolder1_QueryCourseGridView_TeacherLabel_"+str(a))
        current_student_number_ID=str("ContentPlaceHolder1_QueryCourseGridView_SelNoLabel_"+str(a))
        limit_student_number_ID=str("ContentPlaceHolder1_QueryCourseGridView_MaxNoLabel_"+str(a))

        # course_name_list.append(browser.find_element_by_css_selector("td.text-left a").text)
        course_name_list.append(browser.find_element_by_id(course_name_ID).text)
        number_list.append(browser.find_element_by_id(course_number_ID).text)
        teacher_list.append(browser.find_element_by_id(course_teacher_ID).text)
        current_student_list.append(browser.find_element_by_id( current_student_number_ID).text)
        limit_student_list.append(browser.find_element_by_id(limit_student_number_ID).text)

    print("catch course success")
    length=len(number_list)
    for s in range(0,length):
        if("Creative Thinking" in course_name_list[s] or "Literature and Landscapes" in course_name_list[s]):
            # course_name_list.remove(course_name_list[s])
            # number_list.remove(number_list[s])
            # teacher_list.remove(teacher_list[s])
            # current_student_list.remove(current_student_list[s])
            # limit_student_list.remove(limit_student_list[s])
            continue
        # print("課程名稱-",course_name_list[s],"課程代碼-",number_list[s],"授課老師-",teacher_list[s],"修課人數-",current_student_list[s],"修課上限",limit_student_list[s])
        if(int(current_student_list[s])<int(limit_student_list[s])or not status):
            ans+="目前文學與創新課程有空缺!!"
            ans=ans+str("課程名稱-"+course_name_list[s]+"課程代碼-"+number_list[s]+"授課老師-"+teacher_list[s]+"修課人數-"+current_student_list[s]+"修課上限"+limit_student_list[s]+"\n\n")        
    if(ans==''):
        ans=''
    return ans

def login():
    try:
        browser.get('https://webapp.yuntech.edu.tw/YunTechSSO/Account/Login'  ) 
        # ------ address and password ------
        username = "B10923057"
        password = "cxz123499"
        # ------ enter address and password ------

        print("[System]Login condition prepare function not available please step by")
        elem = browser.find_element_by_id("pLoginName")
        elem.send_keys(username)
        print("[System]type in username OK")
        elem = browser.find_element_by_id("pLoginPassword")
        elem.send_keys(password)        
        print("[System]type in password OK")
        elem.send_keys(Keys.RETURN)
    except Exception as e:
        print(e)
        print("has logined")
    return True

def main():
    if(loginstatus):
        msg=course(True)
        code=lineNotifyMessage_text(token,msg)
        print("[System]",code)
    else:
        login()
        msg=course(True)
        code=lineNotifyMessage_text(token,msg)
        print("[System]",code)
def another():
    if(loginstatus):
        msg=course(False)
        code=lineNotifyMessage_text(token,msg)
        print("[System]",code)
    else:
        login()
        msg=course(False)
        code=lineNotifyMessage_text(token,msg)
        print("[System]",code)

schedule.every(3).hours.do(another)
loginstatus=login()
schedule.every(0.5).hours.do(main)
while True:  
    schedule.run_pending()  
    time.sleep(1)  
