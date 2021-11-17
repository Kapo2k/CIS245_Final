import requests


def weatherCity(city):  # function to return weather based on city
    try:

        response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="
                                + city + "&appid=684a46a1e6118f6296bc15243a21bb76")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if response.status_code == 200:  # if API status is good retrieve weather data
        response = response.json()
        temp = response['main']['temp']
        temp = round((temp * 1.8) - 459.67)
        weather = response['weather'][0]['main']
        description = response['weather'][0]['description']
        wind = response['wind']['speed']
        wind = round(wind * 0.000621371)
        print("Temperature: " + str(temp))
        print("Weather: " + weather + " (" + description + ")")
        print("Wind Speed: " + str(wind) + " mph")
    else:
        print("That City was invalid")


def weatherZip(zip):  # function to return weather based on zip
    try:
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + zip
                                + ",US&appid=684a46a1e6118f6296bc15243a21bb76")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if response.status_code == 200:
        response = response.json()
        temp = response['main']['temp']
        temp = round((temp * 1.8) - 459.67)
        weather = response['weather'][0]['main']
        description = response['weather'][0]['description']
        wind = response['wind']['speed']
        wind = round(wind * 0.000621371)
        print("Temperature: " + str(temp))
        print("Weather: " + weather + " (" + description + ")")
        print("Wind Speed: " + str(wind) + " mph")
    else:
        print("That Zip code was invalid")


def main():
    print("Welcome to the weather Program\n")
    keep_going = True
    while keep_going:  # loop to continue until user enters exit
        zip_or_city = input("\nEnter Zip code or City to retrieve weather data or type 'exit' to exit program: ")

        if zip_or_city.isdecimal():
            print("Retrieving weather from Zip: " + zip_or_city)
            weatherZip(zip_or_city)
        elif zip_or_city.lower() == 'exit':
            keep_going = False
        else:
            print("Retrieving weather from City: " + zip_or_city)
            weatherCity(zip_or_city)


if __name__ == "__main__":
    main()
