import streamlit as st
import random
import time

# Configuração da página
st.set_page_config(page_title="Sorteio de Grupos", page_icon="🎲", layout="centered")

st.title("🎲 Sorteio de Grupos para Aula")
st.write("Insira os nomes dos alunos (um por linha) para sortear grupos automaticamente.")

# Entrada de dados
nomes_input = st.text_area(
    "Lista de alunos (24 nomes):",
    height=300,
    placeholder="Digite um nome por linha..."
)

# Número de alunos por grupo
tamanho_grupo = st.selectbox("Quantidade de alunos por grupo:", [2, 3, 4, 5], index=2)

# Botão de sorteio
if st.button("🎯 Sortear Grupos"):
    
    alunos = nomes_input.split("\n")
    alunos = [a.strip() for a in alunos if a.strip() != ""]
    
    total_alunos = len(alunos)

    if total_alunos == 0:
        st.warning("Digite pelo menos um nome.")
    
    elif total_alunos % tamanho_grupo != 0:
        st.error(f"O número de alunos ({total_alunos}) não é divisível por {tamanho_grupo}.")
    
    else:
        with st.spinner("Sorteando grupos... 🎲"):
            time.sleep(2)  # efeito visual
            
            random.shuffle(alunos)
            grupos = [alunos[i:i+tamanho_grupo] for i in range(0, total_alunos, tamanho_grupo)]
        
        st.success("✅ Grupos sorteados com sucesso!")
        
        # Exibir grupos
        for i, grupo in enumerate(grupos, start=1):
            st.subheader(f"Grupo {i}")
            for aluno in grupo:
                st.write(f"- {aluno}")
        
        # Preparar download
        resultado = ""
        for i, grupo in enumerate(grupos, start=1):
            resultado += f"Grupo {i}:\n"
            for aluno in grupo:
                resultado += f"- {aluno}\n"
            resultado += "\n"
        
        st.download_button(
            label="📥 Baixar grupos em TXT",
            data=resultado,
            file_name="grupos.txt",
            mime="text/plain"
        )

# Rodapé
st.markdown("---")
st.caption("Aplicação para sorteio de grupos em sala de aula usando Streamlit 🚀")