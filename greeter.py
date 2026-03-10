import tkinter as tk

# Title and window size
root = tk.Tk()
root.title('Name Greeter')
root.geometry('400x250')
# Name label and entry
name_label = tk.Label(root, text='Please Enter Your Name:', font=('Arial', 12))
name_label.pack(pady=5)

name_entry = tk.Entry(root, width= 30, font=('Arial', 12))
name_entry.pack(pady=5)

result_label= tk.Label(root, text='', font=('Arial', 12), fg='blue')
result_label.pack(pady=10)

# Greet Function/Button
def greet():
    name = name_entry.get()
    result_label.config(text=f'Hello, {name}! Welcome to DS3850')
btn=tk.Button(root, text='Greet Me', command=greet, font=('Arial', 12), bg="#D39AE8", fg='white')
btn.pack(pady=10)

# Clear Entry Function/Button
def clear_entry():
    name_entry.delete(0, tk.END)
    result_label.config(text='')
btn=tk.Button(root, text='Clear Entry', command=clear_entry, font=('Arial', 12), bg="#D39AE8", fg='white')
btn.pack(pady=10)

root.mainloop()
