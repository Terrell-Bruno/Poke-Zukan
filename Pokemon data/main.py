import pandas as pd
import pandas
import matplotlib.pyplot as plt
import numpy as np
import csv

with open('pokemon.csv', 'r') as data:
    for line in csv.DictReader(data):
        print(line)

insert_data = pandas.read_csv('pokemon.csv')

dict.count(insert_data["Type 1"])

print(insert_data["Name"])

plt.pie(insert_data["Type 1"])
plt.show()