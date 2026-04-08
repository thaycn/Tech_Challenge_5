import streamlit as st
import pandas as pd
import joblib

# Configuração inicial da página
st.set_page_config(page_title="Passos Mágicos - Alerta de Risco", page_icon="🔮", layout="centered")

# Título e Descrição
st.title("🔮 Previsão de Risco Acadêmico")
st.markdown("""
Este aplicativo utiliza **Inteligência Artificial** para prever a probabilidade de um aluno da **Associação Passos Mágicos** entrar em risco de defasagem (queda de desempenho ou atraso de fase).
Insira os dados comportamentais e pedagógicos do aluno abaixo para realizar a análise preventiva.
""")

# Carregando o modelo de Machine Learning
@st.cache_resource
def load_model():
    # O arquivo .pkl precisa estar na mesma pasta que este código
    return joblib.load('modelo_passos_magicos.pkl')

modelo = load_model()

# Interface de Entrada de Dados
st.header("📊 Dados do Aluno")
col1, col2 = st.columns(2)

with col1:
    idade = st.number_input("Idade do Aluno", min_value=7, max_value=25, value=15)
    ieg = st.slider("Engajamento (IEG)", min_value=0.0, max_value=10.0, value=8.0, step=0.1)
    iaa = st.slider("Autoavaliação (IAA)", min_value=0.0, max_value=10.0, value=8.0, step=0.1)

with col2:
    ips = st.slider("Aspecto Psicossocial (IPS)", min_value=0.0, max_value=10.0, value=8.0, step=0.1)
    ipp = st.slider("Aspecto Psicopedagógico (IPP)", min_value=0.0, max_value=10.0, value=8.0, step=0.1)

# Botão para ativar a previsão
if st.button("Analisar Risco", type="primary"):
    
    # Organizando os dados do jeito que o modelo aprendeu (Idade, IEG, IAA, IPS, IPP)
    dados_entrada = pd.DataFrame([[idade, ieg, iaa, ips, ipp]], 
                                 columns=['Idade', 'IEG', 'IAA', 'IPS', 'IPP'])
    
    # Pedindo para o robô prever
    previsao = modelo.predict(dados_entrada)[0]
    probabilidade = modelo.predict_proba(dados_entrada)[0]
    
    # Exibindo o Resultado na Tela
    st.divider()
    st.header("Resultado da Análise")
    
    if previsao == 1:
        st.error("🚨 **ALERTA: RISCO ACADÊMICO DETECTADO!**")
        st.write(f"Probabilidade de entrar em defasagem: **{probabilidade[1] * 100:.1f}%**")
        st.warning("Recomendação: Acionar a equipe pedagógica e psicológica para intervenção preventiva imediata (reforço escolar e acompanhamento próximo).")
    else:
        st.success("✅ **ALUNO FORA DE RISCO**")
        st.write(f"Probabilidade de entrar em defasagem: **{probabilidade[1] * 100:.1f}%**")
        st.info("Recomendação: O aluno apresenta um bom padrão comportamental. Continuar monitoramento padrão.")
        st.balloons() # Animação de sucesso