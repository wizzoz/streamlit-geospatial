import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info(
    """
    Aplikasi ini merupakan bagian dari Hibah Penelitian Dasar Fakultas Ilmu Sosial Universitas Negeri Jakarta dengan nomor 386/UN39/HK.02/2022 
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Dibuat oleh [Fauzi R A'rachman](https://www.linkedin.com/in/fauzi-ramadhoan/)

    Credit:
    [Qiusheng Wu](https://www.linkedin.com/in/qiushengwu)
    """
)

# Customize page title
st.title("Aplikasi Penginderaan Jauh Berbasis Cloud Computing")

st.markdown(
    """
    Pengolahan data Citra Satelit yang biasanya membutuhkan teknik, peralatan, dan keahlian khusus, kini semakin mudah untuk dipelajari oleh semua kalangan dengan memanfaatkan aplikasi berbasis website.
    """
)

#st.header("Fitur")

#markdown = """
#1. Timelapse Citra Satelit
#2. Pemetaan Tutupan Lahan
#"""

#st.markdown(markdown)

#m = leafmap.Map(minimap_control=True)
#m.add_basemap("OpenTopoMap")
#m.to_streamlit(height=500)

st.subheader("Timelapse dari Citra Satelit")
st.markdown(
    """
    Animasi berikut dibuat menggunakan fitur Timelapse. Klik `Timelapse` pada menu sidebar di sebelah kiri untuk membuat timelapse citra satelit dari area mana saja diseluruh dunia.
"""
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

with row1_col2:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")