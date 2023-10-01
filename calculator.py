import tkinter as tk
from tkinter import messagebox, ttk

class ShoppingCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Calculator")

        self.order_total = 0
        self.order_items = []

        # Create and configure GUI elements
        self.label = tk.Label(root, text="Enter the item price (Rs):", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.price_entry = tk.Entry(root, font=("Helvetica", 12))
        self.price_entry.pack(pady=5)

        self.item_name_label = tk.Label(root, text="Enter the item name:", font=("Helvetica", 12))
        self.item_name_label.pack()

        self.item_name_entry = tk.Entry(root, font=("Helvetica", 12))
        self.item_name_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item, font=("Helvetica", 12))
        self.add_button.pack(pady=10)

        # Bind the Enter key to the add_item method
        self.root.bind('<Return>', lambda event=None: self.add_item())

        self.summary_label = tk.Label(root, text="Order Summary:", font=("Helvetica", 12))
        self.summary_label.pack()

        self.summary_text = tk.Text(root, height=10, width=40, font=("Helvetica", 12))
        self.summary_text.pack()

        self.total_label = tk.Label(root, text="Total Amount:", font=("Helvetica", 12))
        self.total_label.pack()

        self.total_amount_label = tk.Label(root, text="Rs0.00", font=("Helvetica", 14, "bold"))
        self.total_amount_label.pack()

        self.create_bill_button = tk.Button(root, text="Create Bill", command=self.create_bill, font=("Helvetica", 12))
        self.create_bill_button.pack(pady=10)

    def add_item(self):
        try:
            item_price = float(self.price_entry.get())
            item_name = self.item_name_entry.get()
            if item_price < 0:
                messagebox.showerror("Error", "Price cannot be negative.")
            else:
                self.order_items.append((item_name, item_price))
                self.order_total += item_price
                self.summary_text.insert(tk.END, f"{item_name}: Rs{item_price:.2f}\n")
                self.total_amount_label.conrRsfig(text=f"Total Amount: Rs{self.order_total:.2f}")
                self.price_entry.delete(0, tk.END)
                self.item_name_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def create_bill(self):
        if len(self.order_items) > 0:
            bill_filename = "order_bill.txt"
            with open(bill_filename, "w") as bill_file:
                bill_file.write("Order Summary:\n")
                for item, price in self.order_items:
                    bill_file.write(f"{item}: Rs{price:.2f}\n")
                bill_file.write(f"Total Amount: Rs{self.order_total:.2f}")
            messagebox.showinfo("Success", f"Bill saved to '{bill_filename}'")
        else:
            messagebox.showerror("Error", "No items in the order to create a bill.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCalculatorApp(root)
    root.geometry("400x600")
    root.configure(bg="#f2f2f2")
    root.mainloop()
