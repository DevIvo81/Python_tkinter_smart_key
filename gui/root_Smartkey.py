from . import tk

from .frame_models import MainFrame, PinPanel, GumbiPanel, AdminPanel


class RootWindow(tk.Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.title('IZ_Py - SmartKey')
        self.geometry('575x700')
        
        # MAIN FRAME 
        self.frm_main = MainFrame(self)
        self.frm_main.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')
        
        
        # PIN PANEL
        self.frm_pin = PinPanel(self.frm_main)
        self.frm_pin.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
        
        
        # ADMIN PANEL
        self.frm_admin = AdminPanel(self.frm_main)
        self.frm_admin.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
        

