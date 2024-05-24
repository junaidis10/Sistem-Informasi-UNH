import streamlit as st
from streamlit_option_menu import option_menu


from  apps import home, data_stats, master,transaksi,stok,xSetting # import your app modules here

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Junaidi Surya,M.Kom',
                options=['Home','Account','Master','Ritail','Stok','Setting'],
                icons=['house-fill','person-circle','database-fill','cart-fill','database-dash','gear'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={ "container": {"padding": "5!important","background-color":'#858282'},
                         "icon": {"color": "white", "font-size": "23px"}, 
                         "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                         "nav-link-selected": {"background-color": "#858282"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            data_stats.app()    
        if app == "Master":
            master.app()        
        if app == 'Ritail':
            transaksi.app()
        if app == 'Stok':
            stok.app()  
        if app == 'Setting':
            xSetting.app()    
             
          
             
    run()            
         