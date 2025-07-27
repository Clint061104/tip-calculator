"""
Tip Calculator App
Author: Lehlohonolo Clint Nkalo
Description: A simple GUI-based app to calculate tips and total amounts from a bill.
"""

import tkinter as tk
from tkinter import messagebox

class TipCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Tip Calculator")
        self.root.geometry("350x300")
        self.root.configure(bg="#f4f4f4")

        self.build_ui()

    def build_ui(self):
        # Bill amount input
        tk.Label(self.root, text="Bill Amount (R):", bg="#f4f4f4", font=('Arial', 11)).pack(pady=(10, 0))
        self.bill_entry = tk.Entry(self.root, font=('Arial', 12), justify='center')
        self.bill_entry.pack()

        # Tip percentage input
        tk.Label(self.root, text="Tip Percentage (%):", bg="#f4f4f4", font=('Arial', 11)).pack(pady=(10, 0))
        self.tip_entry = tk.Entry(self.root, font=('Arial', 12), justify='center')
        self.tip_entry.pack()

        # Calculate button
        tk.Button(self.root, text="Calculate Tip", command=self.calculate_tip, bg="#4CAF50", fg="white", font=('Arial', 11)).pack(pady=15)

        # Result label
        self.result_label = tk.Label(self.root, text="", bg="#f4f4f4", font=('Arial', 12, 'bold'))
        self.result_label.pack(pady=5)

    def calculate_tip(self):
        try:
            bill = float(self.bill_entry.get())
            tip_percent = float(self.tip_entry.get())
            tip = round(bill * (tip_percent / 100), 2)
            total = round(bill + tip, 2)

            self.result_label.config(text=f"Tip: R{tip:.2f}\nTotal: R{total:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TipCalculatorApp(root)
    root.mainloop()