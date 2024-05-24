import streamlit as st
from apps.myConnection import mydb
import pandas as pd
#from app  import mydb

def app():

    mycursor=mydb.cursor()
    # # #xcursor=mydb.cursor()


    option2=st.sidebar.selectbox("Master Transaction",("Transaction","View","Update","Delete"))
    # option3=st.sidebar.selectbox("Stok Barang",("Stok","Supplier  ","View Stok","Delete"))
    # option2=st.sidebar.selectbox("Master Transaction",("Transaction","View","Update","Delete"))
    if option2=="Transaction":
        st.write("-"*70)
        st.subheader("Create a Record")
        st.write("-"*70)
        Kode_Brg=st.text_input("Kode Transaksi Barang  ")
        No_Fak=st.number_input("No Faktur ",min_value=1)
        TglTran=st.text_input("Tanggal Transaksi   ")
        Jumlah=st.text_input("Jumlah Penjualan    ")
        Harga=st.text_input("Harga Penjualan   ")
        Keterangan=st.text_input("Keterangan Barang ")
        if st.button("Save Transaction"):
            sql2= "Insert into Jual values(%s,%s,%s,%s,%s,%s)"
            val2= (Kode_Brg,No_Fak,TglTran,Jumlah,Harga,Keterangan)
            mycursor.execute(sql2,val2)
            mydb.commit()
            st.success("Record Created Successfully!!!")

    elif option2=="View":
        st.subheader("View  Records")
        mycursor.execute("select Kode_Brg,No_Fak,TglTran,Jumlah,(Harga*1.1) as Harga,Keterangan from jual ")
        result = mycursor.fetchall()
        #columns=["Kode Barang","Nama Barang","Satuan ","Stok  ","Harga","Keterangan "]
        df=pd.DataFrame(result,columns=mycursor.column_names)
        st.dataframe(df)



    elif option2=="Update":
        st.subheader("Update a Record")
        pass



    elif option2=="Delete":
        st.subheader("Delete a Record")
        mycursor.execute("select Kode_Brg,No_Fak,TglTran,Jumlah,(Harga*1.1) as Harga,Keterangan from jual ")
        result = mycursor.fetchall()
        #columns=["Kode Barang","Nama Barang","Satuan ","Stok  ","Harga","Keterangan "]
        df=pd.DataFrame(result,columns=mycursor.column_names)
        st.dataframe(df)
        xKode=st.text_input("Kode Barang Yang Akan Dihapus ? ")
        if st.button("Delete"):
            sql_Delete = """Delete from jual where Kode_Brg = %s"""
            # row to delete
            mycursor.execute(sql_Delete, (xKode,))
          
            mydb.commit()
            mycursor.execute("select Kode_Brg,No_Fak,TglTran,Jumlah,(Harga*1.1) as Harga,Keterangan from jual ")
            result = mycursor.fetchall()
            #columns=["Kode Barang","Nama Barang","Satuan ","Stok  ","Harga","Keterangan "]
            df=pd.DataFrame(result,columns=mycursor.column_names)
            st.dataframe(df)
            st.success("Record Deleted Successfully!!!")
