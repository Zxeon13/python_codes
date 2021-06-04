import pytube
def main():
        
    url = input("Enter the video's link: ")
    vidoe = pytube.YouTube(url)
    type = input("Wanna download vidoe(v) or audio(a): ").lower()

    if type == "v" :
        type="True"
    elif type=="a":
        type="160kbps"
    else:
        input("wrong input!!")
        exit()
    print('Downloding...')

    for stream in vidoe.streams:
        if  type in str(stream):
            stream.download()
            break

    input('Done!')

while True:
    main()