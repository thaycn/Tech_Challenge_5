# 🔮 Datathon Passos Mágicos: Inteligência Artificial na Educação

**Projeto Final (Tech Challenge 5) - Pós-Graduação em Data Analytics**

Este repositório contém a solução completa para o Datathon da Associação Passos Mágicos. O objetivo do projeto é compreender a evolução educacional dos alunos ao longo de 3 anos (2022-2024) e construir uma solução baseada em dados para prever e evitar a defasagem escolar.

---

## 📌 Links Principais
* **🚀 Aplicativo Web (Streamlit):** [Cole o link do seu app aqui, ex: https://seu-app.streamlit.app]
* **📓 Notebook de Análise (Colab):** [Cole o link do seu Google Colab ou deixe o arquivo .ipynb no repositório]
* **📹 Pitch de Apresentação (Vídeo):** [Cole o link do seu vídeo no YouTube/Drive]
* **📊 Apresentação de Negócios (Slides):** [Cole o link do seu Gamma App / Canva / PDF]

---

## 🎯 O Desafio
A Associação Passos Mágicos atua na transformação social de crianças e jovens através da educação. O desafio proposto foi responder a 10 perguntas de negócio cruciais sobre a eficácia da metodologia da ONG e desenvolver um modelo preditivo para identificar alunos em risco de queda de desempenho acadêmico.

## 🛠️ A Solução Construída
O projeto foi dividido em 3 Sprints principais:

### 1. Data Analytics e Storytelling (Sprint 1)
Realizamos o cruzamento de bases históricas para identificar os gatilhos do sucesso. Principais descobertas:
* A categoria de excelência (Topázio) saltou de 15.1% em 2022 para **39.3% em 2024**.
* O "Ponto de Virada" do aluno não é impulsionado por sua autoavaliação (IAA), mas sim por seu **Engajamento (IEG)** e **Adaptação Pedagógica (IPP)**.

### 2. Machine Learning: Previsão de Risco (Sprint 2)
Treinamos um algoritmo **Random Forest** focado em comportamento preventivo:
* **Objetivo:** Prever se o aluno entrará em defasagem escolar ou terá nota acadêmica (IDA) inferior a 6.0.
* **Métrica de Sucesso:** O modelo alcançou um **Recall de 77%**, atuando como um poderoso sistema de alerta precoce antes que o aluno seja reprovado.

### 3. Deploy e Produto de Dados (Sprint 3)
Transformamos o modelo de IA em uma interface web interativa utilizando **Streamlit**. A equipe pedagógica da ONG pode simular o perfil comportamental do aluno e receber alertas preditivos (verdes ou vermelhos) em tempo real.

---

## 💻 Tecnologias Utilizadas
* **Linguagem:** Python
* **Manipulação de Dados:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (RandomForestClassifier)
* **Visualização:** Matplotlib, Seaborn
* **Deploy Web:** Streamlit, Joblib

---

## ⚙️ Como executar o projeto localmente

Caso queira rodar o aplicativo de Machine Learning na sua própria máquina:

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SeuUsuario/Tech_Challenge_5.git](https://github.com/SeuUsuario/Tech_Challenge_5.git)

2. Acesse a pasta do projeto:
cd Tech_Challenge_5/app

3. Instale as dependências:
pip install -r requirements.txt

4. Execute o Streamlit:
streamlit run app.py


Desenvolvido com dedicação por [Tainara].
