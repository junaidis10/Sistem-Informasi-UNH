# """Frameworks for running multiple Streamlit applications as a single app.
# """
# import streamlit as st
# from streamlit_option_menu import option_menu
# #from multipage import MultiApp

# from  apps import home, data_stats, master,transaksi,stok # import your app modules here


# # class MultiApp:
# #     def __init__(self):
# #         self.apps = []
        

# #     def add_app(self, title, func):
# #         """Adds a new application.
# #         Parameters
# #         ----------
# #         func:
# #             the python function to render this app.
# #         title:
# #             title of the app. Appears in the dropdown in the sidebar.
# #         """
# #         self.apps.append({
# #             "title": title,
# #             "function": func
# #         })

# #     def run(self):
# #         app = st.sidebar.radio(
# #             'Selction Menu',
# #             self.apps,
# #             format_func=lambda app: app['title'])

# #         app['function']()

# # Batas
# class MultiApp:

#     def __init__(self):
#         self.apps = []

#     def add_app(self, title, func):

#         self.apps.append({
#             "title": title,
#             "function": func
#         })

#     def run():
#         # app = st.sidebar(
#         with st.sidebar:        
#             app = option_menu(
#                 menu_title='Junaidis10@',
#                 options=['Home','Account','Master','Ritail','Setting'],
#                 icons=['house-fill','person-circle','database-fill','chat-fill','info-circle-fill'],
#                 menu_icon='chat-text-fill',
#                 default_index=1,
#                 styles={ "container": {"padding": "5!important","background-color":'#858282'},
#                          "icon": {"color": "white", "font-size": "23px"}, 
#                          "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
#                          "nav-link-selected": {"background-color": "#858282"},}
                
#                 )

        
#         if app == "Home":
#             home.app()
#         if app == "Account":
#             #test.app()    
#         if app == "Master":
#             master.app()        
#         if app == 'Ritail':
#             transaks.app()
#         if app == 'Setting':
#             stok.app()    
             
          
             
#     run()            
         