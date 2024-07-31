import tkinter as tk
from PIL import Image, ImageTk
window=tk.Tk()
window.geometry("700x600")
file_path="C:/Users/thars/Appdata/Local/Programs/Python/hg.jpeg"
image=Image.open(file_path)
photo=ImageTk.PhotoImage(image)

label17=tk.Label(window,image=photo)
label17.place(x=0, y=0)
label17.image=photo
label17.pack()


label8 = tk.Label(window, text="Taste of Tradition Restaurant",font="times 28 bold")
label8.place(x=350, y=20, anchor="center")

# Menu Card
label1 =tk.Label(window, text="Menu",
               font="times 28 bold")
label1.place(x=520, y=70)

label2 =tk. Label(window, text="Pepper chicken Rs 230",
               font="times 18")
label2.place(x=450, y=120)

label3 =tk. Label(window, text="Dragon prawn  Rs 290",
               font="times 18")
label3.place(x=450, y=150)

label4 = tk.Label(window, text="Fish finger   Rs 190",
               font="times 18")
label4.place(x=450, y=180)

label5 = tk.Label(window, text="Mutton chuka  Rs 350",
               font="times 18")
label5.place(x=450, y=210)

label6 = tk.Label(window, text="Crab lollipop  Rs 270",
               font="times 18")
label6.place(x=450, y=240)

label7 =tk. Label(window, text="Gulab Jamun  Rs 50",
               font="times 18")
label7.place(x=450, y=270)

####
label9=tk.Label(window,text="Select the items",
             font="times 18")
label9.place(x=115,y=70)

label10=tk.Label(window,text="Pepper chicken",
              font="times 18")
label10.place(x=20,y=120)

e1=tk.Entry(window)
e1.place(x=20,y=150)

label11=tk.Label(window,text="Dragon prawn",
              font="times 18")
label11.place(x=20,y=200)

e2=tk.Entry(window)
e2.place(x=20,y=230)

label12=tk.Label(window,text="Fish finger ",
              font="times 18")
label12.place(x=20,y=280)

e3=tk.Entry(window)
e3.place(x=20,y=310)


label13=tk.Label(window,text="Mutton chuka ",
              font="times 18")
label13.place(x=20,y=360)

e4=tk.Entry(window)
e4.place(x=20,y=390)

label14=tk.Label(window,text="Crab lollipop",
              font="times 18")
label14.place(x=250,y=120)

e5=tk.Entry(window)
e5.place(x=250,y=150)

label15=tk.Label(window,text="Gulab Jamun",
              font="times 18")
label15.place(x=250,y=200)

e6=tk.Entry(window)
e6.place(x=250,y=230)
###

def calculate():
  
   # dic for storing the food quantity and price
    dic = {'aloo_partha': [e1, 230],
           'samosa': [e2, 290],
           'pizza': [e3, 190],
           'chilli_potato': [e4, 350],
           'chowmein': [e5, 270],
           'gulab_jamun': [e6, 50]}
    total = 0
    
    for key, val in dic.items():
        if val[0].get() != "":
            total += int(val[0].get())*val[1]
    tk.label16 = tk.Label(window,
                    text="Your Total Bill is - "+str(total),
                    font="times 18")

    # position
    tk.label16.place(x=20, y=490)

    # it will update the label with a new one
    tk.label16.after(1000,tk. label16.destroy)

    # refreshing the window
    window.after(1000, calculate)


# execute calculate function after 1 second
window.after(1000, calculate)



# closing the main loop
window.mainloop()
#root.mainloop()
