import pandas as pd
import csv

rows = []

df = pd.read_csv('final.csv')

df.drop(['Unnamed: 0'], axis = 1, inplace = True)

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity = []

def conversion(radius, mass):
    for a in range(0, len(radius) - 1):
        try:
            r1 = float(radius[a])
            m1 = float(mass[a])
            radius[a] = r1 * 6.957e+8
            mass[a] = m1 * 1.989e+30
        except Exception as err:
            radius[a] = 0
            mass[a] = 0
            continue

conversion(radius, mass)

def calculateGravity(radius, mass):
    G = 6.674e-11 
    for i in range(0, len(mass)):
        try:
            g = (mass[i] * G) / radius[i]**2 
            gravity.append(g)
        except Exception as err:
            gravity.append(0)
            continue

calculateGravity(radius, mass)
df['gravity'] = gravity

df.to_csv('detail.csv')