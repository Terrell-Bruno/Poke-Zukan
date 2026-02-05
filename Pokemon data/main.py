import pandas as pd
import pandas
import matplotlib as plt
import numpy as np
import csv

with open('pokemon.csv', 'r') as data:
    for line in csv.DictReader(data):
        print(line)

insert_data = pandas.read_csv('pokemon.csv')