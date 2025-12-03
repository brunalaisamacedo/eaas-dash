import streamlit as st
import pandas as pd

st.set_page_config(page_title="EaaS Dashboard", layout="wide", page_icon="📊")

st.title("📊 Economics as a Service (EaaS) Dashboard")
st.markdown("**Mercado de Consultoria Econômica - Florianópolis | SC | Brasil**")

# Abas principais
tab1, tab2, tab3, tab4 = st.tabs(["📈 Resumo Executivo", "🏙️ Florianópolis", "🌎 Santa Catarina", "🇧🇷 Brasil"])

with tab1:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Empresas Alvo", "47.080", "+12%")
    col2.metric("Mercado Potencial", "R$ 1,9B", "+8%")
    col3.metric("Ticket Médio", "R$ 2.900", "-3%")
    col4.metric("Penetração", "4%", "↑ 2pp")
    
    st.markdown("---")
    
    resumo = pd.DataFrame({
        'Região': ['Florianópolis', 'Santa Catarina', 'Brasil'],
        'Empresas': [280, 1.800, 45.000],
        'Mercado (R$)': ['R$ 50,4M', 'R$ 432M', 'R$ 1,44B'],
        'Ticket Médio': ['R$ 2.840', 'R$ 2.900', 'R$ 3.135'],
        'Penetração': ['18%', '10%', '4%']
    })
    st.dataframe(resumo, use_container_width=True)

with tab2:
    st.header("🏙️ Mercado de Florianópolis")
    fl_empresas = pd.DataFrame({
        'Empresa': ['Ás Consultoria', 'MS Tecnologia', 'Parcon Consultoria', 'Regência Contabilidade'],
        'Serviço Principal': ['Análise Econômica', 'BPO Financeiro', 'Planejamento PME', 'Gestão Fiscal'],
        'Faixa de Preço': ['R$ 3.500-5.500', 'R$ 2.000-3.500', 'R$ 2.500-4.000', 'R$ 2.500-4.500'],
        'Clientes Aprox.': ['25-35', '60-80', '40-55', '70-100']
    })
    st.dataframe(fl_empresas, use_container_width=True)

with tab3:
    st.header("🌎 Mercado de Santa Catarina")
    st.write("**Principais cidades:** Florianópolis, Blumenau, Joinville, Chapecó")
    st.metric("Total de Empresas", "1.800")
    st.metric("Mercado Total", "R$ 432 Milhões")

with tab4:
    st.header("🇧🇷 Mercado Nacional")
    st.write("**Brasil - Potencial de crescimento 250%**")
    st.metric("Total de Empresas", "45.000")
    st.metric("Mercado Total", "R$ 1,44 Bilhões")

st.markdown("---")
st.markdown("**Dashboard atualizado em:** Dec 02, 2025 | **Fonte:** Análise EaaS Bruna")
