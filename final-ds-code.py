import bs4
import requests
import re
import pandas as pnd
import requests
from requests.exceptions import ConnectionError, Timeout

def get_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return response.text, response
    except (ConnectionError, Timeout) as e:
        print(f"An error occurred: {e}")
        return None, None

def main():
    url = 'https://science.kln.ac.lk/depts/im/index.php/staff/academic-staff'
    html, response = get_page(url)
    if html is not None and response is not None:
        # Your code to parse the response goes here
        pass
    else:
        print("Failed to fetch the page.")

if __name__ == '__main__':
    main()


class Lecturer:
    def __init__(self):
        self.name = None
        self.designation = None
        self.room = None
        self.email = None
        self.phone = None
        self.specilization_area = None

def get_page(url):
    response = requests.get(url)
    return response.text, response

def convert_to_soup(html):
    return bs4.BeautifulSoup(html, 'lxml')

def init_lecturer(lecturer_obj, soup):
    lecturer_obj.name = soup.find('h3' , class_='sppb-addon-title').get_text()

    designation = soup.find('div', class_='sppb-addon sppb-addon-text-block').find('strong')
    if designation:
        lecturer_obj.designation = designation.get_text()
    
    # Extracting the email
    ancher_tags = soup('a')
    for ancher_tag in ancher_tags:
        if re.search(r'@', ancher_tag.text):
            lecturer_obj.email=ancher_tag.text

    #Extract contact number
    span_tags = soup('span')
    for span_tag in span_tags:
        if re.search(r'Phone',span_tag.text):
            lecturer_obj.phone=re.search(r"\+.+ext[0-9]{3}\)",span_tag.text).group() if re.search(r"\+.+ext[0-9]{3}\)",span_tag.text) else None

    #Extract room number
    for span_tag in span_tags:
        if re.search(r'Room', span_tag.text) and re.search(r"[A-Z][0-9].[0-9]{3}", span_tag.text):
        # person.room=span_tag.text[8:14]
            lecturer_obj.room = re.search(r"[A-Z][0-9].[0-9]{3}",span_tag.text).group()
    
    all_specilizations = ""
    parent_divs = soup('div', class_="sppb-panel sppb-panel-modern")
    for parent_div in parent_divs:
        span_tags = parent_div.find_all('span')
        for span_tag in span_tags:
            if "Specialization" in span_tag.text:
                li_tags = parent_div.find_all('li')
                for li_tag in li_tags:
                    all_specilizations += li_tag.text + ", "
                lecturer_obj.specilization_area = all_specilizations
            


def findLinkToFullProfile(soup):
    anchor_tag = soup.find('a')
    if anchor_tag:
        if anchor_tag.text == 'View Full Profile':
            link_to_full_profile = anchor_tag['href']
            return link_to_full_profile

def csv_writer(data):
    df = pnd.DataFrame(data, columns=['Name', 'Designation', 'Room', 'Email', 'Phone', 'Specialization Area'])
    df.to_csv('lecturer_data.csv', index=False)
    print("Data saved to lecturer_data.csv")

def main():
    data = []
    url = 'https://science.kln.ac.lk/depts/im/index.php/staff/academic-staff'
    html, response = get_page(url)
    soup = convert_to_soup(html)
    if response.status_code == 200:
        LecturerSection = soup.find_all('div', class_='sppb-column-addons')
        for section in LecturerSection:
            link_for_full_profile = findLinkToFullProfile(section)
            if link_for_full_profile:
                html, response = get_page(link_for_full_profile)
                soup = convert_to_soup(html)
                if response.status_code == 200:
                    lecturer = Lecturer()
                    init_lecturer(lecturer, soup)
                    data.append([lecturer.name, lecturer.designation, lecturer.room, lecturer.email, lecturer.phone, lecturer.specilization_area])
    csv_writer(data)

if __name__ == '__main__':
    try:
        main()
    except (ConnectionError, Timeout) as e:
        print("Connection error occured. Please check your internet connection.")
    except PermissionError as e:
        print("Permission denied to write the file. Please close the file and try again.")
    except Exception as e:
        print(e)
        print("Error occured")
    finally:
        print("End of the program")


