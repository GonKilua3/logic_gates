from tkinter import *
window = Tk()
window.title("Logic Gates")
window.config(bg="Yellow")
canvas = Canvas(width=1800, height=960)
canvas.place(x=0, y=0)
text = canvas.create_text(680, 100, text="LOGIC GATES", fill="#FFF380", font="Skia, 35")
canvas.create_rectangle(canvas.bbox(text), fill="Black")
text = canvas.create_text(680, 100, text="LOGIC GATES", fill="#FFF380", font="Skia, 35")
canvas.create_line(350, 300, 550, 300, fill="Black", width=5)
canvas.create_line(547, 300, 547, 380, fill="Black", width=5)
canvas.create_line(545, 380, 870, 380, fill="Black", width=5)
line1 = canvas.create_line(350, 460, 550, 460, fill="Black", width=5, tags="secondline")
line2 = canvas.create_line(547, 383, 547, 460, fill="Black", width=5, tags="secondline")
result = Label(window, text="1", font="Skia, 24", bg="#C4C4C4", fg="Black")
result.place(x=870, y=360)
input1 = Button(window, text="0", font="Skia, 24", bg="#C4C4C4", fg="Black", activebackground="#C4C4C4", activeforeground="Black", command=lambda: changeInput(1))
input2 = Button(window, text="0", font="Skia, 24", bg="#C4C4C4", fg="Black", activebackground="#C4C4C4", activeforeground="Black", command=lambda: changeInput(2))
input1.place(x=350, y=270)
def changeGate():
    gates = ("BUFFER", "NOT", "OR", "NOR", "AND", "NAND", "XOR", "XNOR")
    if gate.cget("text") == "XNOR":
        gate.config(text="BUFFER")
    else:
        gate.config(text="{}".format(gates[gates.index(gate.cget("text")) + 1]))
gate = Button(window, text="BUFFER", font="Skia, 24", bg="#C4C4C4", fg="Black", activebackground="#C4C4C4", activeforeground="Black", command=changeGate)
gate.place(x=620, y=350)
def changeInput(Type):
    if Type == 1:
        input1.config(text="{}".format(str((int(input1.cget("text")) + 1) % 2)))
    if Type == 2:
        input2.config(text="{}".format(str((int(input2.cget("text")) + 1) % 2)))
def NOT(num):
    if num == 0:
        return 1
    return 0
def OR(num1, num2):
    nums = (num1, num2)
    if 1 in nums:
        return 1
    return 0
def AND(num1, num2):
    if num1 == 1 and num2 == 1:
        return 1
    return 0
def XOR(num1, num2):
    if AND(NOT(num1), num2) or AND(num1, NOT(num2)):
        return 1
    return 0
def updateLogic():
    global line1, line2, input2
    if gate.cget("text") == "NOT" or gate.cget("text") == "BUFFER":
        if canvas.find_withtag("secondline"):
            canvas.itemconfig(line1, fill="#F0F0F0")
            canvas.itemconfig(line2, fill="#F0F0F0")
        if input2.winfo_exists():
            input2.destroy()
        if gate.cget("text") == "NOT":
            result.config(text="{}".format(str(NOT(int(input1.cget("text"))))))
        else:
            result.config(text="{}".format(input1.cget("text")))
    else:
        if not input2.winfo_exists():
            input2 = Button(window, text="0", font="Skia, 24", bg="#C4C4C4", fg="Black", activebackground="#C4C4C4", activeforeground="Black", command=lambda: changeInput(2))
            input2.place(x=350, y=430)
        canvas.itemconfig(line1, fill="Black")
        canvas.itemconfig(line2, fill="Black")
    if gate.cget("text") == "OR":
        result.config(text="{}".format(str(OR(int(input1.cget("text")), int(input2.cget("text"))))))
    elif gate.cget("text") == "NOR":
        result.config(text="{}".format(str(NOT(OR(int(input1.cget("text")), int(input2.cget("text")))))))
    elif gate.cget("text") == "AND":
        result.config(text="{}".format(str(AND(int(input1.cget("text")), int(input2.cget("text"))))))
    elif gate.cget("text") == "NAND":
        result.config(text="{}".format(str(NOT(AND(int(input1.cget("text")), int(input2.cget("text")))))))
    elif gate.cget("text") == "XOR":
        result.config(text="{}".format(str(XOR(int(input1.cget("text")), int(input2.cget("text"))))))
    elif gate.cget("text") == "XNOR":
        result.config(text="{}".format(str(NOT(XOR(int(input1.cget("text")), int(input2.cget("text")))))))
    window.after(1, updateLogic)
updateLogic()
window.mainloop()