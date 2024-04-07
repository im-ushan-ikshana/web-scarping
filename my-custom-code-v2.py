from bs4 import BeautifulSoup
import requests
import re

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

def findGivenTagClassAndId(soup, tag, class_name, id_name):
    return soup.find_all(tag, class_=class_name, id=id_name)



#check the request status
def checkRequestStatus(request):
    if request.status_code == 200:
        return True
    elif request.status_code == 404:
        print("Page not found")
    elif request.status_code == 403:
        print("Access denied")
    elif request.status_code == 505:
        print("HTTP version not supported")
    else:
        print("Unknown error")
    
    return False
    
#get Lecturer sections
def getLecturerSections(soup):
    if soup:
        lecturer_sections = soup.find_all('section', class_='sppb-section')
        return lecturer_sections
    else:
        return None

#get basic details of a  Lecturer
def getName(soup):
    if soup:
        name_tag = soup.find('h3')
        if name_tag:
            name = name_tag.text
            return name
        else:
            return None
    else:
        return None
    
def getDesignation(soup):
    if soup:
        designation_tags = soup.find_all(class_='sppb-addon-text-block')  # Find all elements with the specified class
        designations = []  # Initialize an empty list to store designations
        for designation_tag in designation_tags:  # Iterate through found elements
            p_tag = designation_tag.find('p')  # Find the first <em> tag within the current element
            strong_tag = designation_tag.find('strong')  # Find the first <strong> tag within the current element
            if p_tag:  # If <em> tag is found, append its text to designations
                designations.append(p_tag.text.strip())
            elif strong_tag:  # If <strong> tag is found, append its text to designations
                designations.append(strong_tag.text.strip())
            else:  # If neither <em> nor <strong> tag is found, append None
                designations.append("")
        return designations if designations else None  # Return the list of designations or None if empty
    else:
        return None

# Get other details of a Lecturer
def getOtherDetails(soup):
    if soup:
        other_details = soup.find_all(class_='sppb-addon-content')
        if other_details:  # Check if other_details is not empty
            details_text = ""
            for detail in other_details:
                p_elements = detail.find_all('p')  # Find all <p> elements within the current element
                for p_element in p_elements:
                    details_text += p_element.text.strip() + " \n"  # Append the text of each <p> element to details_text
            return details_text.strip()  # Return the concatenated text, stripping any leading/trailing whitespace
        else:
            return "empty"  # Return "empty" if other_details is empty
    else:
        return None


# get full deetails page link
def getFullDetailsLink(soup):
    if soup:
        fullDetailsLink = soup.find_all('div', class_='sppb-text-center')
        if fullDetailsLink:
            for link in fullDetailsLink:
                a_tag = link.find('a')
                if a_tag:
                    return a_tag['href']
                else:
                    return None
        else:
            return None

def getDetailsSection(soup):
    if soup:
        details_section = soup.find_all('div', class_='sppb-column-addons')
        return details_section
    else:
        return None

def getPanelGroupSection(soup):
    if soup:
        panel_group_section = soup.find_all('div', class_='sppb-panel-group')
        return panel_group_section
    else:
        return None

#get links to other sites
def getLinksToSites(soup):
    if soup:
        # Find all <p> elements within the soup
        find_path_to_links = soup.find_all('p')
        links_string = ""
        if find_path_to_links:
            for link in find_path_to_links:
                a_tag = link.find('a')
                if a_tag:
                    link_name = a_tag.text
                    link_url = a_tag['href'] # Extract the URL of the link
                    if link_url:
                        links_string += f"{link_name}: {link_url} \n"  # Concatenate the link name and URL
        return links_string.strip()  # Return the concatenated string, stripping any leading/trailing whitespace
    else:
        return ""  # Return an empty string if soup is None

def getAcademicQualifications(soup):
    soup = getPanelGroupSection(soup)
    if soup:
        academic_qualifications = []
        for section in soup:
            qualification = section.find('ul', class_='sppb-addon-content')
            if qualification == "Academic Qualifications":
                academic_qualifications.append(qualification.text.strip())
        return academic_qualifications if academic_qualifications else None
    else:
        return None

#convert list to string
def listToString(input_list):
    if input_list is None:
        return ""
    else:
        return ' '.join([str(elem) for elem in input_list])


url = "https://mit.kln.ac.lk/index.php/staff/academic-staff"
url2 = "https://science.kln.ac.lk/depts/im/index.php/staff/academic-staff"

def fullProfile(url):
    if url:
        html, req = get_page(url)
        if checkRequestStatus(req):
            soup = convert_to_soup(html)
            details = getDetailsSection(soup)
            full_details_text = ""  # Initialize an empty string to store the full details text
            for section in details:
                links_text = getLinksToSites(section)  # Get the links for the current section
                if links_text:  # If links are found, concatenate them with the full details text
                    full_details_text += links_text + "\n"  # Add the links text to the full details text
            if full_details_text:  # If there is any full details text, print it
                print(full_details_text.strip())  # Print the full details text after stripping leading/trailing whitespace
            panelsSet = getPanelGroupSection(soup)
            
    else:
        print("No link found")



def main():
    html, request = get_page(url)
    if checkRequestStatus(request):
        soup = convert_to_soup(html)
        lecturer_sections = getLecturerSections(soup)
        for section in lecturer_sections:
            name = getName(section)
            details = getOtherDetails(section)
            full_details_link = getFullDetailsLink(section)

            print(name)
            print(details)
            print("\nSites for More Details :")
            if full_details_link:
                fullProfile(full_details_link)
                print("\n")
            else:
                print("No Extra details link available")
                print("\n")

if __name__ == "__main__":
    main()


