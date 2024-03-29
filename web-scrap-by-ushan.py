import bs4
import requests

url = "https://science.kln.ac.lk/depts/im/index.php/staff/academic-staff"
requestData = requests.get(url)


# Check the status of the request
def checkRequestStatus(request):
    '''
    Check the status of the request
    '''
    if request.status_code == 200:
        print("Request successful")
        return True
    elif request.status_code == 404:
        print("Page not found")
    elif request.status_code == 500:
        print("Internal server error")
    elif request.status_code == 403:
        print("Forbidden access")
    elif request.status_code == 503:
        print("Service unavailable")
    elif request.status_code == 504:
        print("Gateway timeout")
    elif request.status_code == 505:
        print("HTTP version not supported")
    else:
        print("Unknown error")
    
    return False

# Convert the request to a soup object
def convertRequestToSoup(request):
    '''
    Convert the request to a soup object
    '''
    if request:
        soup = bs4.BeautifulSoup(request.text, 'lxml')
        return soup
    else:
        return None


# Print the soup object
def printSoup(soup):
    '''
    Print the soup object
    '''
    if soup:
        print(soup.prettify())
    else:
        print("No soup object found")

# Get the lecturer sections
def getLecturerSections(soup):
    '''
    Get the lecturer sections
    '''
    if soup:
        lecturer_sections = soup.find_all('section', class_='sppb-section')
        return lecturer_sections
    else:
        return None

# Get the lecturer name
def getLecturerName(section):
    '''
    Get the lecturer name
    '''
    if section:
        lecturer_name_tag = section.find('h3', class_='sppb-addon-title')
        if lecturer_name_tag:
            lecturer_name = lecturer_name_tag.text.strip()
            return lecturer_name
    return "No lecturer name found"

# Get the lecturer email
def getLecturerEmail(section):
    '''
    Get the lecturer email
    '''
    if section:
        lecturer_email_tag = section.find('a')
        if lecturer_email_tag:
            lecturer_email = lecturer_email_tag.text.strip()
            return lecturer_email
    return "No email found"


# Main function
def main():
    '''
    Main function
    '''
    if checkRequestStatus(requestData):
        soup = convertRequestToSoup(requestData)
        lecturer_sections = getLecturerSections(soup)
        for section in lecturer_sections:
            lecturer_name = getLecturerName(section)
            lecturer_email = getLecturerEmail(section)
            print(f'{lecturer_name} \temail - {lecturer_email}')


if __name__ == "__main__":
    main()

