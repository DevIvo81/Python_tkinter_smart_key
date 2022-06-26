import tkinter as tk

LARGE_FONT = ('Book Antiqua', 20)

class RootWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('IZ_Py - SmartKey')
        
        #region MAIN FRAME - inherits self 
        
        self.frm_main = tk.LabelFrame(self, text='MAIN FRAME', highlightbackground='orange',
                                        highlightthickness=3, labelanchor='n')
        self.frm_main.grid(row=0, column=0, padx=20, pady=10)
        
        # LABELA za orjentaciju unutar self.frm_main
        self.lbl_frm_main = tk.Label(self.frm_main, text='LABELA MAIN',width=100, bg='yellow')
        self.lbl_frm_main.grid(row=0, column=0, columnspan=2)
        
        #endregion
        
        #region PANEL S GUMBIMA
        self.frm_buttons = tk.LabelFrame(self.frm_main, text='PANEL S GUMBIMA', highlightbackground='orange',
                                        highlightthickness=3, labelanchor='n')
        self.frm_buttons.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
        # LABELA za orjentaciju unutar self.frm_main
        self.lbl_frm_buttons = tk.Label(self.frm_buttons, text='LABELA GUMBI',width=100, bg='purple', fg='white')
        self.lbl_frm_buttons.grid(row=0, column=0, columnspan=2)
        
        self.btn_pozvoni = tk.Button(self.frm_buttons, text='Pozvoni', font=LARGE_FONT, bg='orange', bd=1)
        self.btn_pozvoni.grid(row=1, column=0, padx=20, pady=10)
        
        self.btn_otkljucaj = tk.Button(self.frm_buttons, text='Otključaj', font=LARGE_FONT, bg='green', bd=1)
        self.btn_otkljucaj.grid(row=1, column=1, padx=20, pady=10)
        
        #endregion
        
        #region PIN PANEL
        
        # FRAME SA DIGITS I STATUS
        
        self.frm_pin = tk.LabelFrame(self.frm_main, text='PIN PANEL', highlightbackground='orange',
                                        highlightthickness=3)
        self.frm_pin.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
        
        # LABELA za orjentaciju unutar self.frm_main
        self.lbl_frm_pin = tk.Label(self.frm_pin, text='LABELA GUMBI',width=100, bg='blue', fg='white')
        self.lbl_frm_pin.grid(row=0, column=0, columnspan=2)
        
        self.frm_digits = tk.LabelFrame(self.frm_pin, text='DIGITS PANEL', highlightbackground='orange',
                                        highlightthickness=3, labelanchor='n')
        self.frm_digits.grid(row=1, column=0, padx=20, pady=10)
        
            # FRAME BUTTONS
        self.lbl_pin_display = tk.Label(self.frm_digits, text='LABELA PIN DISPLAY', width=50, bg='red', fg='white', bd=1)
        self.lbl_pin_display.grid(row=0, column=0, padx=20, pady=10)
        
        
        # FRAME STATUS
        self.frm_status = tk.LabelFrame(self.frm_pin, text='STATUS I PORUKE', highlightbackground='orange',
                                        highlightthickness=3, labelanchor='n')
        self.frm_status.grid(row=1, column=1, columnspan=2, padx=20, pady=10)
        
        
        self.lbl_status = tk.Label(self.frm_status, text='Privremeni status', width=50, height=20, bg='white', fg='white', bd=3)
        self.lbl_status.grid(row=0, column=0, padx=20, pady=10)
        
        
    

class MainFrame(tk.LabelFrame):
    def __init__(self, container) -> None:
        super().__init__(container)
        
        
        
    








'''
#region SUČELJE 

root=tk.Tk()
root.title = ('IZ_Py - SmartKey')

LARGE_FONT = ('Calibri', 20)
#endregion

#region FUNKCIJE

def zvoni():
    print('ZVONIIIII...!!!!')

def otvori():
    print('OTVARAAAA...!!!!')

#endregion


# GLAVNI FRAME

frm_main = tk.LabelFrame(root, text='GLAVNI PANEL')
# frm_main.grid(row=0, column=0, padx=10, pady=20)
frm_main.pack(padx=10, pady=20, fill='both', expand=True)


#region BUTTON PANEL

frm_btn_panel = tk.LabelFrame(frm_main, text='PANEL S GUMBIMA')
frm_btn_panel.pack(padx=10, pady=20, fill='both', expand=True)

lbl_btn_panel_var = tk.StringVar()
lbl_btn_panel = tk.Label(frm_btn_panel, textvariable=lbl_btn_panel_var)

btn_pozvoni = tk.Button(frm_btn_panel, text='Pozvoni',
                        font=LARGE_FONT, bg='orange', bd=1, command=zvoni)
btn_pozvoni.grid(side='left', padx=10, pady=20, fill='both', expand=True)

btn_otkljucaj = tk.Button(frm_btn_panel, text='Otključaj',
                        font=LARGE_FONT, bg='orange', bd=1, command=otvori)
btn_otkljucaj.pack(side='left', padx=30, pady=20, fill='both', expand=True)



frm_pin_panel = tk.LabelFrame(frm_main, text='PIN PANEL')
frm_pin_panel.pack(padx=10, pady=20, fill='both', expand=True)






frm_keymanager_panel = tk.LabelFrame(frm_main, text='PANEL ZA UPRAVLJANJE KLJUČEVIMA')
frm_keymanager_panel.pack(padx=10, pady=20, fill='both', expand=True)
'''

if __name__ == '__main__':
    root = RootWindow()
    root.mainloop()





