import streamlit as st
import re
import pandas as pd 
import numpy as np

st.title("""
Masukkan data 
Migrain :
""")

#Fractional Knapsack Problem
#Getting input from user
Umur = int(st.number_input("Masukan Umur: ",0))
Durasi = int(st.number_input("Durasi : ",0))
Frekuensi = int(st.number_input("Frekuensi : ",0))
Lokasi = int(st.number_input("Lokasi : ",0))
Karakter = int(st.number_input("Karakter : ",0))
Intensitas = int(st.number_input("Intensitas : ",0))
Mual = int(st.number_input("Mual : ",0))
Muntah = int(st.number_input("Muntah : ",0))
Fanofobia = int(st.number_input("Fanofobia : ",0))
Photophobia = int(st.number_input("Ketakutan dipotret : ",0))

submit = st.button("submit")


if submit:
    st.info("Jadi,dinyakataan . ")


