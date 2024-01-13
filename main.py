#App to help in the saved challeng
import flet as ft
import os

def main(page: ft.Page):
    page.title = "Saved Challeng"
    #CHECK THE CONFIG
    if not os.path("config.txt"):
        print("dosent exist")
    else:
        #check that the file have the correct data format
        #for this i will create a script and import 
        print("I have config")
        #if the config is correct then update the data 
        # For this i will open a new file that it will be named 
        #  "saves.csv" in this will show the data of your saves
        ####################################################
        #else show the config page
        ####################################################
    def config_page():
        if not os.path.exists("config.txt"): #dosent exist then create
            try:
                with open("config.json", "x") as file_config:
                    file_config.write()
                    print("Archivo 'config.txt' creado y año guardado.")
            except FileExistsError:
                pass
            
            
            with open("config.txt", "r") as file_config:
                config_data = file_config.read()

        #
    page.add(
        ft.Row(
            [
                ft.Text(" ! ! "),
                ft.Text(" ~ ~ ~ "),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)