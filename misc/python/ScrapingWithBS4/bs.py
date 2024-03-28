from bs4 import BeautifulSoup
#Soup = BeautifulSoup
#import BeautifulSoup

html= """<html>
<input autocomplete="off" name="lsd" type="hidden" value="AVqQVmuN"/> 

<input autocomplete="off" id="display" name="display" type="hidden" value=""/> 

<input autocomplete="off" id="enable_profile_selector" name="enable_profile_selector" type="hidden" value=""/> 

<input autocomplete="off" id="isprivate" name="isprivate" type="hidden" value=""/> 

<input autocomplete="off" id="legacy_return" name="legacy_return" type="hidden" value="0"/> 

<input autocomplete="off" id="profile_selector_ids" name="profile_selector_ids" type="hidden" value=""/> 

<input autocomplete="off" id="return_session" name="return_session" type="hidden" value=""/> 

<input autocomplete="off" id="skip_api_login" name="skip_api_login" type="hidden" value=""/> 

<input autocomplete="off" id="signed_next" name="signed_next" type="hidden" value=""/> 
"""

#html = requests.get(url)
#soup = BeautifulSoup(html.content, 'html.parser')
#print html
soup = BeautifulSoup(html,'html.parser')
#print soup
f = soup.find_all('input')
elements = soup.find_all('input')
for element in elements:
     print element['autocomplete']
     for key in element:
       print key 
#print(values)
#print type(f), f
