import yt_dlp

def download_video(url, output_path="downloads"):
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'format': 'best',
            'nonplaylist': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download concluido!")

    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

if __name__ == "__main__":
    video_url = input("Digite o link do vídeo: ").strip()
    download_video(video_url)
        