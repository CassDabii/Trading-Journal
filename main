from tkinter import *
from db import Database
from tkinter import messagebox
db = Database('tradelog.db')

root = Tk()
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Grid.rowconfigure(root, x, weight=1)
Grid.columnconfigure(root, x, weight=1)


# ==================================================================================================================================================================
# Methods for Applications
# ==================================================================================================================================================================

def populate_listbox():
    trade_log.delete(0, END)
    for row in db.fetch():
        trade_log.insert(END, row)


def addtrade():
    if date_entries.get() == '' or time_entries.get() == '' or instrument_entries.get() == '' or direction_entries.get() == '' or lot_entries.get() == '' or entry_price_entries.get() == '' or exit_price_entries.get() == '' or pnl_entries.get() == '' or note_entries.get() == '' or outcome_entries.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields \n(Exception Account Balance)')
        return
    db.insert(date_entries.get(), time_entries.get(), instrument_entries.get(),
              direction_entries.get(), lot_entries.get(), entry_price_entries.get(),
              exit_price_entries.get(), pnl_entries.get(), note_entries.get(),
              outcome_entries.get())
    trade_log.delete(0, END)
    trade_log.insert(END, (date_entries.get(), time_entries.get(), instrument_entries.get(),
                           direction_entries.get(), lot_entries.get(), entry_price_entries.get(),
                           exit_price_entries.get(), pnl_entries.get(), note_entries.get(),
                           outcome_entries.get()))
    cleartrade()
    populate_listbox()


def select_trade(event):
    try:
        global selected_trade
        index = trade_log.curselection()[0]
        selected_trade = trade_log.get(index)

    # To show the selected row in the respected entry boxes
        date_entries.delete(0, END)
        date_entries.insert(END, selected_trade[1])
        time_entries.delete(0, END)
        time_entries.insert(END, selected_trade[2])
        instrument_entries.delete(0, END)
        instrument_entries.insert(END, selected_trade[3])
        direction_entries.delete(0, END)
        direction_entries.insert(END, selected_trade[4])
        lot_entries.delete(0, END)
        lot_entries.insert(END, selected_trade[5])
        entry_price_entries.delete(0, END)
        entry_price_entries.insert(END, selected_trade[6])
        exit_price_entries.delete(0, END)
        exit_price_entries.insert(END, selected_trade[7])
        pnl_entries.delete(0, END)
        pnl_entries.insert(END, selected_trade[8])
        note_entries.delete(0, END)
        note_entries.insert(END, selected_trade[9])
        outcome_entries.delete(0, END)
        outcome_entries.insert(END, selected_trade[10])
    except IndexError:
        pass


def removetrade():
    db.remove(selected_trade[0])
    populate_listbox()


def cleartrade():
    date_entries.delete(0, END)
    time_entries.delete(0, END)
    instrument_entries.delete(0, END)
    direction_entries.delete(0, END)
    lot_entries.delete(0, END)
    entry_price_entries.delete(0, END)
    exit_price_entries.delete(0, END)
    pnl_entries.delete(0, END)
    note_entries.delete(0, END)
    outcome_entries.delete(0, END)


def updatetrade():
    db.update(selected_trade[0], date_entries.get(), time_entries.get(), instrument_entries.get(),
              direction_entries.get(), lot_entries.get(), entry_price_entries.get(),
              exit_price_entries.get(), pnl_entries.get(), note_entries.get(),
              outcome_entries.get())
    populate_listbox()

# ==================================================================================================================================================================
# Design of Application
# ==================================================================================================================================================================

# Creating the title of the frame


root.title('Cyxas Trading Journal')

# Changing background colour of app
root['bg'] = 'white'

# Making the starting size bigger for ease will change when more functionality is added
root.minsize(300, 300)
root.geometry('700x700')  # Dimension of the window

# Create & Configure frame
frame = Frame(root)
frame.grid(row=0, column=0, sticky=N + S + E + W)

