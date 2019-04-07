import tkinter as tk
from generate import Generator
from plan import Planner

HEIGHT = 500
WIDTH = 800
planner = Planner()
generator = Generator()

def generate_poem(hints):
    keywords = planner.plan(hints)
    print("Keywords: " + ' '.join(keywords))
    poem = generator.generate(keywords)
    print("Poem generated:")
    for index in range(4):
        print(poem[index])
        sentences[index]['text'] = poem[index]

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='img/poem.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#e6ffe6', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Create", fg='#2e2e1f', bg='#e6ffe6', command=lambda: generate_poem(entry.get()))
button.config(font=("Courier", 18, ""))
button.place(relx=0.7, relheight=1, relwidth=0.3)


rely = 0.3
sentences = []
for index in range(4):
    sentence = tk.Label(root, bd=0, bg='#ffddcc', fg='#cc4400',relief='groove')
    sentence.config(font=("SimSun", 20))
    sentence.place(relx=0.5, rely=rely+index*0.15, relwidth=0.35, anchor='n')
    sentences.append(sentence)


root.mainloop()