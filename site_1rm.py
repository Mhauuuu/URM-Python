import streamlit as st

def calcular_1rm(peso, repeticoes):
    calculo = peso * (1 + repeticoes/30)
    return round(calculo, 2)


st.title("Calculadora de 1RM Pro 💪")
st.write("Descubra sua força máxima e gere sua tabela de treinos.")


exercicio = st.text_input("Qual o exercício? (Ex: Supino, Agachamento)")


peso_usuario = st.number_input("Digite o peso levantado (kg):", min_value=0.0, step=1.0)
reps_usuario = st.number_input("Digite o número de repetições:", min_value=1, step=1)


if st.button("Calcular meu 1RM"):
    
    if exercicio != "": 

        resultado_estimado = calcular_1rm(peso_usuario, reps_usuario)
        
        st.success(f"No exercício {exercicio}, o seu 1RM estimado é de {resultado_estimado} kg")
        
        st.write("---") 
        st.subheader("📋 Sua Tabela de Cargas Recomendadas")
        
        aquecimento = round(resultado_estimado * 0.50, 2)
        hipertrofia = round(resultado_estimado * 0.75, 2)
        forca = round(resultado_estimado * 0.90, 2)
        
        st.write(f"🟢 **Aquecimento (50%):** {aquecimento} kg")
        st.write(f"🟡 **Hipertrofia (75-80%):** {hipertrofia} kg")
        st.write(f"🔴 **Força Pura (90-95%):** {forca} kg")
        
    else:
        st.warning("Por favor, digite o nome do exercício primeiro!")



