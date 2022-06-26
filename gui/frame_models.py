import tkinter as tk

LARGE_FONT = ('Book Antiqua', 12)

class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(highlightbackground='orange',
                    highlightthickness=3, 
                    width=100)
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')
        

class GumbiPanel(tk.Frame):
    def __init__(self, container):
        super().__init__(container)    
        self.config(highlightbackground='orange',
                    highlightthickness=3)
        self.columnconfigure((0, 1), weight=1)
        
        self.btn_pozvoni = tk.Button(self, text='Pozvoni', font=LARGE_FONT, bg='orange', bd=1)
        self.btn_pozvoni.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')
        
        self.btn_otkljucaj = tk.Button(self, text='Otključaj', font=LARGE_FONT, bg='green', bd=1)
        self.btn_otkljucaj.grid(row=0, column=1, padx=5, pady=10, sticky='nsew')
    

#region PIN FRAME

class PinPanel(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(highlightbackground='orange',
                    highlightthickness=3)
        self.columnconfigure((0, 1), weight=1)
        
        self.frm_buttons = GumbiPanel(self)
        self.frm_buttons.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
        
        self.frm_status = StatusIPoruke(self)
        self.frm_status.grid(row=1, column=0, padx=5, pady=10, sticky='nsew')
        
        self.frm_digits = DigitsFrame(self)
        self.frm_digits.grid(row=1, column=1, padx=5, pady=10, sticky='nsew')
        
        
class DigitsFrame(tk.Frame):
    
    def __init__(self, container):
        super().__init__(container)
        self.config(highlightbackground='orange',
                    highlightthickness=3)
        self.rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)
        
        self.ent_digits_var = tk.StringVar()
        self.ent_digits = tk.Entry(self, textvariable=self.ent_digits_var, 
                                    font=('Verdana', 12), bg='#0dcaf0', justify='right')
        self.ent_digits.grid(row=0, column=0, columnspan=3, 
                            padx=5, pady=10, sticky='nsew')
        
        
        #region 1. RED BROJKI
        self.btn_7 = tk.Button(self, text='7', 
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('7'))
        self.btn_7.grid(row=1, column=0,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_8 = tk.Button(self, text='8', 
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('8'))
        self.btn_8.grid(row=1, column=1,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_9 = tk.Button(self, text='9',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('9'))
        self.btn_9.grid(row=1, column=2,
                        padx=5, pady=10, sticky='ew')
        #endregion
        
        
        #region 2. RED BROJKI        
        self.btn_4 = tk.Button(self, text='4',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('4'))
        self.btn_4.grid(row=2, column=0,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_5 = tk.Button(self, text='5',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('5'))
        self.btn_5.grid(row=2, column=1,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_6 = tk.Button(self, text='6',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('6'))
        self.btn_6.grid(row=2, column=2,
                        padx=5, pady=10, sticky='ew')
        #endregion
        
        
        #region 3. RED BROJKI
        self.btn_1 = tk.Button(self, text='1',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('1'))
        self.btn_1.grid(row=3, column=0,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_2 = tk.Button(self, text='2',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('2'))
        self.btn_2.grid(row=3, column=1,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_3 = tk.Button(self, text='3',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('3'))
        self.btn_3.grid(row=3, column=2,
                        padx=5, pady=10, sticky='ew')
        #endregion
        

        #region 4. RED BROJKI
        self.btn_clear = tk.Button(self, text='C',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=self.clear_entry)
        self.btn_clear.grid(row=4, column=0,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_0 = tk.Button(self, text='0',
                                font=('Verdana', 12),
                                bg='#0d6efd',
                                command=lambda: self.click_paste('0'))
        self.btn_0.grid(row=4, column=1,
                        padx=5, pady=10, sticky='ew')
        
        self.btn_E = tk.Button(self, text='E',
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
        pass
        
            
    #endregion

class StatusIPoruke(tk.Frame):
    def __init__(self, container) -> None:
        super().__init__(container)
        self.config(highlightbackground='orange',
                    highlightthickness=3)
        
        self.lbl_status_var = tk.StringVar()
        self.lbl_status_var.set('Privremeni status')
        self.lbl_status = tk.Label(self, textvariable=self.lbl_status_var, font=LARGE_FONT)
        self.lbl_status.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')

#endregion





#region ADMIN PANEL

class AdminPanel(tk.Frame):
        
    def __init__(self, container):
        super().__init__(container)
    
        self.config(highlightbackground='orange',
                    highlightthickness=3)
        self.columnconfigure((0, 1), weight=1)
        
        self.frm_lista_osoba = ListaOsoba(self)
        self.frm_lista_osoba.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')
        
        self.frm_novi_korisnik = NoviKorisnik(self)
        self.frm_novi_korisnik.grid(row=0, column=1, padx=5, pady=10, sticky='nsew')
        
        # FRAME LISTA OSOBA

class ListaOsoba(tk.Frame):
        
    def __init__(self, container):
        super().__init__(container)
        self.config(highlightbackground='orange',
                    highlightthickness=3)
        
        self.lbl_lista_osoba_var = tk.StringVar()
        self.lbl_lista_osoba_var.set('OKVIRNA LISTA\nOsoba_1\nOsoba_2\nOsoba_3\nOsoba_A')
        self.lbl_lista_osoba = tk.Label(self, textvariable=self.lbl_lista_osoba_var, font=LARGE_FONT)
        self.lbl_lista_osoba.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')


class NoviKorisnik(tk.Frame):
        
    def __init__(self, container):
        super().__init__(container)
        self.config(highlightbackground='orange',
                    highlightthickness=3)
        self.columnconfigure((0, 1, 2), weight=1)
        
        self.lbl_ime = tk.Label(self, text='Ime', font=LARGE_FONT, justify='right')
        self.lbl_ime.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')
        
        self.entry_ime = tk.Entry(self, text='Ime', font=LARGE_FONT, justify='center')
        self.entry_ime.grid(row=0, column=1, padx=5, pady=10, sticky='nsew')
        
        
        self.lbl_prezime = tk.Label(self, text='Prezime', font=LARGE_FONT, justify='right')
        self.lbl_prezime.grid(row=1, column=0, padx=5, pady=10, sticky='nsew')
        
        self.entry_prezime = tk.Entry(self, text='Prezime', font=LARGE_FONT, justify='center')
        self.entry_prezime.grid(row=1, column=1, padx=5, pady=10, sticky='nsew')
        
        
        self.lbl_pin = tk.Label(self, text='PIN (4 broja)', font=LARGE_FONT, justify='right')
        self.lbl_pin.grid(row=2, column=0, padx=5, pady=10, sticky='nsew')
        
        self.entry_pin = tk.Entry(self, text='PIN (4 broja)', font=LARGE_FONT, justify='center')
        self.entry_pin.grid(row=2, column=1, padx=5, pady=10, sticky='nsew')
        
        # CHECKBUTTON
        self.lbl_cb_aktivan = tk.Label(self, text='Aktivan', font=LARGE_FONT, justify='right')
        self.lbl_cb_aktivan.grid(row=3, column=0, padx=5, pady=10, sticky='nsew')
        
        self.cb_aktivan = tk.Checkbutton(self)
        self.cb_aktivan.grid(row=3, column=1, padx=5, pady=10, sticky='nsew')
        
        # BUTTONS
        
        self.btn_spremi = tk.Button(self, text='Spremi', font=LARGE_FONT, bg='light blue')
        self.btn_spremi.grid(row=4, column=0, padx=5, pady=10, sticky='nsew')
        
        self.btn_odustani = tk.Button(self, text='Odustani', font=LARGE_FONT, bg='light blue')
        self.btn_odustani.grid(row=4, column=1, padx=5, pady=10, sticky='nsew')
        
        self.btn_izbrisi = tk.Button(self, text='Izbriši', font=LARGE_FONT, bg='light blue')
        self.btn_izbrisi.grid(row=4, column=2, padx=5, pady=10, sticky='nsew')
        
        
#endregion





