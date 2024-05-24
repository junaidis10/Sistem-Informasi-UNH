import streamlit as st
from streamlit_option_menu import option_menu
from apps.myConnection import mydb
import pandas as pd
#from app  import mydb
def app():
    #st.image('gambar/master.png')
    st.title("Master Data Barang",'house-fill')
    st.divider()
    
   
    mycursor=mydb.cursor()
    
    # Display Options for CRUD Operations

    #option=st.sidebar.selectbox("Master Record",("Create","Read","Update","Delete","Search"))
    pilihan = option_menu (
            
            menu_title='Master',
            options=["Create","Search","Read","Update","Delete"],
            icons=['database-fill','search','book','database-fill','trash-fill'],
            menu_icon='house-fill',
            default_index=0,
            orientation="horizontal",
            styles={ "container": {"padding": "5!important","background-color":'#858282'},
                         "icon": {"color": "white", "font-size": "23px"}, 
                         "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                         "nav-link-selected": {"background-color": "#858282"},}
                
    )

     
    # Perform Selected CRUD Operations (Create, Read, Update and Delete)
    if pilihan == "Create":
        st.subheader("Create a Record Master")
        Kode_Brg=st.text_input("Kode Barang  ")
        Nama=st.text_input("Nama Barang ")
        Satuan=st.text_input("Satuan  ")
        Stok=st.text_input("Stok    ")
        Harga=st.text_input("Harga    ")
        Keterangan=st.text_input("Keterangan ")
        if st.button("Save Master"):
            sql= "insert into master values(%s,%s,%s,%s,%s,%s)"
            val= (Kode_Brg,Nama,Satuan,Stok,Harga,Keterangan)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully!!!")



    elif pilihan=="Read":
        mycursor=mydb.cursor()
        st.subheader("Master Records")
        
        mycursor.execute("select * from master")
        result = mycursor.fetchall()
        columns=["Kode Barang "," Nama Barang "," Satuan ","Stok  "," Harga "," Keterangan "]
        df=pd.DataFrame(result,columns=columns)
        st.dataframe(df)
        

    elif pilihan=="Update":
        st.subheader("Update a Record")
        id=st.number_input("Enter ID",min_value=1)
        Kode_Brg=st.text_input("Kode Barang  ")
        Nama=st.text_input("Nama Barang ")
        Satuan=st.text_input("Satuan  ")
        Stok=st.text_input("Stok    ")
        Harga=st.text_input("Harga    ")
        Keterangan=st.text_input("Keterangan ")
        if st.button("Update"):
            sql="update master set Nama=%s, Satuan=%s, Stok=%s, Harga=%s,Keterangan=%s where id =%s"
            val= (Kode_Brg,Nama,Satuan,Stok,Harga,Keterangan,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")


    elif pilihan=="Delete":
        st.subheader("Delete a Record")
        # Ceck Record for Delete
        mycursor.execute("select * from master")
        result = mycursor.fetchall()
        columns=["Kode Barang "," Nama Barang "," Satuan ","Stok  "," Harga "," Keterangan "]
        df=pd.DataFrame(result,columns=columns)
        st.dataframe(df)
        
        xKode=st.text_input("Kode Barang Yang Akan Dihapus ? ")
        if st.button("Delete"):
            # sql="delete from master where Kode_Brg=%s"
            # mycursor.execute(sql,xKode)
            sql_Delete_query = """Delete from Master where Kode_Brg = %s"""
            # row to delete
            mycursor.execute(sql_Delete_query, (xKode,))

            mydb.commit()
            #Refresh Tables with New Record
            st.subheader("New Record In Tables")
            mycursor.execute("select * from master")
            result = mycursor.fetchall()
            columns=["Kode Barang "," Nama Barang "," Satuan ","Stok  "," Harga "," Keterangan "]
            df=pd.DataFrame(result,columns=columns)
            st.dataframe(df)
        
            st.success("Record Deleted Successfully!!!")

        
    elif pilihan=="Search":
        search_Kode=st.text_input("Masukkan Kode Barang ? : ")
        if st.button("Cari Data"):
            
            #sql_Search_query = """Select from Master where Kode_Brg = %s"""
            sql_select_query = "select * from Master where Kode_Brg like  %s "
       
            mycursor.execute(sql_select_query, (search_Kode,))
            result = mycursor.fetchall()
            columns=["Kode Barang "," Nama Barang "," Satuan ","Stok  "," Harga "," Keterangan "]
            #df=pd.DataFrame(result,columns=columns)
            df=pd.DataFrame(result,columns=mycursor.column_names)
            st.dataframe(df)
            #mydb.commit()  
        else:
            st.success("Maaf Data Tidak Ada !!")    
        
            