import tkinter as tk

from database.Alch_repo import pin_to_compare

LARGE_FONT = ('Book Antiqua', 12)

class PinPanel(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(highlightbackground='orange',
                    highlightthickness=3)
        self.columnconfigure((0, 1), weight=1)
        
        
        self.frm_buttons = tk.Frame(self,
                            highlightbackground='orange',
                            highlightthickness=3
                            )
        self.frm_buttons.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
        self.frm_buttons.columnconfigure((0, 1), weight=1)
        
        
        self.btn_pozvoni = tk.Button(self.frm_buttons, 
                                    text='Pozvoni', 
                                    font=LARGE_FONT, 
                                    bg='orange', bd=1,
                                    command=self.click_pozvoni)
        self.btn_pozvoni.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')
        
        self.btn_otkljucaj = tk.Button(self.frm_buttons,
                                    text='Otključaj', 
                                    font=LARGE_FONT, 
                                    bg='green', bd=1,
                                    command=self.click_otkljucaj)
        self.btn_otkljucaj.grid(row=0, column=1, padx=5, pady=10, sticky='nsew')
        
        
        self.frm_pin_panel = tk.LabelFrame(self, text='PIN PANEL',
                    highlightbackground='orange',
                    highlightthickness=3
                    )
        self.frm_pin_panel.grid(row=1, column=0, padx=5, pady=10, sticky='nsew')
        self.columnconfigure((0, 1), weight=1)
        
        
        
        
        self.frm_status = tk.Frame(self.frm_pin_panel,
                    highlightbackground='orange',
                    highlightthickness=3
                    )
        self.frm_status.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')
        
        self.lbl_status_var = tk.StringVar()
        self.lbl_status_var.set('Privremeni status')
        self.lbl_status = tk.Label(self.frm_status, textvariable=self.lbl_status_var, font=LARGE_FONT)
        self.lbl_status.grid(row=0, column=0, rowspan=5, padx=5, pady=10, sticky='nsew')
        
        
        
        
        self.frm_digits = tk.Frame(self.frm_pin_panel,
                    highlightbackground='orange',
                    highlightthickness=3
                    )
        self.frm_digits.grid(row=0, column=1, padx=5, pady=10, sticky='nsew')
        self.frm_digits.rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.frm_digits.columnconfigure((0, 1, 2), weight=1)
        
        self.ent_digits_var = tk.StringVar()
        self.ent_digits = tk.Entry(self.frm_digits, textvariable=self.ent_digits_var, 
                                    font=('Verdana', 12), bg='#0dcaf0', justify='right')
        self.ent_digits.grid(row=0, column=0, columnspan=3, 
                            padx=5, pady=10, sticky='nsew')
        
        #region 1. RED BROJKI
        self.btn_7 = tk.Button(self.frm_digits, text='7', 
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('7'))
        self.btn_7.grid(row=1, column=0,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_8 = tk.Button(self.frm_digits, text='8', 
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('8'))
        self.btn_8.grid(row=1, column=1,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_9 = tk.Button(self.frm_digits, text='9',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('9'))
        self.btn_9.grid(row=1, column=2,
                        padx=5, pady=10, sticky='ew')
        #endregion
        
        
        #region 2. RED BROJKI        
        self.btn_4 = tk.Button(self.frm_digits, text='4',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('4'))
        self.btn_4.grid(row=2, column=0,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_5 = tk.Button(self.frm_digits, text='5',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('5'))
        self.btn_5.grid(row=2, column=1,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_6 = tk.Button(self.frm_digits, text='6',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('6'))
        self.btn_6.grid(row=2, column=2,
                        padx=5, pady=10, sticky='ew')
        #endregion
        
        
        #region 3. RED BROJKI
        self.btn_1 = tk.Button(self.frm_digits, text='1',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('1'))
        self.btn_1.grid(row=3, column=0,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_2 = tk.Button(self.frm_digits, text='2',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('2'))
        self.btn_2.grid(row=3, column=1,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_3 = tk.Button(self.frm_digits, text='3',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('3'))
        self.btn_3.grid(row=3, column=2,
                        padx=5, pady=10, sticky='ew')
        #endregion
        

        #region 4. RED BROJKI
        self.btn_clear = tk.Button(self.frm_digits, text='C',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=self.clear_entry)
        self.btn_clear.grid(row=4, column=0,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_0 = tk.Button(self.frm_digits, text='0',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('0'))
        self.btn_0.grid(row=4, column=1,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_E = tk.Button(self.frm_digits, text='E',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=self.click_unos)
        self.btn_E.grid(row=4, column=2,
                        padx=5, pady=10, sticky='ew')
        #endregion
    
        
    #region FUNKCIJE
        
        self.unos_pina = ''
    
    def click_paste(self, value):
        self.unos_pina += value
        self.ent_digits_var.set(self.unos_pina)
        
        
    def clear_entry(self):
        
        pass
        
        
    def click_unos(self):
        entered_pin = self.ent_digits_var.get()
        
    
    def click_pozvoni(self):
        self.lbl_status_var.set('Netko će doći otvoriti')
    
    def click_otkljucaj(self):
        self.lbl_status_var.set('Unesite pin!')
    #endregion


root = tk.Tk()

frame = PinPanel(root)
frame.grid(column=0, row=0, padx=5, pady=10, sticky='nsew')

root.mainloop()