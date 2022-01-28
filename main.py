import tkinter as tk

if __name__ == "__main__":
    okno = tk.Tk()

    canvas = tk.Canvas(okno, width=600, height=300)
    canvas.grid(columnspan=3, rowspan=2)

    welcome_text = tk.Label(text="QRCode Generátor", font="Bahnschrift")
    welcome_text.grid(column=0, row=0)

    url_input = tk.Entry(okno)
    url_input.grid(column=1, row=0)


    def generate_qrcode():
        print(url_input.get())


    btn_submit = tk.Button(text="Generuj!", command=lambda: generate_qrcode())
    btn_submit.grid(column=1, row=1)

    okno.mainloop()
