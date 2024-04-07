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

# Print function - this function will be used to print the output   
def myPrinter(String_to_print):
    if String_to_print is not None and String_to_print.strip() != "":
        print(String_to_print)


def main():
    print("-------------------Start-------------------")
    url =  "https://mit.kln.ac.lk/index.php/staff/academic-staff"
    htlm_file , response_code = get_page(url)
    if(response_code):
        soup = convert_to_soup(htlm_file)
        sectionSoup = findGivenClass(soup, 'sppb-section')
        for Section in sectionSoup:
            colomunSection = findGivenClass(Section, 'sppb-row')
            for innerSection in colomunSection:
                myPrinter(getLecturerName(innerSection))
                detailSection = findGivenClass(innerSection, 'sppb-addon-content')
                for innerInnerSection in detailSection:
                    myPrinter(getLecturerDesignation(innerInnerSection))
                    print(innerInnerSection)
                    print("\n")
                        

                


        

if __name__ == "__main__":
    main()


    