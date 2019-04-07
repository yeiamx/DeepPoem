import tkinter as tk

HEIGHT = 500
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='img/poem.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

label = tk.Label(root, bd=0, width=48, bg='#ffddcc', fg='#cc4400', text='test', relief='groove')
label.config(font=("Courier", 44))
label.place(relx=0.5, rely=0.15, anchor='n')

root.mainloop()