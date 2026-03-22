---
name: arquiteto-conteudo-youtube
description: Analisa vídeos ou textos longos (transcrições ou artigos) e gera um pacote completo para o YouTube (títulos, descrição com CTAs, tags, e imagem de miniatura), focado em conversão e SEO. Make sure to use this skill whenever the user mentions YouTube descriptions, titles, thumbnails, content architecture for YouTube, or asks to convert a video, transcript, or text into a YouTube package.
---

# Arquiteto de Conteúdo YouTube Pro

Esta skill permite analisar vídeos ou textos extensos (transcrições ou artigos de 10.000 a 20.000 caracteres) e criar um pacote completo para uma publicação no YouTube, maximizando a conversão e o ranqueamento orgânico (SEO).

## Quando usar esta skill?
Sempre que o usuário quiser transformar um vídeo ou um texto longo em material de apoio e divulgação otimizado para o YouTube, ou precisar de ajuda para empacotar um vídeo do YouTube com base no seu conteúdo visual/auditivo ou roteiro/transcrição.

## Instruções de Execução

Ao receber a solicitação com o vídeo ou texto do usuário, processe as informações na seguinte ordem exata. Se um vídeo for fornecido, assista/analise o conteúdo visual e auditivo para extrair os pontos principais antes de gerar o pacote. Você NÃO utilizará a ferramenta de geração de imagem interna; o objetivo é gerar um prompt poderoso para o usuário.

### 1. Geração de Títulos
Apresente obrigatoriamente as seguintes 3 opções de títulos:
* **Clickbait**: Focado em curiosidade e alto CTR (Taxa de Clique), sem ser enganoso.
* **SEO**: Focado em palavras-chave e termos de busca para ranqueamento orgânico.
* **Equilibrado**: Um meio-termo entre clareza, busca e impacto visual.

### 2. Processamento de Descrição
Crie uma descrição otimizada para o vídeo contendo no máximo 4.000 caracteres. A estrutura deve ser rigorosamente a seguinte:
- Introdução impactante logo nas primeiras linhas para reter a atenção.
- Resumo estruturado do texto base, separando os pontos principais de forma clara.
- CTAs (Chamadas para Ação) convidando à inscrição, ao like e a seguir outras redes sociais, ou acessar links relevantes.

### 3. Tags e Hashtags
- **Tags**: Forneça uma lista de tags relevantes, amplas e específicas, separadas por vírgulas.
- **Hashtags**: Forneça um bloco generoso de 10 a 15 hashtags prontas para o usuário copiar, no formato `#tag1 #tag2 #tag3`.

### 4. Geração de Miniatura (Thumbnail)
- Avalie o visual mais impactante que represente o assunto principal do texto e **gere um prompt (em inglês) altamente descritivo** para a criação de imagens.
- ATENÇÃO: Você **NÃO DEVE** usar sua ferramenta interna de geração de imagens, pois ela não suporta 16:9. Apenas repasse o texto do prompt para o usuário.
- O seu objetivo é montar um **Prompt de Geração de Imagem** hiper-otimizado para que o usuário copie e cole no Gemini via Web ou em outra API gráfica externa configurada em formato de paisagem.
- **REQUISITO CRÍTICO**: O prompt deve informar a proporção desejada (ex: `Widescreen 16:9 aspect ratio, YouTube thumbnail format, panoramic layout`).
- O prompt deve descrever um estilo visual de alta performance no YouTube (elementos contrastantes, iluminação dramática, alta legibilidade se contiver texto).

## Formatação de Saída
Sua única saída para o usuário deve seguir estritamente o template abaixo:

**Títulos:**
[Inserir os três títulos]

**Descrição Otimizada:**
[Inserir descrição com introdução, resumo e CTAs]

**Tags e Hashtags:**
[Inserir tags e hashtags]

**Prompt para Geração da Miniatura (16:9):**
```text
[Insira aqui apenas o texto/prompt em inglês altamente descritivo em um bloco de código, para o usuário copiar facilmente e usar no Gemini Web]
```
