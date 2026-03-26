import os
import sys
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from moviepy.video.fx.all import resize

def criar_video(pasta_imagens, arquivo_audio, output_video="video_final.mp4", zoom_suave=True):
    """
    Combina uma pasta de imagens com um áudio do NotebookLM para criar um vídeo.
    """
    # Verificações básicas
    if not os.path.exists(arquivo_audio):
        print(f"❌ Erro: O arquivo de áudio não foi encontrado em: {arquivo_audio}")
        return

    if not os.path.exists(pasta_imagens):
        print(f"❌ Erro: A pasta de imagens não existe: {pasta_imagens}")
        return

    # 1. Carregar o áudio
    print(f"🎤 Carregando áudio: {arquivo_audio}")
    audio = AudioFileClip(arquivo_audio)
    duracao_total = audio.duration
    
    # 2. Listar e ordenar as imagens da pasta
    extensoes_validas = ('.png', '.jpg', '.jpeg', '.webp')
    imagens_arquivos = sorted([
        os.path.join(pasta_imagens, f) 
        for f in os.listdir(pasta_imagens) 
        if f.lower().endswith(extensoes_validas)
    ])
    
    if not imagens_arquivos:
        print("❌ Erro: Nenhuma imagem encontrada na pasta!")
        return

    # 3. Calcular tempo de cada imagem
    duracao_por_imagem = duracao_total / len(imagens_arquivos)
    print(f"🖼️  Encontradas {len(imagens_arquivos)} imagens. Cada uma terá {duracao_por_imagem:.2f} segundos.")

    # 4. Criar os clipes de vídeo para cada imagem
    print("🎬 Processando clipes (isso pode levar alguns minutos)...")
    clips = []
    
    for img_path in imagens_arquivos:
        clip = ImageClip(img_path).set_duration(duracao_por_imagem)
        
        # Aplica um efeito de zoom suave (Ken Burns)
        if zoom_suave:
            # O zoom aumenta de 1.0 para 1.15 durante a exibição
            clip = clip.fx(resize, lambda t: 1.0 + 0.05 * t/duracao_por_imagem)
            clip = clip.set_position(('center', 'center'))

        clips.append(clip)
    
    # 5. Concatenar imagens e adicionar o áudio
    video = concatenate_videoclips(clips, method="compose")
    video = video.set_audio(audio)
    
    # 6. Exportar o vídeo final
    print(f"🚀 Renderizando vídeo final: {output_video}")
    # Usando threads para acelerar a renderização
    video.write_videofile(
        output_video, 
        fps=24, 
        codec="libx264", 
        audio_codec="aac",
        threads=4,
        preset="medium"
    )
    
    print("\n" + "="*40)
    print(f"✅ VÍDEO CONCLUÍDO: {os.path.abspath(output_video)}")
    print("="*40)

if __name__ == "__main__":
    # Ajuste os caminhos abaixo conforme necessário
    projeto_path = r"C:\Antigravity\Youtube\Videos com Skills\Armagedom-Trump"
    
    PASTA_IMAGENS = os.path.join(projeto_path, "imagens")
    ARQUIVO_AUDIO = os.path.join(projeto_path, "audio_notebooklm.wav") # ou .mp3
    OUTPUT_NAME = os.path.join(projeto_path, "video_final_notebooklm.mp4")
    
    criar_video(PASTA_IMAGENS, ARQUIVO_AUDIO, OUTPUT_NAME)
