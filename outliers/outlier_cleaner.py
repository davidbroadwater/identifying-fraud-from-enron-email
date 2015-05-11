#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here

    error = abs(predictions - net_worths)

    cleaned_data = sorted(zip(ages, net_worths, error), key=lambda item: item[2])

    cleaning_percentage = 10
    cleaning_index = int(float(100-cleaning_percentage)*len(cleaned_data)/100)


    cleaned_data = cleaned_data[:cleaning_index]

    
    return cleaned_data

