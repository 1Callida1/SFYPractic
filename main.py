import cv2
from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from tkinter import filedialog as fd


def load_image():
    global image
    image = None
    file = fd.askopenfilename(
        title="Выберите изображение",
        filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png")),
    )
    if file is not None:
        try:
            image = Image.open(file)
            img = ImageTk.PhotoImage(image)
            label.config(image=img)
            label.image = img
        except Exception as e:
            print("Ошибка при открытии файла:", e)


def take_snapshot():
    global image
    image = None
    video_capture = cv2.VideoCapture(0)
    success, image = video_capture.read()
    if success:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image)
        label.config(image=imgtk)
        label.image = imgtk
    else:
        print("Не удалось подключиться к веб-камере")


def clear_channel():
    label.image = image


def show_channel(channel):
    if channel == "R":
        red_channel = image.split()[0]
        red = ImageTk.PhotoImage(red_channel)
        label.config(image=red)
        label.image = red
    elif channel == "G":
        green_channel = image.split()[1]
        green = ImageTk.PhotoImage(green_channel)
        label.config(image=green)
        label.image = green
    elif channel == "B":
        blue_channel = image.split()[2]
        blue = ImageTk.PhotoImage(blue_channel)
        label.config(image=blue)
        label.image = blue
    else:
        print("Некорректный выбор канала")


def rotate_image(angle):
    try:
        rotated_image = image.rotate(int(angle))
        rotated_image = ImageTk.PhotoImage(rotated_image)
        label.config(image=rotated_image)
        label.image = rotated_image
    except Exception as e:
        print("Ошибка при вращении:", e)


def draw(x_first, x_second, y_first, y_second):
    try:
        temp_image = image
        draw = ImageDraw.Draw(temp_image)
        draw.rectangle(
            (int(x_first), int(x_second), int(y_first), int(y_second)), "blue", "blue"
        )
        temp_image = ImageTk.PhotoImage(temp_image)
        label.config(image=temp_image)
        label.image = temp_image
    except Exception as e:
        print("Ошибка при рисовании:", e)


def image_to_gray():
    try:
        temp_image = image
        temp_image = temp_image.convert("L")
        temp_image = ImageTk.PhotoImage(temp_image)
        label.config(image=temp_image)
        label.image = temp_image
    except Exception as e:
        print("Ошибка при рисовании:", e)


root = Tk()
root.title("Обработка изображений")

label = Label(root)
angle = StringVar()
x_first = StringVar()
x_second = StringVar()
y_first = StringVar()
y_second = StringVar()
channel = StringVar()

button1 = Button(root, text="Загрузить изображение", command=load_image)
button2 = Button(root, text="Сделать снимок с веб-камеры", command=take_snapshot)
button3 = Button(
    root, text="Показать канал", command=lambda: show_channel(channel.get())
)
button4 = Button(
    root, text="Повернуть изображение", command=lambda: rotate_image(angle.get())
)
button5 = Button(
    root,
    text="Нарисовать прямоугольник",
    command=lambda: draw(x_first.get(), x_second.get(), y_first.get(), y_second.get()),
)
button6 = Button(
    root,
    text="В градации серого",
    command=image_to_gray
)
angel_label = Label(root, text="Угол")
rotate_textbox = Entry(root, textvariable=angle)
x_first_textbox = Entry(root, textvariable=x_first)
x_second_textbox = Entry(root, textvariable=x_second)
y_first_textbox = Entry(root, textvariable=y_first)
y_second_textbox = Entry(root, textvariable=y_second)
x_first_label = Label(root, text="X1")
x_second_label = Label(root, text="X2")
y_first_label = Label(root, text="Y1")
y_second_label = Label(root, text="Y2")
channel_dropdown = OptionMenu(root, channel, "R", "G", "B")

label.grid(row=0, column=1)
button1.grid(row=1, column=1)
button2.grid(row=2, column=1)
button3.grid(row=3, column=2)
button4.grid(row=4, column=2)
button5.grid(row=5, column=2)
button6.grid(row=10, column=2)
rotate_textbox.grid(row=4, column=1)
channel_dropdown.grid(row=3, column=1)
x_first_textbox.grid(row=6, column=1)
x_second_textbox.grid(row=7, column=1)
y_first_textbox.grid(row=8, column=1)
y_second_textbox.grid(row=9, column=1)
x_first_label.grid(row=6, column=0)
x_second_label.grid(row=7, column=0)
y_first_label.grid(row=8, column=0)
y_second_label.grid(row=9, column=0)
angel_label.grid(row=4, column=0)

root.mainloop()