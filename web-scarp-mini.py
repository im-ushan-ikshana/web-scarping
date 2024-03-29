from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://science.kln.ac.lk/depts/im/index.php/staff/academic-staff').text
soup = BeautifulSoup(html_text, 'lxml')

lecturer_sections = soup.find_all('section', class_='sppb-section')

for section in lecturer_sections:
    lecturer_name_tag = section.find('h3', class_='sppb-addon-title')
    lecturer_email_tag = section.find('a')

    if lecturer_name_tag:
        lecturer_name = lecturer_name_tag.text.strip()
        # print(lecturer_name)

    if lecturer_email_tag:
        lecturer_email = lecturer_email_tag.text.strip()
        print(f'{lecturer_name} \temail - {lecturer_email}')