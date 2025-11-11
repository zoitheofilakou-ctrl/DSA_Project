### Record of weekly temperatures

def week_temp():

    #create a list with 7 temperatures
    temperatures = [12.5, 14.2, 15.8, 13.9, 11.6, 10.2, 12.0]
    print("Temperatures of the week",temperatures)

    #find mean
    mean_temp = sum(temperatures)/len(temperatures)
    print("Average weekly temperature:", round(mean_temp))

    #find a specific element-day = Wedenesday
    print("Wedensday's temperature is :", temperatures[3])


    #display min and max
    print("Highest temperature:", max(temperatures))
    print("Lowest temperature:", min(temperatures))

    # replace wrong temperature
    temperatures[2] = 15
    print("Corrected temperatutre", temperatures[2])

    #remove temperature
    remove= temperatures.pop() #delete last element
    print("Last day was removed", remove)

    #add temperature
    temperatures.append(18.2)
    print("One more day added:", temperatures)

if __name__ == "__main__":
    print("Run tests/test_arrays_lists.py to see the demo.")
    