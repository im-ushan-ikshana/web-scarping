from bs4 import BeautifulSoup
import requests


# Get functions - these functions will be used to get the page and convert it to a soup object
def get_page(url):
    response = requests.get(url)
    return response.text, response

# Convert functions - these functions will be used to convert the page to a soup object
def convert_to_soup(html):
    return BeautifulSoup(html, 'lxml')

# Find functions - these functions will be used to find elements in the soup object
def findGivenTag(soup, tag):
    return soup.find_all(tag)

def findGivenClass(soup, class_name):
    return soup.find_all(class_=class_name)

def findGivenId(soup, id_name):
    return soup.find_all(id=id_name)

def findGivenTagAndClass(soup, tag, class_name):
    return soup.find_all(tag, class_=class_name)

def findGivenTagAndId(soup, tag, id_name):
    return soup.find_all(tag, id=id_name)

def findGivenClassAndId(soup, class_name, id_name):
    return soup.find_all(class_=class_name, id=id_name)

#convert soup to readable text
def convertSoupToText(soup):
    return soup.get_text()

#get Lecturer name
def getLecturerName(soup):
    if soup:
        lecturer_name = soup.find('h3', class_='sppb-addon-title')
        if lecturer_name:
            return lecturer_name.get_text()
    else:
        return None

#get Lecturer - designation
def getLecturerDesignation(soup):
    if soup:
        lecturer_designation = soup.find('strong')
        if lecturer_designation:
            return lecturer_designation.get_text() if lecturer_designation else ""
    else:
        return None

def getLecturerDetails(soup):
    if soup:
        room = ""
        phone = ""
        email = ""
        fax = ""
        i = 0
        for lecturer_details in soup.find_all('p'):
            if i == 1:
                room = lecturer_details.get_text()
            elif i == 2:
                phone = lecturer_details.get_text()
            elif i >= 3:
                if lecturer_details.get_text().find("Email" or "email") != -1:
                    email = lecturer_details.get_text()
                if lecturer_details.get_text().find("Fax" or "fax") != -1:
                    fax = lecturer_details.get_text()
            i += 1
        return room, phone, email , fax   
    else:
        return None

# Print function - this function will be used to print the output   
def myPrinter(String_to_print):
    if String_to_print is not None and String_to_print.strip() != "":
        print(String_to_print)


def getSpecs(soup):
    if soup:
        tabs = soup.find_all('div', class_='sppb-panel sppb-panel-modern')
        for tab in tabs:
            if tab.get_text().find("Areas of Specialization") != -1:
                return tab.get_text().replace("Areas of Specialization", "")
    else:
        return None


def getSpecialization(url):
    html_file , response_code = get_page(url)
    if(response_code):
        soup = convert_to_soup(html_file)
        sectionSoup = findGivenClass(soup, 'sppb-addon-content')
        for Section in sectionSoup:
            myPrinter(getSpecs(Section))
            



def main():
    print("-------------------Start-------------------")
    url =  "https://mit.kln.ac.lk/index.php/staff/academic-staff"
    htlm_file , response_code = get_page(url)
    if(response_code):
        with open("details.csv", "w") as csv_file:
            soup = convert_to_soup(htlm_file)
            sectionSoup = findGivenClass(soup, 'sppb-section')
            for Section in sectionSoup:
                colomunSection = findGivenClass(Section, 'sppb-row')
                for innerSection in colomunSection:
                    name = getLecturerName(innerSection) if getLecturerName(innerSection) else ""
                    detailSection = findGivenClass(innerSection, 'sppb-addon sppb-addon-text-block sppb-text-left')
                    for innerInnerSection in detailSection:
                        designation = getLecturerDesignation(innerInnerSection) if getLecturerDesignation(innerInnerSection) else ""
                        #print(innerInnerSection)
                        room , phone , email , fax = getLecturerDetails(innerInnerSection) if getLecturerDetails(innerInnerSection) else "","","",""
                    getLinkSection = findGivenTagAndClass(innerSection, 'a', 'sppb-btn sppb-btn-custom sppb-btn-lg sppb-btn-round')
                    link_to_full_details = ""
                    for innerInnerSection in getLinkSection:
                        link_to_full_details = innerInnerSection.get('href') if innerInnerSection.get('href') else ""
                            
                    print("---------------------------------")
                    special = getSpecialization(link_to_full_details) if link_to_full_details else ""
                    myList = [name, designation, room, phone, email, fax, special]
                    if myList is not None:
                        csv_file.write(f"{name},{designation},{room},{phone},{email},{fax},{special}\n")
                       
                    print("---------------------------------")


                


        

if __name__ == "__main__":
    main()


    