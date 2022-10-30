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

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2020'
        )
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

m.to_streamlit(height=700)
