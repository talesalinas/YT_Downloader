from pytube import YouTube

link = input("Video's URL: ")
print("Downloading...")

YouTube(link).streams.first().download()
yt = YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
print("Video downloaded succefully")