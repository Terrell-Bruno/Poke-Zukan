import pandas as pd
import pandas
import matplotlib.pyplot as plt
import numpy as np
import csv
import customtkinter as ctk

data = pd.read_csv('pokemon.csv')

app = ctk.CTk()
app.geometry("1920x1080")
app.title("Poke-Zukan")
app.configure(fg_color="darkgray")

search_insert = ctk.CTkEntry(app,
                             placeholder_text="Search Pokemon")
search_insert.grid(padx=0,
                   pady=0,
                   column=0,
                   row=0)

search_button = ctk.CTkButton(app,
                              text="Search")
search_button.grid(padx=0,
                   pady=0,
                   column=0,
                   row=0)

Title = ctk.CTkLabel(app,
                      text="Poke-Zukan Searcher"
                      )
Title.grid(padx=960,
            pady=50,
           column=0,
           row=0)

pokemon_types = {
    "Fire": 0,
    "Water": 0,
    "Grass": 0,
    "Dark": 0,
    "Fairy": 0,
    "Dragon": 0,
    "Ice": 0,
    "Ground": 0,
    "Rock": 0,
    "Ghost": 0,
    "Steel": 0,
    "Flying": 0,
    "Bug": 0,
    "Fighting": 0,
    "Normal": 0,
    "Psychic": 0,
    "Electric": 0,
    "Poison": 0,
    }

app.mainloop()