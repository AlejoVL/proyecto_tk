import tkinter as tk
from paquetes.gui_interface import Frame

def main():
    root = tk.Tk()
    root.title('Proyecto Tk')
    root.resizable(False,False)
    root.iconbitmap('.//img//icono2.ico')
    root.attributes('-alpha', 0.9)
    app = Frame(root = root)
    root.mainloop()

if __name__ == "__main__":
    main()