# Adding labels of the entries
account_balance = Label(root, text='Balance', bg='white', fg='black', pady=2)
account_balance.grid(row=1, column=0, sticky=W)
date_label = Label(root, text='Date', bg='white', fg='black', pady=2)
date_label.grid(row=2, column=0, sticky=W)
time_label = Label(root, text='Time', bg='white', fg='black')
time_label.grid(row=2, column=2, sticky=W)
instrument_label = Label(root, text='Instrument', bg='white', fg='black')
instrument_label.grid(row=2, column=4, sticky=W)
direction_label = Label(root, text='Direction', bg='white', fg='black')
direction_label.grid(row=2, column=6, sticky=W)
lots_label = Label(root, text='Lots', bg='white', fg='black')
lots_label.grid(row=3, column=0, sticky=W, pady=2)
entry_price_label = Label(root, text='Entry Price', bg='white', fg='black')
entry_price_label.grid(row=3, column=2, sticky=W)
exit_price_label = Label(root, text='Exit Price', bg='white', fg='black')
exit_price_label.grid(row=3, column=4, sticky=W)
pnl_label = Label(root, text='P & L', bg='white', fg='black')
pnl_label.grid(row=3, column=6, sticky=W)
notes_label = Label(root, text='Notes', bg='white', fg='black')
notes_label.grid(row=4, column=0, sticky=W, pady=2)
outcome_label = Label(root, text='Outcome', bg='white', fg='black')
outcome_label.grid(row=4, column=4, sticky=W)

# Entry Boxes
account_balance_entries = Entry(root, width=20, borderwidth=1)
account_balance_entries.grid(row=1, column=1, columnspan=4, sticky=W)
account_balance_entries.configure({'background': 'white'})
account_balance_entries.get()

date_entries = Entry(root, width=10, borderwidth=1)
date_entries.grid(row=2, column=1, sticky=W)
date_entries.configure({'background': 'white'})
date_entries.get()

time_entries = Entry(root, width=10, borderwidth=1)
time_entries.grid(row=2, column=3, sticky=W)
time_entries.configure({'background': 'white'})
time_entries.get()

instrument_entries = Entry(root, width=10, borderwidth=1)
instrument_entries.grid(row=2, column=5, sticky=W)
instrument_entries.configure({'background': 'white'})
instrument_entries.get()

direction_entries = Entry(root, width=10, borderwidth=1)
direction_entries.grid(row=2, column=7, sticky=W)
direction_entries.configure({'background': 'white'})
direction_entries.get()

lot_entries = Entry(root, width=10, borderwidth=1)
lot_entries.grid(row=3, column=1, sticky=W)
lot_entries.configure({'background': 'white'})
lot_entries.get()

entry_price_entries = Entry(root, width=10, borderwidth=1)
entry_price_entries.grid(row=3, column=3, sticky=W)
entry_price_entries.configure({'background': 'white'})
entry_price_entries.get()

exit_price_entries = Entry(root, width=10, borderwidth=1)
exit_price_entries.grid(row=3, column=5, sticky=W)
exit_price_entries.configure({'background': 'white'})
exit_price_entries.get()

pnl_entries = Entry(root, width=10, borderwidth=1)
pnl_entries.grid(row=3, column=7, sticky=W)
pnl_entries.configure({'background': 'white'})
pnl_entries.get()

note_entries = Entry(root, width=37, borderwidth=1)
note_entries.grid(row=4, column=1, columnspan=3, sticky=W)
note_entries.configure({'background': 'white'})
note_entries.get()

outcome_entries = Entry(root, width=10, borderwidth=1)
outcome_entries.grid(row=4, column=5, sticky=W)
outcome_entries.configure({'background': 'white'})
outcome_entries.get()

# Trade List
trade_log = Listbox(root, height=27, width=115, bg='white', borderwidth=0)
trade_log.grid(row=6, column=0, columnspan=8, rowspan=10, padx=(10, 0))

# Create Scrollbar
scrollbar = Scrollbar(root)
scrollbar.grid(row=6, column=8, padx=0)
trade_log.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=trade_log.yview)

# Buttons
add_trade = Button(root, text='Add Trade', width=12, bg='white', command=addtrade)
add_trade.grid(row=5, column=1, pady=5, sticky=N + S + E + W)

remove_trade = Button(root, text='Remove Trade', width=12, bg='white', command=removetrade)
remove_trade.grid(row=5, column=3, pady=5, sticky=N + S + E + W)

update_trade = Button(root, text='Update Trade', width=12, bg='white', command=updatetrade)
update_trade.grid(row=5, column=5, pady=5, sticky=N + S + E + W)

clear_trade = Button(root, text='Clear Trade', width=12, bg='white', command=cleartrade)
clear_trade.grid(row=5, column=7, pady=5, sticky=N + S + E + W)

# bind select
trade_log.bind('<<ListboxSelect>>', select_trade)


populate_listbox()
# Start Program
root.mainloop()
