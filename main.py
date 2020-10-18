from pytube import *
from tkinter import  *
from tkinter.filedialog import *
from tkinter.messagebox import *


file_size=0
def startDownload():
    global file_size
    # main code
    try:
        url=url_Field.get()
        print(url)
        dBtn.config(text='Please Wait..')
        dBtn.config(state=DISABLED)
        save_location = askdirectory()
        print((save_location))
        # return if no location is given
        if save_location is None:
            return
        obj = YouTube(url)
        str = obj.streams.first()
        str.download(save_location)
        print('Video Download sucessfully..')
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)
        showinfo("Download Finsihed","Downloaded Successfully")


    except Exception as e:
        print("Error..!!")

main=Tk()
# create title
main.title("YouTube Downloader")
# adding icon
main.iconbitmap('yt.ico')
main.geometry("500x500")
# add image
file=PhotoImage(file='download.png')
headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP)
# add url_box
url_Field=Entry(main,font=("verdana",20),justify=CENTER)
url_Field.pack(side=TOP,fill=X,padx=12,pady=10)
#add Button
dBtn=Button(main,text="Start Download",font=("verdana",20),relief='ridge',command=startDownload)
dBtn.pack(side=TOP,pady=12)

main.mainloop()



