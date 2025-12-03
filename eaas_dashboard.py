import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="EaaS Dashboard", 
    layout="wide", 
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Tema
st.markdown("""
<style>
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.title("📊 Economics as a Service (EaaS) Dashboard")
st.markdown("**Mercado de Consultoria Econômica - Análise de Oportunidade**")
st.markdown("**Regiões:** Florianópolis | Santa Catarina | Brasil | **Data:** 02/12/2025")

# ============================================================================
# DADOS CONSOLIDADOS
# ============================================================================

# Dimensionamento de Mercado
mercado_data = {
    'Região': ['Florianópolis', 'Santa Catarina', 'Brasil'],
    'Empresas Alvo': [280, 1800, 45000],
    'Mercado (R$ mi)': [50.4, 432, 1440],
    'Ticket Médio (R$)': [2840, 2900, 3135],
    'Taxa Penetração': [18, 10, 4],
    'Crescimento Anual': [12, 9, 6]
}

# Concorrentes por região
concorrentes_fl = {
    'Empresa': ['Ás Consultoria', 'MS Tecnologia', 'Parcon Consultoria', 'Novo Design', 'Neo Pessoas', 'Agência G13'],
    'Serviço Principal': ['Análise econômica', 'BPO Financeiro', 'Planejamento PME', 'Design/Consultoria', 'Gestão de Pessoas', 'Design/Marketing'],
    'Faixa de Preço (R$)': ['3.500-5.500', '2.000-3.500', '2.500-4.000', '2.500-4.500', '3.000-5.000', '2.000-4.000'],
    'Clientes Aprox.': ['25-35', '60-80', '40-55', '20-30', '35-45', '50-70']
}

# Segmentação Florianópolis
segmentacao_fl = {
    'Segmento': [
        'Startups Growth',
        'PMEs Pequenas',
        'PMEs Micro'
    ],
    'Qtd. Estimada': [60, 110, 110],
    'Ticket Médio (R$)': [5000, 3000, 1500],
    'Receita Mensal (R$)': [300000, 330000, 165000],
    'Inv. Anual EaaS': [60000, 36000, 18000]
}

# Indicadores de Performance
kpi_data = {
    'Indicador': ['HHI Index', 'Taxa Adoção Tech', 'Elasticidade-Preço', 'Barreira Entrada', 'Score Oportunidade'],
    'Florianópolis': [6800, 48, -0.72, 3.8, 78],
    'Santa Catarina': [5200, 42, -0.65, 3.2, 68],
    'Brasil': [2900, 62, -0.58, 2.3, 55]
}

# SWOT Florianópolis
swot_fl = {
    'Forças': [
        'Ecossistema startups em crescimento',
        'Expertise em análise econômico-financeira',
        'Custos operacionais baixos',
        'Relacionamentos com founders',
        'Serviço diferenciado'
    ],
    'Fraquezas': [
        'Mercado limitado (280 alvo)',
        'Capacidade pagamento limitada',
        'Dificuldade reter especialistas',
        'Falta de volume para escala',
        'Dependência de parcerias'
    ],
    'Oportunidades': [
        'Expansão regional (Blumenau, Brusque)',
        'Alta demanda crescimento',
        'Mentorias e aceleradoras',
        'Modelo online escalável',
        'Especialização em inovação'
    ],
    'Ameaças': [
        'Plataformas SaaS desintermediando',
        'Entrada consultorias nacionais',
        'Recessão econômica',
        'Automatização por IA',
        'Regulação de consultores'
    ]
}

# ============================================================================
# ABAS PRINCIPAIS
# ============================================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Resumo Executivo", 
    "🏙️ Florianópolis", 
    "🌎 Santa Catarina", 
    "🇧🇷 Brasil",
    "📋 Análise Consolidada"
])

# ============================================================================
# TAB 1: RESUMO EXECUTIVO
# ============================================================================
with tab1:
    st.header("📈 Resumo Executivo - Dimensionamento de Mercado")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Empresas Alvo Total", "47.080", "+12% YoY")
    col2.metric("Mercado Potencial", "R$ 1,9B", "+8% YoY")
    col3.metric("Ticket Médio", "R$ 2.900", "-3% vs FL")
    col4.metric("Penetração Média", "10,7%", "Baixa concentração")
    
    st.markdown("---")
    
    # Tabela comparativa
    st.subheader("Comparativo Regional")
    df_mercado = pd.DataFrame(mercado_data)
    st.dataframe(df_mercado, use_container_width=True)
    
    # Gráficos lado a lado
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Mercado Potencial (R$ mi)")
        fig_mercado = go.Figure(data=[
            go.Bar(x=df_mercado['Região'], y=df_mercado['Mercado (R$ mi)'], marker_color='indianred')
        ])
        fig_mercado.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig_mercado, use_container_width=True)
    
    with col2:
        st.subheader("Universo de Empresas")
        fig_empresas = go.Figure(data=[
            go.Bar(x=df_mercado['Região'], y=df_mercado['Empresas Alvo'], marker_color='lightsalmon')
        ])
        fig_empresas.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig_empresas, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Taxa de Penetração (%)")
        fig_penetracao = go.Figure(data=[
            go.Bar(x=df_mercado['Região'], y=df_mercado['Taxa Penetração'], marker_color='lightseagreen')
        ])
        fig_penetracao.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig_penetracao, use_container_width=True)
    
    with col2:
        st.subheader("Ticket Médio (R$)")
        fig_ticket = go.Figure(data=[
            go.Bar(x=df_mercado['Região'], y=df_mercado['Ticket Médio (R$)'], marker_color='khaki')
        ])
        fig_ticket.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig_ticket, use_container_width=True)

# ============================================================================
# TAB 2: FLORIANÓPOLIS
# ============================================================================
with tab2:
    st.header("🏙️ Florianópolis - Análise de Mercado EaaS")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Empresas Alvo", "280", "18% penetração")
    col2.metric("Mercado Potencial", "R$ 50,4M", "Anual")
    col3.metric("Ticket Médio", "R$ 2.840", "-0.72 elasticidade")
    col4.metric("Oportunidade", "78/100", "MUITO ATRATIVO")
    
    st.markdown("---")
    
    # Concorrentes
    st.subheader("🏢 Análise Competitiva - Principais Concorrentes")
    df_concorrentes = pd.DataFrame(concorrentes_fl)
    st.dataframe(df_concorrentes, use_container_width=True)
    
    st.markdown("---")
    
    # Segmentação
    st.subheader("📊 Segmentação de Clientes - Startups e PMEs")
    df_segmentacao_fl = pd.DataFrame(segmentacao_fl)
    st.dataframe(df_segmentacao_fl, use_container_width=True)
    
    st.write("**Debug:** Quantidade de registros:", len(df_segmentacao_fl))
    st.write("**Valores para gráficos:**")
    st.write(f"- Segmentos: {df_segmentacao_fl['Segmento'].tolist()}")
    st.write(f"- Quantidades: {df_segmentacao_fl['Qtd. Estimada'].tolist()}")
    
    # Gráficos de Florianópolis - CORRIGIDO
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Distribuição de Clientes por Segmento")
        fig_dist_fl = px.pie(
            df_segmentacao_fl,
            labels='Segmento',
            values='Qtd. Estimada',
            color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1'],
            title="Clientes por Segmento"
        )
        fig_dist_fl.update_layout(height=400)
        st.plotly_chart(fig_dist_fl, use_container_width=True)
    
    with col2:
        st.subheader("Ticket Médio por Segmento (R$)")
        fig_ticket_fl = px.bar(
            df_segmentacao_fl,
            x='Segmento',
            y='Ticket Médio (R$)',
            color_discrete_sequence=['#FF6B6B'],
            title="Ticket Médio"
        )
        fig_ticket_fl.update_layout(height=400, xaxis_tickangle=-45)
        st.plotly_chart(fig_ticket_fl, use_container_width=True)
    
    # Gráficos adicionais
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Receita Mensal Potencial por Segmento (R$)")
        fig_receita_fl = px.bar(
            df_segmentacao_fl,
            x='Segmento',
            y='Receita Mensal (R$)',
            color_discrete_sequence=['#4ECDC4'],
            title="Receita Mensal"
        )
        fig_receita_fl.update_layout(height=400, xaxis_tickangle=-45)
        st.plotly_chart(fig_receita_fl, use_container_width=True)
    
    with col2:
        st.subheader("Investimento Anual em EaaS (R$)")
        fig_inv_fl = px.bar(
            df_segmentacao_fl,
            x='Segmento',
            y='Inv. Anual EaaS',
            color_discrete_sequence=['#45B7D1'],
            title="Investimento Anual"
        )
        fig_inv_fl.update_layout(height=400, xaxis_tickangle=-45)
        st.plotly_chart(fig_inv_fl, use_container_width=True)
    
    st.markdown("---")
    
    # SWOT Analysis
    st.subheader("🎯 Análise SWOT - Florianópolis")
    
    swot_col1, swot_col2 = st.columns(2)
    
    with swot_col1:
        st.success("**Forças**")
        for i, forca in enumerate(swot_fl['Forças'], 1):
            st.write(f"{i}. {forca}")
        
        st.error("**Fraquezas**")
        for i, fraqueza in enumerate(swot_fl['Fraquezas'], 1):
            st.write(f"{i}. {fraqueza}")
    
    with swot_col2:
        st.info("**Oportunidades**")
        for i, oportunidade in enumerate(swot_fl['Oportunidades'], 1):
            st.write(f"{i}. {oportunidade}")
        
        st.warning("**Ameaças**")
        for i, ameaca in enumerate(swot_fl['Ameaças'], 1):
            st.write(f"{i}. {ameaca}")
    
    st.markdown("---")
    
    # KPIs
    st.subheader("📈 Indicadores-Chave de Performance (KPIs)")
    
    kpi_col1, kpi_col2 = st.columns(2)
    
    with kpi_col1:
        st.metric("Índice HHI (Concentração)", "6.800", "Altamente concentrado")
        st.metric("Taxa Adoção Tecnologia", "48%", "Oportunidade digital")
        st.metric("Elasticidade-Preço", "-0,72", "Moderadamente elástica")
    
    with kpi_col2:
        st.metric("Barreira de Entrada", "3,8/5", "Moderada-Alta")
        st.metric("Score Oportunidade", "78/100", "MUITO ATRATIVO ✓")

# ============================================================================
# TAB 3: SANTA CATARINA
# ============================================================================
with tab3:
    st.header("🌎 Santa Catarina - Análise Regional")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Empresas Alvo", "1.800", "6,4x Florianópolis")
    col2.metric("Mercado Potencial", "R$ 432M", "Anual")
    col3.metric("Ticket Médio", "R$ 2.900", "Tickets maiores")
    col4.metric("Oportunidade", "68/100", "ATRATIVO")
    
    st.markdown("---")
    
    st.subheader("📍 Principais Cidades Econômicas")
    cidades_sc = {
        'Cidade': ['Florianópolis', 'Blumenau', 'Joinville', 'Chapecó', 'Criciúma', 'Brusque'],
        'Especialização': [
            'Startups/Tech',
            'Têxtil/Turismo',
            'Planejamento Urbano',
            'Agro/Indústria',
            'Cerâmica/Porcelana',
            'Têxtil/Varejo'
        ],
        'Ticket Médio': ['R$ 2.840', 'R$ 3.200', 'R$ 3.500', 'R$ 2.500', 'R$ 3.800', 'R$ 3.100']
    }
    df_cidades = pd.DataFrame(cidades_sc)
    st.dataframe(df_cidades, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("🏢 Concorrentes Regionais Principais")
    concorrentes_sc = {
        'Empresa': ['Parcon', 'Ás Consultoria', 'Regência', 'Alore', 'EconômiX', 'Análise Setorial SC'],
        'Região Base': ['Florianópolis', 'Florianópolis', 'Várias', 'Criciúma', 'Blumenau', 'Brusque'],
        'Estratégia': ['Local/Acessível', 'Especializada', 'Volume', 'Setorial', 'EaaS Esp.', 'Cluster'],
        'Preço Base (R$/mês)': ['2.500-4.500', '3.500-6.000', '2.500-5.000', '4.000-6.500', '3.000-5.500', '2.800-5.000']
    }
    df_conc_sc = pd.DataFrame(concorrentes_sc)
    st.dataframe(df_conc_sc, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("📊 Segmentação de Clientes - SC")
    segmentacao_sc = {
        'Segmento': ['Startups Growth', 'PMEs Médias', 'PMEs Pequenas'],
        'Qtd. Estimada': [360, 720, 720],
        'Ticket Médio (R$)': [4500, 3200, 1800],
        'Receita Mensal': [1620000, 2304000, 1296000]
    }
    df_seg_sc = pd.DataFrame(segmentacao_sc)
    st.dataframe(df_seg_sc, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_seg_sc_pie = px.pie(df_seg_sc, labels='Segmento', values='Qtd. Estimada',
                               color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        st.plotly_chart(fig_seg_sc_pie, use_container_width=True)
    
    with col2:
        st.subheader("Receita Potencial por Segmento")
        fig_receita_sc = px.bar(df_seg_sc, x='Segmento', y='Receita Mensal',
                               color_discrete_sequence=['#4ECDC4'])
        st.plotly_chart(fig_receita_sc, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("📈 KPIs Santa Catarina")
    kpi_col1, kpi_col2 = st.columns(2)
    
    with kpi_col1:
        st.metric("HHI (Concentração)", "5.200", "Moderadamente concentrado")
        st.metric("Taxa Adoção Tech", "42%", "Crescente")
    
    with kpi_col2:
        st.metric("Barreira Entrada", "3,2/5", "Moderada")
        st.metric("Score Oportunidade", "68/100", "ATRATIVO")

# ============================================================================
# TAB 4: BRASIL
# ============================================================================
with tab4:
    st.header("🇧🇷 Brasil - Mercado Nacional")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Empresas Alvo", "45.000", "160x Florianópolis")
    col2.metric("Mercado Potencial", "R$ 1,44B", "Anual")
    col3.metric("Ticket Médio", "R$ 3.135", "Maior valor agregado")
    col4.metric("Oportunidade", "55/100", "MODERADA")
    
    st.markdown("---")
    
    st.subheader("🏢 Concorrentes Nacionais - Top Players")
    
    concorrentes_br = {
        'Empresa/Plataforma': [
            'Hubbli Finance', 'Caju Finance', 'Contabl', 'Omni Finance',
            'XP Investimentos', 'Deloitte', 'PwC', 'Eureca Consultoria'
        ],
        'Especialidade': [
            'PME Digital', 'Fluxo Caixa SaaS', 'Gestão Completa',
            'AI Analysis', 'Corporate', 'Enterprise', 'Enterprise', 'Startups'
        ],
        'Abrangência': [
            'Online Brasil', 'Online Brasil', 'Online Brasil',
            'Online Brasil', 'Nacional', 'Nacional', 'Nacional', 'Online Brasil'
        ],
        'Ticket Médio (R$/mês)': [
            '1.500-4.000', '2.000-4.500', '1.800-4.000', '2.500-5.000',
            '10.000-50.000', '15.000-60.000', '12.000-40.000', '2.000-5.000'
        ]
    }
    df_conc_br = pd.DataFrame(concorrentes_br)
    st.dataframe(df_conc_br, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("📊 Segmentação de Clientes - Brasil")
    
    segmentacao_br = {
        'Segmento': [
            'Startups Growth',
            'Startups Scale',
            'PMEs Médias',
            'PMEs Pequenas'
        ],
        'Qtd. Estimada': [9000, 2250, 18000, 15750],
        'Ticket Médio (R$)': [4500, 6500, 3200, 1800],
        'Receita Mensal (R$)': [40500000, 14625000, 57600000, 28350000]
    }
    df_seg_br = pd.DataFrame(segmentacao_br)
    st.dataframe(df_seg_br, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Distribuição de Clientes")
        fig_seg_br_pie = px.pie(df_seg_br, labels='Segmento', values='Qtd. Estimada',
                               color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1', '#F7DC6F'])
        st.plotly_chart(fig_seg_br_pie, use_container_width=True)
    
    with col2:
        st.subheader("Potencial de Receita Mensal")
        fig_receita_br = px.bar(df_seg_br, x='Segmento', y='Receita Mensal (R$)',
                               color_discrete_sequence=['#4ECDC4'])
        st.plotly_chart(fig_receita_br, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("📈 KPIs Brasil")
    kpi_col1, kpi_col2 = st.columns(2)
    
    with kpi_col1:
        st.metric("HHI (Concentração)", "2.900", "Fragmentado - múltiplos nichos")
        st.metric("Taxa Adoção Tech EaaS", "62%", "Oportunidade crescente")
        st.metric("Elasticidade-Preço", "-0,58", "Preço é fator decisão")
    
    with kpi_col2:
        st.metric("Barreira Entrada", "2,3/5", "Baixa a Moderada")
        st.metric("Score Oportunidade", "55/100", "MODERADO - Nichos com potencial")

# ============================================================================
# TAB 5: ANÁLISE CONSOLIDADA
# ============================================================================
with tab5:
    st.header("📋 Análise Consolidada - Comparativo Regional")
    
    # Comparativo geral
    st.subheader("📊 Dimensionamento Comparativo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Empresas Alvo por Região")
        fig_empresas_comp = px.bar(df_mercado, x='Região', y='Empresas Alvo',
                                  color_discrete_sequence=['#FF6B6B'])
        st.plotly_chart(fig_empresas_comp, use_container_width=True)
    
    with col2:
        st.subheader("Mercado Potencial Comparativo")
        fig_mercado_comp = px.bar(df_mercado, x='Região', y='Mercado (R$ mi)',
                                 color_discrete_sequence=['#4ECDC4'])
        st.plotly_chart(fig_mercado_comp, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("🎯 Índices de Oportunidade (KPIs Consolidados)")
    
    df_kpi = pd.DataFrame(kpi_data)
    st.dataframe(df_kpi, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**Florianópolis**\n\n- 🎯 Score: 78/100\n- 📊 HHI: 6.800\n- 💰 Mercado: R$ 50,4M\n- 📈 Crescimento: 12% ao ano")
    
    with col2:
        st.info("**Santa Catarina**\n\n- 🎯 Score: 68/100\n- 📊 HHI: 5.200\n- 💰 Mercado: R$ 432M\n- 📈 Crescimento: 9% ao ano")
    
    with col3:
        st.info("**Brasil**\n\n- 🎯 Score: 55/100\n- 📊 HHI: 2.900\n- 💰 Mercado: R$ 1,44B\n- 📈 Crescimento: 6% ao ano")
    
    st.markdown("---")
    
    st.subheader("💡 Recomendações Estratégicas por Região")
    
    recomendacoes = {
        'Dimensão': [
            'Foco Principal',
            'Target Principal',
            'Positioning',
            'Preço Base Recomendado',
            'Horizon Inicial',
            'Escala Viável (Year 1)',
            'Receita Realista (Year 1)'
        ],
        'Florianópolis': [
            'Diferenciação Local Premium',
            'Cat A+B (270 clientes)',
            'Expert Local + Design + Marketing',
            'R$ 4.500-6.000/mês',
            '12 meses',
            '10-15 clientes',
            'R$ 60-90 mil/mês'
        ],
        'Santa Catarina': [
            'Integração Regional',
            'Cat A (640 clientes)',
            'Solução Integrada Multi-Regional',
            'R$ 3.500-5.500/mês',
            '18 meses',
            '15-25 clientes',
            'R$ 75-150 mil/mês'
        ],
        'Brasil': [
            'Especialização Nacional',
            'Cat B+C (42.5k clientes)',
            'Nicho Especializado',
            'R$ 2.000-8.000/mês',
            '24-36 meses',
            '5-10 clientes',
            'R$ 50-100 mil/mês'
        ]
    }
    
    df_recomendacoes = pd.DataFrame(recomendacoes)
    st.dataframe(df_recomendacoes, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("🚀 Gaps e Oportunidades Principais")
    
    gaps_oportunidades = {
        'Gap/Oportunidade': [
            'Consultoria Integrada',
            'Especialização em PME',
            'Transformação Digital',
            'Suporte Local + Online',
            'Certificações Profissionais',
            'Parcerias Estratégicas',
            'Copyright/Propriedade Intelectual'
        ],
        'Florianópolis': ['FORTE', 'FORTE', 'MODERADA', 'FORTE', 'MODERADA', 'MODERADA', 'OPORTUNIDADE'],
        'Santa Catarina': ['MODERADA', 'FORTE', 'MODERADA', 'MODERADA', 'FRACA', 'FORTE', 'OPORTUNIDADE'],
        'Brasil': ['FORTE', 'MUITO FORTE', 'FORTE', 'OPORTUNIDADE', 'FORTE', 'FORTE', 'OPORTUNIDADE'],
        'Recomendação': [
            'Diferenciar como EaaS',
            'Nicho principal',
            'Combinar com inovação',
            'Modelo híbrido',
            'Diferenciar expertise',
            'Ampliar com universidades',
            'Novo mercado emergente'
        ]
    }
    
    df_gaps = pd.DataFrame(gaps_oportunidades)
    st.dataframe(df_gaps, use_container_width=True)

# ============================================================================
# RODAPÉ
# ============================================================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    <p><b>Dashboard atualizado em:</b> 02/12/2025</p>
    <p><b>Fonte:</b> Análise EaaS - Mercado de Consultoria Econômica</p>
    <p><b>Regiões Cobertas:</b> Florianópolis (SC) | Santa Catarina | Brasil</p>
</div>
""", unsafe_allow_html=True)
