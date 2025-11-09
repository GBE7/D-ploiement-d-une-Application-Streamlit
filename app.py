<<<<<<< HEAD
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Visualisation des données avec Streamlit')
uploaded_file = st.file_uploader("Choisissez un fichier csv", type="csv")

if uploaded_file is not None :
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des fichiers")
    st.write(df.head())


    x_col = st.selectbox("Choisissez la colonne pour l'axe X", df.columns)
    y_col = st.selectbox("Choisissez la colonne pour l'axe Y", df.columns)

    st.write(f"Gaphique de {x_col} vs {y_col}")
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x=x_col, y=y_col)
    st.pyplot(plt)
=======
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Visualisation des données avec Streamlit')
uploaded_file = st.file_uploader("Choisissez un fichier csv", type="csv")

if uploaded_file is not None :
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des fichiers")
    st.write(df.head())


    x_col = st.selectbox("Choisissez la colonne pour l'axe X", df.columns)
    y_col = st.selectbox("Choisissez la colonne pour l'axe Y", df.columns)

    st.write(f"Gaphique de {x_col} vs {y_col}")
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x=x_col, y=y_col)
    st.pyplot(plt)
>>>>>>> 9ac566eb9bba3a2aab10c7ef9489302aa2220a75
