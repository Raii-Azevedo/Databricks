import streamlit as st
import time
from questions import questions, answers 

# Configuração inicial
st.title("DATABRICKS - TEST 🚀")
st.write("You have **90 minutes** to complete the test.")

# Tempo limite (90 minutos = 5400 segundos)
TEMPO_LIMITE = 5400 

# Inicializa variáveis na sessão
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
    st.session_state.finalizado = False  # Controle de finalização

# Garante que 'respostas' está na sessão do usuário
if "respostas" not in st.session_state:
    st.session_state.respostas = {}

# Verifica o tempo restante
tempo_restante = TEMPO_LIMITE - (time.time() - st.session_state.start_time)

# Se o tempo acabou, trava a prova
if tempo_restante <= 0:
    st.session_state.finalizado = True
    tempo_restante = 0  # Evita números negativos

# Exibir contador regressivo apenas se a prova ainda estiver ativa
if not st.session_state.finalizado:
    minutos = int(tempo_restante // 60)
    segundos = int(tempo_restante % 60)
    st.info(f"⏳ Remaining time: **{minutos} min {segundos} sec**")

# Exibir perguntas apenas se a prova ainda não foi finalizada
if not st.session_state.finalizado:
    # Exibir as perguntas com numeração
    for idx, (pergunta, opcoes) in enumerate(questions.items(), 1):
        st.markdown(f"### **Question {idx}:** {pergunta}")
        resposta = st.radio(f"Choose an option:", opcoes, key=pergunta)
        st.session_state.respostas[pergunta] = resposta  # Salva resposta na sessão

    if st.button("Finish Test"):
        st.session_state.finalizado = True
        st.rerun()  # Atualiza a página para exibir o ranking

# Exibir ranking se o tempo acabar ou o usuário finalizar
if st.session_state.finalizado:
    st.subheader("🏆 Answer Ranking")
    acertos = sum(1 for q, r in st.session_state.respostas.items() if r == answers.get(q, ""))  # Evita erro

    total_questoes = len(questions)
    porcentagem_acertos = (acertos / total_questoes) * 100

    # Calculando o tempo gasto na prova
    tempo_gasto = time.time() - st.session_state.start_time
    minutos_gastos = int(tempo_gasto // 60)
    segundos_gastos = int(tempo_gasto % 60)

    # Exibir a quantidade de acertos, a porcentagem de acertos e o desempenho
    st.write(f"**You got {acertos} out of {total_questoes} questions correct.**")
    st.write(f"**Your accuracy: {porcentagem_acertos:.2f}%**")
    st.write(f"**Time spent: {minutos_gastos} min {segundos_gastos} sec**")
    
    if porcentagem_acertos >= 80:
        # Animação de sucesso
        st.success("You have been **APPROVED**! 🎉")
        st.balloons()  # Exibe animação de balões
    else:
        # Animação de fracasso
        st.error("You **FAILED**! ❌")
        st.snow()  # Exibe animação de neve

    st.warning("Test completed! ✅")

# Atualizar a página a cada segundo **somente se a prova ainda estiver em andamento**
if not st.session_state.finalizado:
    time.sleep(1)
    st.rerun()  # Força atualização apenas quando necessário
