import numpy as np
import pandas as pd

def calcula_raca(Dataframe):
    return Dataframe['race'].value_counts()

def avarage_age(Dataframe):
    avarageAge = Dataframe.loc[Dataframe['sex'].str.strip() == 'Male']
    return avarageAge['age'].mean()

def parcent_bachelor(Dataframe):
    haveBachelor = Dataframe.loc[Dataframe['education'].str.strip() == 'Bachelors']
    return ((haveBachelor['education'].count() * 100) / Dataframe['education'].count())

def salary_educaion(Dataframe):
    highEducation = Dataframe.loc[(Dataframe['education'].str.strip() == 'Bachelors') 
                                  | (Dataframe['education'].str.strip() == 'Masters')
                                  | (Dataframe['education'].str.strip() == 'Doctorate')]
    highEducation = highEducation.loc[highEducation['salary'].str.strip() == '>50K']
    return (highEducation['salary'].count() * 100) / Dataframe['salary'].count()

def low_education(Dataframe):
    lowEducation = Dataframe.loc[(Dataframe['education'].str.strip() != 'Bachelors') 
                                    & (Dataframe['education'].str.strip() != 'Masters')
                                    & (Dataframe['education'].str.strip() != 'Doctorate')]
    lowEducation = lowEducation.loc[lowEducation['salary'].str.strip() == '>50K']
    return (lowEducation['salary'].count() * 100) / Dataframe['salary'].count()

def min_hours(Dataframe):
    minimalHours = Dataframe.loc[Dataframe['hours-per-week'] == 
                                 Dataframe['hours-per-week'].min()]
    minimalHours = minimalHours.loc[minimalHours['salary'].str.strip() == '>50K']
    return (minimalHours['salary'].count()*100) / Dataframe['salary'].count()

def per_country(Dataframe):
        peoplePerCountry = Dataframe['native-country'].value_counts()
        moreThen50 = Dataframe.loc[Dataframe['salary'].str.strip() == '>50K']
        moreThen50 = moreThen50['native-country'].value_counts()
        return ((moreThen50 / peoplePerCountry) * 100).max()

def India(Dataframe):
    country = Dataframe.loc[Dataframe['native-country'].str.strip() == 'India']
    country = country.loc[country['salary'].str.strip() == '>50K']
    return country['occupation'].value_counts()

db_adultos = pd.read_csv('dados/adultData.csv')
db_adultos.columns = ['age','workclass', 'fnlwgt','education', 'education-num', 
            'marital-status', 'occupation', 'relationship', 'race', 
            'sex', 'capital-gain', 'capital-loss','hours-per-week',
            'native-country', 'salary']

print(db_adultos.head())

print("Races in database")
print(calcula_raca(db_adultos))

print('Average age of men')
print(avarage_age(db_adultos))

print(parcent_bachelor(db_adultos))

print(salary_educaion(db_adultos))

print(low_education(db_adultos))

print(db_adultos['hours-per-week'].min())

print(min_hours(db_adultos))

print(per_country(db_adultos))

print(India(db_adultos))



