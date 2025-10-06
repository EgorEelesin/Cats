from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from PIL import ImageTk

def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Error: {e}')
        return None

window = Tk()
window.title('Cats')
window.geometry('500x500')

label = Label()
label.pack()

update_button = Button(text='Update', command=set_image)
update_button.pack()


url = 'https://cataas.com/cat'

set_image()

# img = load_image(url)
#
# if img:
#     label.config(image=img)
#     label.image = img

window.mainloop()




