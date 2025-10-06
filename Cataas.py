from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from PIL import ImageTk

def open_new_window():
    tag = tag_entry.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')

        label = Label(new_window, image=img)
        label.pack()
        label.image = img

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

tag_entry = Entry(window)
tag_entry.pack()

load_button = Button(text='Загрузить по тегу', command=open_new_window)
load_button.pack()

# label = Label()
# label.pack()

# update_button = Button(text='Update', command=set_image)
# update_button.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
# file_menu.add_command(label='Загрузить фота', command= set_image)
file_menu.add_command(label='Загрузить фота', command= open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=window.quit)

url = 'https://cataas.com/cat'

# set_image()

# img = load_image(url)
#
# if img:
#     label.config(image=img)
#     label.image = img

window.mainloop()




