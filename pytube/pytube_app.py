import pytube

url = input("Enter the video's link: ")
vidoe = pytube.YouTube(url)

print('Downloding...')

for stream in vidoe.streams:
    if 'True' in str(stream):
        stream.download()

print('Done!')
