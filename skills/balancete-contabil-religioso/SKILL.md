---
name: balancete-contabil-religioso
description: Gera balancetes mensais para organizações religiosas sem funcionários. Consolida entradas (mensalidades, vendas de artigos, doações) e saídas (reembolsos, manutenção, limpeza, aluguel, utilidades) a partir de extratos bancários e conversas de WhatsApp. Use sempre que o usuário solicitar prestação de contas, fechamento de mês ou balancete contábil.
---

# Balancete Contábil Religioso

Esta skill automatiza a prestação de contas mensal para organizações religiosas. Ela transforma conversas de WhatsApp e extratos PDFs em um relatório financeiro profissional, com organização digital rigorosa.

## Fluxo de Trabalho

### 1. Identificação do Período
- Determine o mês alvo. Filtre datas no WhatsApp e nos extratos para este período.

### 2. Coleta e Categorização
- **Mapeamento de Transações**: Cruze pedidos de Pix no WhatsApp com débitos no extrato.
- **Regras de Negócio**:
    - **Mensalidade**: Valor fixo de R$ 120,00. Valores excedentes no mesmo comprovante devem ser lançados como `DOAÇÕES` ou `VENDAS/RIFAS`.
    - **Aluguel**: Deve somar Aluguel + IPTU + Condomínio em um único lançamento de `ALUGUEL`.

### 3. Geração do Arquivo (XLSX)
- **Regra de Sinais e Fórmulas**: Cada linha de saídas (despesas) na planilha `Balancete` deve ter valor **negativo**. Como consequência, a fórmula do "Balanço do Mês" na célula `B17` (e colunas subsequentes) deve ser o somatório `=(B7+B15)`, ou caso se mantenham os valores positivos `=(B7-B15)`. Mantenha o padrão de **valores negativos para saídas**.
- **Mestre**: Atualize o arquivo `CONTROLE MENSAL-2026.xlsx` preenchendo a coluna correspondente (B=Jan, C=Fev, etc.).
- **Mensal**: Gere `CONTROLE MENSAL-YYYY-MM.xlsx` na pasta `Contabil` do mês, contendo dados apenas até aquele mês (snapshot).

### 4. Organização Digital de Pastas
Para cada mês, crie a seguinte estrutura em `Tesouraria\Balancetes-Antigravity\YYYY-MM`:
- **`Contabil`**: Contém o `.xlsx` do mês e os extratos bancários (`PDF`).
- **`Fiscal`**: Contém APENAS comprovantes de despesas, notas fiscais e boletos.
    - **Nomenclatura Semântica**: Renomeie arquivos como `IMG-*` para nomes descritivos (ex: `NF-Velas.jpg`, `Boleto-IPTU.jpg`, `Recibo-Reforma.jpg`) baseando-se no contexto da conversa.
- **`..\Arquivos-Extras\YYYY-MM`**: Mova para cá áudios (`PTT-*`, `.opus`), vídeos, figurinhas e fotos não-fiscais (pessoais ou informativas).

### 5. Finalização
Apresente o resumo em Markdown e confirme a criação dos arquivos e a organização semântica das imagens.
