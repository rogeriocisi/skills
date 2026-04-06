---
name: gestor-despesas-pessoais
description: Processa holerites, extratos bancários e faturas de cartão de crédito para gerar um resumo financeiro mensal consolidado, com categorização específica e abatimento de duplicidade. Use esta skill sempre que o usuário quiser organizar gastos mensais, analisar faturas ou gerar relatórios financeiros baseados em documentos bancários ou fiscais.
---

# Gestor de Despesas Pessoais

Esta skill é projetada para processar múltiplos documentos financeiros (holerites, extratos e faturas) e consolidá-los em um relatório mensal estruturado, garantindo que não haja contagem duplicada de gastos e que as categorias sigam regras específicas de negócio.

## Processo de Consolidação

Ao receber documentos financeiros, siga estes passos:

1. **Extração**: Extraia todos os lançamentos de débito e crédito de cada arquivo (Extratos, Cartões, Holerites).
2. **Categorização Especial**: Aplique as regras de categorização abaixo para itens específicos, independentemente da fonte.
3. **Abatimento de Duplicidade (CRÍTICO)**: 
   - Para os cartões **Porto Seguro** e **Bradesco**:
   - O valor final da linha "Cartão" no resumo deve ser: `(Valor Total da Fatura) - (Soma de todos os itens do cartão que já foram movidos para Categorias Especiais)`.
   - Isso evita que um gasto em "Educação" (pago no cartão) seja contado duas vezes (uma vez na categoria e outra no total do cartão).
4. **Extrato Bancário**: Pagamentos de cobrança (boleto) devem ser categorizados pelo nome do beneficiário (ex: "Petropolis" → Educação, "Sulamerica" → Seguros). Pagamentos de fatura de cartão ("Portoseg") devem ser IGNORADOS pois já estão na fatura.
5. **Agrupamento**: Some os valores por categoria.
6. **Relatório**: Gere um resumo consolidado por categorias.

## Regras de Categorização

### Categorias Maiores
- **Educação**:
    - "Petrópolis Serviços Financeiros" (Débitos Diretos e Boletos).
    - "Rematrícula Petrópolis", "PETROPOLIS SERVICOS", "Banana Nutrition" (Cartões e Boletos).
    - **Subcategoria Material Escolar**: "LORD PAPEL PRESENTE", "PAPELARIA PRESTES MAIA", "DISAL", "LEITURA ABC LIVRARI" (Mantenha agrupado dentro de Educação/Escola).
- **Mercados / Supermercados**: Inclui "Carrefour", "CARREFOUR", "Pão de Açúcar", "PAO DE ACUCAR", "Oxxo", "PETZ", "Daki", "WMS SUPERMERCADOS", "Conveniencias", "São Vicente", "Kitanda", etc.
- **Restaurantes**: Inclui "iFood", "IFD*", Restaurantes, Padarias, Pastelarias, Lanchonetes, "Doceira", "SodieDoces", "Chefinhos", "Mirante Restaurante", etc.
- **Viagens**: Qualquer menção a "AFPESP".
- **Cidadania Italiana**: Qualquer menção a "CIDADANIA".
- **Lazer**: Eventos, Esportes, Parques, "Hopi Hari", "Nova Cidade Parques", "Salvador Arena", "Sociedade Esportiva", etc.
- **Serviços/IA**: Invideo, Vidiq, "Claude.ai", "BrightHinki", "Google Ads", "X Corp", "OpenAI", "ChatGPT", etc.
- **Saúde/Bem-estar**: Farmácias ("Drogasil", "Drogaria São Paulo"), Clínicas, Hospitais, etc.
- **Transporte**: Uber, 99, Estacionamentos ("PL ESTACIONAMENTOS"), "CONECTCAR_FATURA", etc.
- **Combustível**: "Posto", "Auto Posto", postos de gasolina.
- **Material de Construção / Reformas**: "MADEIRAMADEIRA", "CENTER CASTILHO", "PDV*BELA TINTAS", "LEROY MERLIN", etc.
- **Casa / Contas Fixas**: "ENEL", "SABESP", "CLARO", IPTU, condomínio, "Conta Agua", "Município de São Bernardo", etc.
- **Assinaturas**: "Estadão" / "Estado S Paulo", YouTube, Google, Netflix, Amazon Prime, Kindle, "ProdutosUOL", "Amazon Kindle Unltd", etc.
- **Eletrônicos**: Lojas de eletrônicos, "MOTOROLA", "LojaMotorolaBR", "GENERA", "Americanas", "Centauro", etc.
- **Gastos Bancários/Seguros**: Seguro de Vida, Seguro de Carro, Seguro da Conta Corrente, "Sulamerica", "Bradesco Vida", "Banco C6", taxas bancárias, etc.

### Linhas Individuais (Manter Separadas)
Estas transações Pix ou débitos não devem ser agrupadas em categorias genéricas:
- "Pix (Eliangela)"
- "Pix (Erismar)"
- "Pix (Tenda Umbanda)"
- "Pix (Quitanda)"
- "Associação (AFPMSBC)" — inclui "Assoc Dos Func Public"
- "Celular (VIVO EASY)"
- "Pix (Katia)"
- "Pix (Pedro)"

### Outros (Não Categorizado)
Qualquer transação de cartão de crédito ou Pix enviado que não se enquadre nas categorias acima deve ser lançada nesta categoria **Outros**, com a descrição original do lançamento visível, para permitir categorização manual posterior.

---

## Formato de Saída — XLSX (Obrigatório)

O relatório deve **sempre** ser gerado no formato `.xlsx` (Excel), utilizando `openpyxl`, com as seguintes abas:

### Aba 1: "Visao Geral"
Tabela consolidada com todas as categorias, valores por mês e total.
Inclui: Renda, todas as categorias de despesa, Cartão Porto Seguro (Líquido), Cartão Bradesco (Total Fatura), Total Despesas e Saldo.
Formatação: cabeçalhos em azul escuro, renda em verde, saldo negativo em vermelho, valores com formato numérico `#,##0.00`.

### Aba 2: "Abatimento Porto"
Detalhamento do cálculo de abatimento do cartão Porto Seguro (Fatura Total, Itens Categorizados, Líquido).

### Abas 3+: "Detalhe [Mês]"
Uma aba por mês com o detalhamento de cada transação agrupada por categoria, incluindo Data, Descrição, Valor e Fonte.


---

## Exemplos de Processamento

**Exemplo de Abatimento:**
- Fatura Porto Seguro Total: R$ 5.000,00
- Dentro da fatura tem: iFood (R$ 100), Amazon (R$ 50), Escola (R$ 2.000).
- No relatório:
    - Educação: R$ 2.000
    - Restaurantes: R$ 100
    - Assinaturas: R$ 50
    - **Cartão Porto Seguro**: R$ 2.850 (R$ 5.000 - R$ 2.150)

**Exemplo de Pagto Cobranca no Extrato:**
- "Pagto Cobranca / Petropolis Servicos" → Categorizar como Educação
- "Pagto Cobranca / Sulamerica" → Categorizar como Gastos Bancários/Seguros
- "Pagto Cobranca / Portoseg" → IGNORAR (já contabilizado na fatura do cartão)
