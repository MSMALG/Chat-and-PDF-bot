import streamlit as st
from streamlit_option_menu import option_menu
import application, pdfbot

st.set_page_config(
    page_title = "ZIKO",
    page_icon = "🤖"
)

#This class is the link between applicaton.py and pdfbot.py
class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append(
            {
                "title": title,
                "function": function
            }
        )
    def run():
        app = option_menu(
            menu_title='Choose your Bot',
            options=['ZIKO BOT', 'ZIKO PDF BOT'],
            default_index=1
        )

        if app == 'ZIKO BOT':
            application.main()
        
        if app == 'ZIKO PDF BOT':
            pdfbot.main()
    run()