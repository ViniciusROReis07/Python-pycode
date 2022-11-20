from pytube import YouTube

link = "https://www.youtube.com/watch?v=FbIbq6OdU-g"
path = input("Digite o diretorio que deseja salvar o video: ")

yt = YouTube(link)

print("Titulo ",yt.title)
print("Numero de views: ", yt.views)
print("Tamanho do video: ", yt.length, "segundos")
print("Avaliacao do video: ", yt.rating)

ys = yt.streams.get_highest_resolution()

print("Baixando....")
ys.download(path)

print("Download completo!")