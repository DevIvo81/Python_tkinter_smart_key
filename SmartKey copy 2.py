import tkinter as tk

#region SUČELJE 

root=tk.Tk()
root.title = ('IZ_Py - SmartKey')

LARGE_FONT = ('Calibri', 20)

#endregion

#region FUNKCIJE
entered_text = ''
def zvoni():
    znak = ''
    lbl_btn_panel_var.set('RiiinG!!! Netko dolazi otvoriti...')

def otvori():
    lbl_btn_panel_var.set('Unesite pin za otključavanje')

#endregion


#region BUTTON PANEL

frm_btn_panel = tk.LabelFrame(root, text='PANEL S GUMBIMA')
frm_btn_panel.columnconfigure((0, 1, 2), weight=1, minsize=100)
frm_btn_panel.grid(row=0, column=0)

lbl_btn_panel_var = tk.StringVar()
lbl_btn_panel_var.set('Vaš izbor?')
lbl_btn_panel = tk.Label(frm_btn_panel, textvariable=lbl_btn_panel_var, font=LARGE_FONT, relief='sunken')
lbl_btn_panel.grid(row=0, column=0, columnspan=3,
                        padx=5, pady=5, ipadx=5, ipady=5, sticky='nsew')

btn_pozvoni = tk.Button(frm_btn_panel, text='Pozvoni', 
                        font=LARGE_FONT, bg='light blue', bd=1, command=zvoni)
btn_pozvoni.grid(row=1, column=0, padx=10, pady=10)

btn_otkljucaj = tk.Button(frm_btn_panel, text='SPACE',
                        font=LARGE_FONT, bg='systembuttonface', bd=0, command=otvori)
btn_otkljucaj.grid(row=1, column=1, padx=10, pady=10)

btn_otkljucaj = tk.Button(frm_btn_panel, text='Otključaj',
                        font=LARGE_FONT, bg='orange', bd=1, command=otvori)
btn_otkljucaj.grid(row=1, column=2, padx=10, pady=10)



frm_pin_panel = tk.LabelFrame(root, text='PIN PANEL')
frm_pin_panel.grid(row=1, column=0)

lbl_pin_panel_var= tk.StringVar()
lbl_pin_panel_var.set('PIN PANEL')
lbl_pin_panel = tk.Label(frm_pin_panel, textvariable=lbl_pin_panel_var, font=LARGE_FONT, relief='sunken')
lbl_pin_panel.grid(row=0, column=0, columnspan=3,
                        padx=5, pady=5, ipadx=5, ipady=5, sticky='nsew')








frm_keymanager_panel = tk.LabelFrame(root, text='PANEL ZA UPRAVLJANJE KLJUČEVIMA')
frm_keymanager_panel.grid(row=2, column=0)





root.mainloop()





