import streamlit as st
import random

st.title("🎲 Sorteio de Grupos")

st.write("Digite os nomes dos 24 alunos (um por linha):")

# Entrada de nomes
nomes_input = st.text_area("Lista de alunos")

if st.button("Sortear grupos"):
    alunos = nomes_input.split("\n")
    
    # Remover linhas vazias
    alunos = [a.strip() for a in alunos if a.strip() != ""]
    
    if len(alunos) != 24:
        st.error("Você precisa inserir exatamente 24 alunos!")
    else:
        random.shuffle(alunos)
        
        grupos = [alunos[i:i+4] for i in range(0, len(alunos), 4)]
        
        st.success("Grupos sorteados!")
        
        for i, grupo in enumerate(grupos, start=1):
            st.subheader(f"Grupo {i}")
            for aluno in grupo:
                st.write(f"- {aluno}")