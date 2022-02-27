# yuntech_selectcourse
choose course automatically  and auto login yuntechSSO

Install all dependencies
```cmd=
pipenv install
```
Renew your google chrome and your chrome driver in this project folder
[Chrome Driver Download Link](https://chromedriver.chromium.org/)

webdriver version should match your browser

### Login Your Yuntech SSO and send notify to you line account
add ".env" file in this project
Don,t add "" in parameter
Content=>
SSO_username = S_id
SSO_password = S_password
token = line_notify_token