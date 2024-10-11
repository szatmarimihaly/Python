import requests

api_key = "api key here"

def get_weather_data(city):
    return requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")

def display_menu():
    print("\n-------------------------")
    print("Weather Information Menu:")
    print("-------------------------")
    print("1. Current Weather Condition")
    print("2. Current Temperature")
    print("3. Max and Min Temperature")
    print("4. Feels Like Temperature")
    print("5. Wind Speed")
    print("6. City and Country")
    print("7. Enter New City")
    print("8. Exit")

def ask_city():
    return input("Enter City: ")

#display_menu()
#enter = input('Enter your choice:')

def main():
    city = ask_city()
    weather_data = get_weather_data(city)

    while weather_data.status_code == 200:
        weather = weather_data.json()['weather'][0]['main']
        temp = weather_data.json()['main']['temp']
        max_temp = weather_data.json()['main']['temp_max']
        min_temp = weather_data.json()['main']['temp_min']
        feels_temp = weather_data.json()['main']['feels_like']
        wind_speed = weather_data.json()['wind']['speed']
        country = weather_data.json()['sys']['country']
        city_name = weather_data.json()['name']

        while True:
            display_menu()
            enter = input("Enter your option:")

            if enter == "1":
                print(f'\n Current Weather Condition: {weather}')

            elif enter == "2":
                print(f'\n Current Temperature: {temp}°C')

            elif enter == "3":
                print(f'\n The maximum temperature today is {max_temp}°C')
                print(f'The minimum temperature today is {min_temp}°C')

            elif enter == "4":
                print(f'\n The temperature today feels like: {feels_temp}°C')

            elif enter == "5":
                print(f'\n The wind speed today is {wind_speed} km/h')

            elif enter == "6":
                print(f'\n The city is: {city_name}, Country is: {country}')

            elif enter == "7":
                city = ask_city()
                weather_data = get_weather_data(city)
                if weather_data.status_code != 200:
                    print(f"Error: Unable to fetch weather data for {city}. Please check the city name.")
                else:
                    break

            elif enter == "8":
                print('Exiting the program...')
                return
            else:
                print(f'Invalid option ({enter}), please try again.')
                
    else:
        print(f'Error: Unable to fetch weather data for {city}, please check the city name again.')
        city = ask_city()

#Run the weather app
main()



