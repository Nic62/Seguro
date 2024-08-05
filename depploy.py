import joblib as jb
import streamlit as st
#.\ambv\Scripts\activate
# streamlit run depploy.py
#modelo=jb.load("gradient.pkl")
st.title("Seguro")
st.divider()
st.header('Digite as informações abaixo:')

info_idade = st.number_input("Digite sua idade")
st.write("Sua idade é:", info_idade)
info_sexo= st.selectbox("Escolha seu sexo",['Masculino','Feminino','Prefiro não dizer'])
st.write("Seu sexo é:", info_sexo)
info_fumante=st.radio("Você é fumante", ['Sim', 'Não'])
st.write("Você se considera fumante:", info_fumante)
info_criança= st.select_slider("Selecione o número de cartões de crédito", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10+"])
if info_criança == "10+":
    total_filho = st.number_input('Se maior que dez, quantos:', min_value=10)
else:
    total_filho = int(info_criança)
st.write("Você possui:", total_filho)
info_regiao=st.selectbox("Qual região você mora", ['southwest', 'northwest','northeast','southeast'])
st.write("Você possui:", info_regiao)
info_seg = st.number_input("Digite o valor do seu seguro saúde")
st.write("Seu seguro é:", info_seg)
st.divider()
botao=st.button("PREVER")
