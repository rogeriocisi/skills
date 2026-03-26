---
name: notebooklm-video-generator
description: Transforme áudios do NotebookLM (Audio Overviews) em vídeos completos para o YouTube. Esta skill gerencia a geração de imagens temáticas via Antigravity, a sincronização com o áudio e a renderização final do vídeo usando Python e MoviePy. Use esta skill sempre que o usuário mencionar NotebookLM, podcasts de áudio para vídeo, ou quiser transformar narrações em apresentações visuais dinâmicas.
---

# NotebookLM Video Generator

Esta skill automatiza a criação de vídeos a partir dos "Audio Overviews" do NotebookLM da Google. Ela guia o usuário na preparação dos arquivos e automatiza a geração de visuais impactantes e a renderização do vídeo.

## Quando usar esta skill?
Sempre que o usuário quiser criar um vídeo a partir de um áudio (especialmente do NotebookLM) e precisar de imagens ilustrativas e montagem automática com efeitos de zoom suave (Ken Burns).

## Fluxo de Execução Obrigatório

Siga estes passos exatamente para garantir o sucesso da criação do vídeo:

### 1. Preparação do Áudio (Usuário)
Solicite ao usuário que:
- Gere o "Audio Overview" no NotebookLM.
- Salve o arquivo como `audio_notebooklm.wav` (ou `.mp3`) na pasta raiz do projeto no Antigravity.
- Confirme o caminho completo do arquivo de áudio.

### 2. Geração de Imagens (Antigravity)
- Analise o tema do vídeo ou a transcrição fornecida.
- Gere automaticamente um conjunto de prompts de imagem (geralmente de 10 a 20 imagens para um podcast de 5 a 10 minutos).
- Use a ferramenta `generate_image` para criar as imagens na proporção 16:9.
- Salve todas as imagens em uma subpasta chamada `imagens` dentro da pasta do projeto.

### 3. Configuração do Script de Renderização
- Certifique-se de que o arquivo `gerar_video_notebooklm.py` está presente na pasta `NotebookLM` do sistema ou na pasta do projeto.
- Se o arquivo não existir, ofereça-se para criá-lo (baseado no módulo de renderização com MoviePy).

### 4. Renderização do Vídeo
- Instrua o usuário a rodar o script no terminal ou ofereça-se para rodar o comando caso tenha permissão:
  ```powershell
  python c:\Antigravity\NotebookLM\gerar_video_notebooklm.py
  ```
- O script irá calcular a duração do áudio e distribuir as imagens geradas uniformemente, aplicando o efeito de zoom suave.

## Dicas para Melhores Resultados
- **Variedade Visual**: Gere imagens que variem entre cenários amplos, retratos de personagens mencionados e infográficos conceituais para manter o dinamismo.
- **Sincronia**: Se houver uma transcrição detalhada com timestamps, ajuste o script para trocar as imagens nos momentos certos (funcionalidade avançada).
- **SEO**: Após a criação do vídeo, sugira ao usuário usar a skill `arquiteto-conteudo-youtube` para gerar a descrição e as tags do vídeo final.

---

## Formato de Saída Sugerido
Ao iniciar o processo, apresente ao usuário um plano de ação:
1. **Tema Identificado**: [Resumo do tema]
2. **Prompts de Imagem**: [Lista de 3-5 conceitos de imagem que serão gerados]
3. **Comando de Execução**: `python caminho/do/script.py`
