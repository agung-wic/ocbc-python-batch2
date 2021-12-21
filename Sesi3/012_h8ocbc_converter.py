def convKelvinToCelcius(degree, tipe='kelvinToCelcius'):
    '''
    This function is used to convert the temperature from Celsius to Kelvin or Kelvin to Celsius.
    :param degree: Input number | int or float
    :param tipe: Input string | string with value kelvinToCelcius(default) or celciusToKelvin

    :return: degree: Converted temperature | int or float
    '''
    if(tipe == 'kelvinToCelcius'): # If tipe equal to 'kelvinToCelcius' then return converted temperature from kelvin to celcius
        return (degree-273.15)
    elif(tipe == 'celciusToKelvin'): # If tipe equal to 'celciusToKelvin' then return converted temperature from celcius to kelvin
        return degree+273.15


def toFahrenheit(degree, tipe):
    '''
    This function is used to convert the temperature from Celsius or Kelvin to Fahrenheit.
    :param degree: Input number | int or float
    :param tipe: Input string | string with value kelvin or celsius

    :return: degree: Converted temperature | int or float
    '''
    if(tipe == 'celcius'): # If tipe equal to 'celcius' then return converted temperature from celcius to fahrenheit
        return (degree*9/5)+32
    elif(tipe == 'kelvin'): # If tipe equal to 'kelvin' then call the convertKelvinToCelcius function with tipe='kelvinToCelcius' and return converted temperature to fahrenheit
        return ((convKelvinToCelcius(degree, tipe='kelvinToCelcius')*9/5)+32)


def fromFahrenheit(degree, tipe):
    '''
    This function is used to convert the temperature from Fahrenheit to Celsius or Kelvin.
    :param degree: Input number | int or float
    :param tipe: Input string | string with value kelvin or celcius

    :return: degree: Converted temperature | int or float
    '''
    if(tipe == 'celcius'): # If tipe equal to 'celcius' then return converted temperature from fahrenheit to celcius
        return (degree-32)*5/9
    elif(tipe == 'kelvin'): # If tipe equal to 'kelvin' then convert fahrenheit to celcius first, call the convertKelvinToCelcius function with tipe='celciusToKelvin and return the value'
        return convKelvinToCelcius((degree-32)*5/9, tipe='celciusToKelvin')


if (__name__ == '__main__'):
    '''
    This function is used to get user input from the keyboard and run a function that the user chooses. This is a void function and always run when this python file run
    :no params required

    :no returned value, just print converted temperature from another function 
    '''
    repeat = 'Y' # variable to repeat the temperature converter menu
    while(repeat=='Y'):
        print('---------------------')
        print('Temperature Converter')
        print('---------------------')
        print('         Menu')
        print('1. Kelvin To Celcius')
        print('2. Celcius To Kelvin')
        print('3. Kelvin To Fahrenheit')
        print('4. Celcius To Fahrenheit')
        print('5. Fahrenheit To Kelvin')
        print('6. Fahrenheit To Celsius')
        print('7. Exit')
        inputNumber = input('Select menu: ') # variable to catch inputed keyboard from user
        if (inputNumber=='1'):
            degree = float(input('Enter Temperature: '))
            print("%.2f C" % convKelvinToCelcius(degree, 'kelvinToCelcius'))
        elif(inputNumber=='2'):
            degree = float(input('Enter Temperature: '))
            print("%.2f K" % convKelvinToCelcius(degree, 'celciusToKelvin'))
        elif(inputNumber=='3'):
            degree = float(input('Enter Temperature: '))
            print("%.2f F" % toFahrenheit(degree, 'kelvin'))
        elif(inputNumber=='4'):
            degree = float(input('Enter Temperature: '))
            print("%.2f F" % toFahrenheit(degree, 'celcius'))
        elif(inputNumber=='5'):
            degree = float(input('Enter Temperature: '))
            print("%.2f K" % fromFahrenheit(degree, 'kelvin'))
        elif(inputNumber=='6'):
            degree = float(input('Enter Temperature: '))
            print("%.2f C" % fromFahrenheit(degree, 'celcius'))
        elif(inputNumber=='7'):
            break
        else:
            print("Invalid menu number") # If the inputed value from keyboard out of 1-7 then print invalid number
        menuNumber = input("Repeat again (Y/n)?") # Varible to cacth inputed keyboar from the user, want to repeat again or not
        if (menuNumber=='Y' or menuNumber==''): # If the value of menuNumber either 'Y' or '' then repeat the process
            repeat='Y'
        else: # If the value of menuNumber neither 'Y' nor '' then close the process
            repeat='N'