import tkinter as tk
from Pillow import Image,  ImageTk
dead=False
window = tk.Tk()
window.title("Dinosaur Game")
window.geometry("900x900")
window.configure(background='white')
image1 = Image. open("dino.png")
image2 =  ImageTk. PhotoImage(image1)
image_label = ttk. Label(win , image =image2)
image_label.place(x = 50 , y = 50)

tick=0;
for(i=0;i<100){
    if(i=99){
    tick=tick+1;


    }
    if (dead=True)
}
