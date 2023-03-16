# Distribuicao-Equipes

### **Necessidades**

Para rodar a ferramenta em sua máquina, é necessário possuir os seguintes requisitos:

- Vscode ou uma IDE com capacidade de versionamento;
- Python instalado na máquina;
- Necessário instalar as importações que irá solicitar na primeira execução;
- Ter acesso ao sistema SIOR.

### **Funcionalidade**

Distribuir processos para as equipes de cadastro da Serget.

### **Validações**

A ferramenta analisa:

- Se a quantidade na planilha é a mesma que consta no Sistema SIOR;
- Se o valor constante no SIOR é acima do piso de ajuizamento 800,00 $
- Se a quantidade de processos da equipe é menor ou maior a quantidade **_Solicitada pelo Supervisor_**, 
caso seja menor, a ferramenta irá distribuir mais processos, caso seja maior a ferramenta pula para a 
próxima equipe.

###  Quantidade que deve ser distribuída por equipe diáriamente
Primeira posição = **_Solicitado pelo supervisor_**

Segunda posição = **_Limite do Robô_**

```
Equipe Cobrança 1 (Adina Ferreira Silva) - 130 - 150
Equipe Cobrança 2 (Adriele Cerilo Mendes Monte) - 156 - 167
Equipe Cobrança 3 (Anna Gontijo) - 180 - 180
Equipe Cobrança 4 (Edney Bandeira Carvalho) - 156 - 167
Equipe Cobrança 5 (Nathalia Ferreira Massad) - 156 - 167
Equipe Cobrança 6 (Jéssica Vieira Lopes) - 156 - 167
Equipe Cobrança 7 (Gabriel Kalil Moraes) - 156 - 167
Equipe Cobrança 8 (Thiago Gamboa Vilar Martins) - 115 - 150
```

#### **IMPORTANTE**!
Após a execução, o operador deverá: 
- Apagar da listagem os Devedores já distribuídos;
- Alimentar a planilha de controle;
- Informar as equipes que a distribuição foi realizada;
