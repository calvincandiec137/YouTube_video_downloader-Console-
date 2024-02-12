from pytube import YouTube

link=input("Enter the link: ")

yt=YouTube(link)

#Title of video
print("Title: ",yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of video: ",yt.length,"seconds")
#Rating
print("Ratings: ",yt.rating)
#res1=input("Enter the resolution: ")
#-------------------------------Menu-------------------------
def menu():
    while True:
        print("\nSelect the resolution:")
        print("1.360p")
        print("2.720p")
        print("3.1080p")
        print("4.mp4")
        print("5.Exit")

        choice = input("Enter your choice: ")
        print("Loading....")

        if choice == '1':
            res1="360p"
        elif choice == '2':
           res1="720p"
        elif choice == '3':
            res1="1080p"
        elif choice == '4':
             res1="mp4"
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
        
        return res1
#--------------------filtering the resolution to the input--------------------

stream=yt.streams
filtered_stream=stream.filter(res=menu())

if filtered_stream:
    ys=filtered_stream.first()
    ys.download()
   
    print("The downloaded media is in the same folder this programme is saved in....")
else:
    print('Try again')