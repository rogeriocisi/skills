---
name: revisor-caperlex
description: Use esta skill mensalmente, até o 3º dia útil, para revisar as pastas "Fiscal" e "Contábil" da entidade religiosa (TCM) antes de enviar ao escritório de contabilidade Caperlex. A skill verifica se os documentos obrigatórios estão presentes e se há arquivos indevidos ou comprometedores nas pastas.
---

# Revisor de Balancetes e Documentação - Caperlex (TCM)

O objetivo desta skill é garantir que os pacotes de documentos mensais da entidade religiosa TCM estejam corretos, completos e, principalmente, seguros antes de serem enviados definitivamente ao escritório de contabilidade Caperlex.

## Regras de Negócio e Checklist de Envio para a Caperlex

**Prazo de Envio:** O envio deve ocorrer até o 3º dia útil do mês subsequente.

**A. Documentos para o Departamento Fiscal (Geralmente na Pasta `Fiscal/`):**
A documentação enviada deve conter apenas informações comerciais e tributárias da Igreja/Associação (PJ):
- Notas fiscais de compra (aquisição de materiais, equipamentos, produtos em geral).
- Notas fiscais de venda (se houver comercialização de livros, apostilas, etc.).
- Notas fiscais de serviços (tomados de terceiros, como manutenção, advogados ou prestados).
- Comprovantes de recolhimento de impostos (Guias de IRRF, DARF, INSS, ISS, certidões).

**B. Documentos para o Departamento Contábil (Geralmente na Pasta `Contabil/`):**
A documentação enviada deve conter apenas as despesas ordinárias e financeiras da PJ:
- Comprovantes de pagamento de despesas regulares com as concessionárias (água, luz, telefone, internet).
- Recibos de pagamento de aluguel e encargos.
- Extratos bancários mensais (completos) da conta Pessoa Jurídica (PJ) correspondentes ao mês em apuração.
- Contratos de seguros ou de empréstimos (sempre que houver celebração, renovação ou liquidação de contratos no mês).

## Instruções de Execução

Ao ser acionado para revisar os balancetes enviados para a Caperlex, execute os seguintes passos:

1. **Listagem dos Arquivos:** Liste recursivamente todos os arquivos e pastas dos caminhos fornecidos pelo usuário correspondentes aos fechamentos das pastas Fiscal e Contábil.
2. **Avaliação de Completude (Checklist):** Verifique, apenas observando a listagem de arquivos (nomes e tipos de arquivos), se as 4 categorias fiscais e as 4 contábeis citadas acima parecem estar com cobertura mínima. Se não houver nenhum arquivo indicando "extrato", alerte para a falta do mesmo.
3. **Auditoria Cautelosa (Documentos Indevidos e Comprometedores):**
   - Busque indícios de arquivos que **não pertencem à contabilidade estatutária da PJ** ou que possam ser comprometedores/desnecessários para a Caperlex ter acesso.
   - **Exemplos do que buscar e reprovar (Não Enviar):**
     - Pagamentos e notas fiscais em nome de PF (Pessoa Física), como contas pessoais de membros, pastores, ou funcionários.
     - Documentos de RH ou pastorais, como "planilha_salarial_pastores_visão_geral.xlsx" ou avaliações de comportamento.
     - Rascunhos, planilhas administrativas, ou registros de pregações.
     - Comprovantes de jantar ou lazer excessivo como "nota_fiscal_outback_aniversario.pdf" quando não houver relação direta com as despesas estatutárias, a não ser que especificamente marcados como válidos.
     - Arquivos com fotos, prints de conversas privadas, e rascunhos de caixa 2 (ex: "controle_ofertas_em_dinheiro_nao_declarado.xlsx").
4. **Resumo e Relatorio Final:** Forneca ao usuario um *Feedback do Balancete* em Markdown plano (evite emojis ou caracteres especiais complexos):
   - **Status Geral:** As pastas parecem refletir os requisitos? Qual a contagem total de arquivos.
   - **Arquivos Faltantes:** Ha clara ausencia de extratos ou comprovantes de despesas basicas?
   - **[ALERTA] ALERTAS CRITICOS (Acao Requerida):** Destaque todos os arquivos suspeitos que devem ser removidos e isolados. Use o marcador "[ALERTA]" em vez de emojis.
   - **Conclusao:** "Pronto para enviar" ou "Requer limpeza dos arquivos pontuados".

**Dica de Postura:** Seja muito diligente na privacidade da igreja TCM. Evite acentuacao excessiva ou caracteres especiais nos marcadores. Na duvida, pergunte: "e necessario encaminhar este arquivo para a Caperlex?".
