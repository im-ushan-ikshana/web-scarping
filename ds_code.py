from bs4 import BeautifulSoup
import requests


# Get functions - these functions will be used to get the page and convert it to a soup object
def get_page(url):
    response = requests.get(url)
    return response.text, response

# Convert functions - these functions will be used to convert the page to a soup object
def convert_to_soup(html):
    return BeautifulSoup(html, 'lxml')

#find all classes
def findAllClasses(soup):
    return soup.find_all(class_=True)

def findAllIds(soup):
    return soup.find_all(id=True)

def findAllTags(soup):
    return soup.find_all(True)

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



def main():
    url =  "https://mit.kln.ac.lk/index.php/staff/academic-staff"
    htlm_file , response_code = get_page(url)
    
    if(response_code):
        soup = convert_to_soup(htlm_file)
        


if __name__ == "__main__":
    main()


    