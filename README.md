

# 🫀 CardioAI: Classificador de Insuficiência Cardíaca

Este projeto utiliza algoritmos de aprendizado de máquina para prever o risco de insuficiência cardíaca com base em atributos clínicos de pacientes. A aplicação foi desenvolvida com **Streamlit**, possibilitando uma interface interativa e acessível para usuários e profissionais da saúde.

## 📊 Modelos de Machine Learning Utilizados

Foram avaliados seis algoritmos supervisionados:

- Random Forest 🌲
- Gradient Boosting
- Support Vector Machine (SVM)
- XGBoost
- K-Nearest Neighbors (KNN)
- Regressão Logística

Após análise de desempenho (acurácia, precisão, recall, F1-score e AUC), o modelo **Random Forest** foi selecionado como o MVP (modelo de valor mínimo), por apresentar:

- Melhor equilíbrio entre precisão e recall
- Excelente F1-score e AUC
- Tempo de execução razoável
- Boa capacidade de generalização

## 📚 Sobre o Dataset

O projeto utiliza o dataset **Heart Failure Prediction**, que contém informações clínicas de pacientes e a indicação da presença ou não de doença cardíaca. A variável alvo é **HeartDisease**, sendo:

- `1`: presença de doença cardíaca
- `0`: ausência de doença cardíaca

### 📌 Variáveis (12 no total):

| Variável          | Descrição |
|-------------------|-----------|
| **Age**           | Idade do paciente (em anos) |
| **Sex**           | Sexo do paciente (`M`: Masculino, `F`: Feminino) |
| **ChestPainType** | Tipo de dor torácica: `TA`: Angina típica, `ATA`: Angina atípica, `NAP`: Dor não anginosa, `ASY`: Assintomática |
| **RestingBP**     | Pressão arterial em repouso (mm Hg) |
| **Cholesterol**   | Colesterol sérico (mg/dl) |
| **FastingBS**     | Glicemia em jejum (`1`: > 120 mg/dl, `0`: caso contrário) |
| **RestingECG**    | Eletrocardiograma em repouso: `Normal`, `ST`: alterações ST-T, `HVE`: hipertrofia ventricular esquerda |
| **MaxHR**         | Frequência cardíaca máxima alcançada |
| **ExerciseAngina**| Angina induzida por exercício (`Y`: Sim, `N`: Não) |
| **Oldpeak**       | Valor numérico da depressão ST |
| **ST_Slope**      | Inclinação do segmento ST durante exercício: `Up`, `Flat`, `Down` |
| **HeartDisease**  | Classe de saída: `1`: Doença cardíaca, `0`: Normal |

### 🔍 Exemplo de paciente com risco:

```text
Idade: 65  
Sexo: M  
Tipo de Dor no Peito: NAP  
Pressão Arterial em Repouso: 170 mmHg  
Colesterol: 300 mg/dL  
Glicemia em Jejum: 1 (Alterada)  
ECG em Repouso: ST  
Frequência Máxima: 95 bpm  
Angina de Exercício: Sim  
Oldpeak: 2.5  
Inclinação ST: Flat  
HeartDisease: 1 (com risco)
````

## 🚀 Como Executar o Projeto

### 🔧 Instalação

Clone o repositório:

```bash
git clone https://github.com/debbtrbl/cardioai.git
cd cardioai
```
Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```
### ▶️ Rodando a aplicação

Execute o aplicativo localmente com:

```bash
python -m streamlit run app.py
```

## 📌 Requisitos

* Python 3.7 ou superior



> Este projeto é de caráter educacional e demonstra como o aprendizado de máquina pode ser aplicado à área médica para apoio à decisão clínica.

