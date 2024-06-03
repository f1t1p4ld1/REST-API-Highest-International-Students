import requests

def getAllUniversities():
    page = 1
    allUniversities = []
    while True:
        url = f'https://jsonmock.hackerrank.com/api/universities?page={page}'
        response = requests.get(url)
        data = response.json()
        allUniversities.extend(data['data'])
        if page >= data['total_pages']:
            break
        page += 1
    return allUniversities

def getHighestInCity(universities, city):
    cityLower = city.lower()
    maxInternationalStudents = -1
    bestUniversity = None
    for university in universities:
        universityCityLower = university['location']['city'].lower()
        if universityCityLower == cityLower:
            numInternationalStudents = int(university['international_students'].replace(',', ''))
            if numInternationalStudents > maxInternationalStudents:
                maxInternationalStudents = numInternationalStudents
                bestUniversity = university
    return bestUniversity

def highestInternationalStudents(firstCity, secondCity):
    universities = getAllUniversities()
    bestUniversityFirstCity = getHighestInCity(universities, firstCity)
    if bestUniversityFirstCity:
        return bestUniversityFirstCity['university']

    bestUniversitySecondCity = getHighestInCity(universities, secondCity)
    if bestUniversitySecondCity:
        return bestUniversitySecondCity['university']

    return None

if __name__ == '__main__':
    firstCity = "Pune"
    secondCity = "New Delhi"
    print(highestInternationalStudents(firstCity, secondCity))