from tkinter import *
from PIL import Image
import requests
from io import BytesIO
from PIL import ImageTk


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Error: {e}')
        return None

window = Tk()
window.title('Cats')
window.geometry('500x500')

label = Label()
label.pack()

url = 'https://cataas.com/cat'

img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()




