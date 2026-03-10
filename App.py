import tkinter as tk

root = tk.Tk()
root.title('Tip Calculator')
root.geometry('400x350') # Increased height slightly to accommodate labels

#Bill Amount & Entry
bill_label = tk.Label(root, text='Bill Amount:', font=('Arial', 12))
bill_label.pack(pady=5)
bill_entry = tk.Entry(root, width= 30, font=('Arial', 12))
bill_entry.pack(pady=5)

#Tip Percentage & Entry
tip_label = tk.Label(root, text='Tip Percentage:', font=('Arial', 12))
tip_label.pack(pady=5)
tip_entry = tk.Entry(root, width= 30, font=('Arial', 12))
tip_entry.pack(pady=5)

#Result Label
result_label= tk.Label(root, text='', font=('Arial', 12), fg='blue')
result_label.pack(pady=10)

#Error Message Label
error_message = tk.Label(root, text='', font=('Arial', 12), fg='red')
error_message.pack(pady=5)

#Calculate Tip Function/Button
def calculate_tip():
    try:
        bill = float(bill_entry.get())
        tip_percent = float(tip_entry.get())
        tip_amount = bill * (tip_percent / 100)
        total= bill + tip_amount
        result_label.config(text=f'Tip Amount: ${tip_amount:.2f}\nTotal with tip: ${total:.2f}')
        error_message.config(text='') # Clear error if calculation succeeds
    except ValueError:
        result_label.config(text='')  # Clear result if there's an error
        error_message.config(text='ERROR: You must enter a valid number!')

btn=tk.Button(root, text='Calculate Tip', command=calculate_tip, font=('Arial', 12), bg='#2E86AB', fg='white')
btn.pack(pady=10)

# Clear Entry Function/Button
def clear_entry():
    # Fixed: pointing to the correct Entry widgets
    bill_entry.delete(0, tk.END)
    tip_entry.delete(0, tk.END)
    result_label.config(text='')
    error_message.config(text='')
    
btn_clear=tk.Button(root, text='Clear Entry', command=clear_entry, font=('Arial', 12), bg="#D39AE8", fg='white')
btn_clear.pack(pady=10)

root.mainloop()
