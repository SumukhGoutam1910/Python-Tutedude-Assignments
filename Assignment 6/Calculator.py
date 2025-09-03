import tkinter as tk
from tkinter import ttk

def on_click(event):
	text = event.widget.cget("text")
	if text == "=":
		try:
			result = str(eval(entry.get()))
			entry.delete(0, tk.END)
			entry.insert(tk.END, result)
		except Exception:
			entry.delete(0, tk.END)
			entry.insert(tk.END, "Error")
	elif text == "C":
		entry.delete(0, tk.END)
	else:
		entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("350x450")
root.configure(bg="#222831")

style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Segoe UI', 16), padding=10)

frame = tk.Frame(root, bg="#222831")
frame.pack(expand=True, fill="both")

entry = tk.Entry(frame, font=("Segoe UI", 24), borderwidth=0, relief=tk.FLAT, justify="right", bg="#393E46", fg="#FFD369")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=30, sticky="we")

buttons = [
	['7', '8', '9', '/'],
	['4', '5', '6', '*'],
	['1', '2', '3', '-'],
	['0', '.', 'C', '+'],
	['(', ')', '=', '']
]

for i, row in enumerate(buttons):
	for j, btn_text in enumerate(row):
		if btn_text:
			btn = tk.Button(frame, text=btn_text, font=("Segoe UI", 18), width=4, height=2, bg="#393E46", fg="#FFD369", activebackground="#FFD369", activeforeground="#222831", borderwidth=0)
			btn.grid(row=i+1, column=j, padx=8, pady=8)
			btn.bind("<Button-1>", on_click)

root.mainloop()
