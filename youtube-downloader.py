from pytube import YouTube

try:
    # DEFINE PASTA Downloads COMO DESTINO
    DOWNLOAD_FOLDER = "/Users/brend/Downloads"
    video_url = input('Insira o link do vídeo: ')
    video_obj = YouTube(video_url)
    # SELECIONA A MELHOR DEFINIÇÃO DISPONÍVEL
    stream = video_obj.streams.get_highest_resolution()
    stream.download(DOWNLOAD_FOLDER)
except:
    print('ERRO: Verifique sua URL ou conexão com a internet.')
