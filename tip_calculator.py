import tkinter as tk

# Set up main window
root = tk.Tk()
root.title('Tip Calculator')
root.geometry('400x350')

# Bill and Tip inputs
tk.Label(root, text='Bill Amount:', font=('Arial', 12)).pack(pady=5)
bill_input = tk.Entry(root) 
bill_input.pack()

tk.Label(root, text='Tip Percent:', font=('Arial', 12)).pack(pady=5)
tip_input = tk.Entry(root)
tip_input.pack()

# Results, tip calculation
result_lbl = tk.Label(root, text='', fg='blue', font=('Arial', 12))
result_lbl.pack(pady=15)

def tip_calculation():
    try:
        # Get data and calculate
        bill_amount = float(bill_input.get())
        tip_percent = float(tip_input.get())
        
        tip_amount = bill_amount * (tip_percent / 100)
        total_amount = bill_amount + tip_amount
        
        # Display
        result_lbl.config(text=f'Tip amount: ${tip_amount:.2f}\nTotal with tip: ${total_amount:.2f}', font=('Arial', 12))
    except:
        result_lbl.config(text='INVALID INPUT, PLEASE TRY AGAIN', fg='red', font=('Arial', 12))
        

# Calculate and Clear buttons
btn = tk.Button(root, text='Calculate',font=('Arial', 12), command=tip_calculation)
btn.pack(pady=10)

def clear():
    bill_input.delete(0, tk.END)
    tip_input.delete(0, tk.END)
    result_lbl.config(text='', font=('Arial', 12))

btn_clr = tk.Button(root, text='Clear', font=('Arial', 12), command=clear)
btn_clr.pack()

root.mainloop()
