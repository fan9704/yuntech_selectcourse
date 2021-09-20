import requests
from requests import status_codes
from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import schedule
import time

token="ZQTEJubMouLuf9MgHLoXrhnu0OyIXiZbruIiLP4PWWP"#line notify token
drivePath="C:\\Users\a8911\Downloads\chromedriver.exe"#chromedriver path

browser=webdriver.Chrome()#open browser
url='https://webapp.yuntech.edu.tw/AAXCCS/CourseSelectionRegister.aspx'

def lineNotifyMessage_text(token,msg):#send message to line notify
    headers={
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload={'message':msg}#deal message
    print("[System]",time.strftime(" %I:%M:%S %p",time.localtime()), " Line Notify connect complete")
    if(not msg ==''): 
        r=requests.post("https://notify-api.line.me/api/notify",headers=headers,params=payload)#post it
        return r.status_code

def course(status):
    ans=''#create reply answer
    course_name_list=[]#create all list
    number_list=[]
    teacher_list=[]
    current_student_list=[]
    limit_student_list=[]
    weekday_list=['',"星期一","星期二","星期三","星期四","星期五"]
    browser.get(url)
    # browser.maximize_window()
    
    courseclass=Select(browser.find_element_by_id('ContentPlaceHolder1_MajOpDDL'))#course option
    courseclass.select_by_visible_text("通識")#course option

    weekdaybox=browser.find_element_by_id(str('ContentPlaceHolder1_WeekCB'+str(status)))#Monday checkbox
    weekdaybox.click()


    button=browser.find_element_by_class_name("buttonGreen")#button of send
    button.click()#click button

    courselength=int(browser.find_element_by_id("ContentPlaceHolder1_QueryTotalRowLabel").text)
    # print("通識門數",courselength)
    for  a in range(courselength):
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
    print(teacher_list)
    print("[System]",time.strftime(" %I:%M:%S %p",time.localtime()),"Weekday",status," catch course success")
    length=len(number_list)
    for s in range(0,length):
        if("Creative Thinking" in course_name_list[s] or "Literature and Landscapes" in course_name_list[s] or limit_student_list[s] == '' or "待聘" == teacher_list[s]):#bind creative thinking and literature and landscapes
            continue
        #print("課程名稱-",course_name_list[s],"課程代碼-",number_list[s],"授課老師-",teacher_list[s],"修課人數-",current_student_list[s],"修課上限",limit_student_list[s])
        if(int(current_student_list[s])<int(limit_student_list[s])):#compare list
            ans+="目前"+weekday_list[status]+"通識課程有空缺!!"
            ans=ans+str("\n課程名稱-"+course_name_list[s]+" 課程代碼-"+number_list[s]+" 授課老師-"+teacher_list[s]+" 修課人數-"+current_student_list[s]+" 修課上限"+limit_student_list[s]+"\n\n")        
    if(ans==''):
        ans=''
    return ans

def login():
    try:
        browser.get('https://webapp.yuntech.edu.tw/YunTechSSO/Account/Login'  ) #login form
        # ------ address and password ------
        username = "B10923057"
        password = "cxz123499"
        # ------ enter address and password ------

        print("[System]",time.strftime(" %I:%M:%S %p",time.localtime())," Login condition prepare function not available please step by")
        elem = browser.find_element_by_id("pLoginName")#login input
        elem.send_keys(username)#key in username
        print("[System]",time.strftime(" %I:%M:%S %p",time.localtime())," type in username OK")
        elem = browser.find_element_by_id("pLoginPassword")#password input
        elem.send_keys(password)        #key in password
        print("[System]",time.strftime(" %I:%M:%S %p",time.localtime())," type in password OK")
        elem.send_keys(Keys.RETURN)
    except Exception as e:
        print(e)
        print("[System]",time.strftime(" %I:%M:%S %p",time.localtime()),"has logined")#login condition
    return True

def main():
    if(loginstatus):
        msg=""
        for i in range(1,6):
            ans=course(i)
            msg+=ans
        code=lineNotifyMessage_text(token,msg)
        print("[System]",time.strftime(" %I:%M:%S %p",time.localtime())," ",code)
    else:
        login()
        msg=""
        for i in range(1,6):
            ans=course(i)
            msg+=ans
        code=lineNotifyMessage_text(token,msg)
        print("[System]",time.strftime(" %I:%M:%S %p",time.localtime())," ",code)

# schedule.every(3).hours.do(another)
loginstatus=login()#login event
schedule.every(0.1).minutes.do(main)
while True:  
    schedule.run_pending()  #scheduling
    time.sleep(1)  
