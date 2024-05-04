import tkinter as tk
from PIL import Image, ImageTk

class FoodOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Order Management")

        # Create a label to display the title
        title_label = tk.Label(root, text="Food Orders", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=7, padx=10, pady=10)

        # Create labels for each column
        columns = ["Sl No.", "Image", "Name", "Food Order", "Time of Request", "Order ID", "Status"]
        for i, col_name in enumerate(columns):
            label = tk.Label(root, text=col_name, font=("Helvetica", 12))
            label.grid(row=1, column=i, padx=10, pady=5)

        # Example data (replace this with your actual data)
        data = [
            {"name": "Rishi Kumar", "food_order": "Aloo Paratha", "time": "10:30 AM", "order_id": "1234",
             "image": "C:/Users/rishi/Downloads/imresizer-1713864073484.jpg"},
            {"name": "Rahul Choudhary", "food_order": "Bread Butter", "time": "11:15 AM", "order_id": "5678",
             "image": "C:/Users/rishi/Downloads/imresizer-1713864073484.jpg"},
            {"name": "Jay Rathor", "food_order": "Chole", "time": "12:00 PM", "order_id": "91011","image": "C:/Users/rishi/Downloads/imresizer-1713864073484.jpg"},
            {"name": "Dhruv Kumar", "food_order": "Paneer", "time": "12:30 PM", "order_id": "121314",
             "image": "C:/Users/rishi/Downloads/imresizer-1713864073484.jpg"}
        ]

        # Display the data
        for i, order in enumerate(data):
            # Determine background color based on row index
            bg_color = "white" if i % 2 == 0 else "lightgrey"

            # Create labels for each data item
            sl_no_label = tk.Label(root, text=i + 1, font=("Arial", 12), bg=bg_color)
            sl_no_label.grid(row=i + 2, column=0, padx=10, pady=5)

            # Load and display image
            image = Image.open(order["image"])



            # Resize image
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(root, image=photo, bg=bg_color)
            image_label.image = photo  # To prevent garbage collection
            image_label.grid(row=i + 2, column=1, padx=10, pady=5)

            name_label = tk.Label(root, text=order["name"], font=("Arial", 12), bg=bg_color)
            name_label.grid(row=i + 2, column=2, padx=10, pady=5)

            food_order_label = tk.Label(root, text=order["food_order"], font=("Arial", 12), bg=bg_color)
            food_order_label.grid(row=i + 2, column=3, padx=10, pady=5)

            time_label = tk.Label(root, text=order["time"], font=("Arial", 12), bg=bg_color)
            time_label.grid(row=i + 2, column=4, padx=10, pady=5)

            order_id_label = tk.Label(root, text=order["order_id"], font=("Arial", 12), bg=bg_color)
            order_id_label.grid(row=i + 2, column=5, padx=10, pady=5)

            status_label = tk.Label(root, text="Pending", font=("Arial", 12), bg=bg_color)
            status_label.grid(row=i + 2, column=6, padx=10, pady=5)

        # Add entry widget for user to input their name
        self.name_entry = tk.Entry(root, font=("Arial", 12))
        self.name_entry.grid(row=len(data) + 3, column=0, padx=10, pady=5, columnspan=2)

        name_label = tk.Label(root, text="Your Name", font=("Helvetica", 12))
        name_label.grid(row=len(data) + 2, column=0, padx=10, pady=5)

        # Button to add a new order
        add_order_btn = tk.Button(root, text="Add Order", command=self.add_order)
        add_order_btn.grid(row=len(data) + 3, column=2, padx=10, pady=5, columnspan=5)

    def add_order(self):
        # Get the name input from the entry widget
        name = self.name_entry.get()

        # You can add functionality here to process the new order, such as adding it to the data list and updating the UI.


if __name__ == "__main__":
    root = tk.Tk()
    app = FoodOrderApp(root)
    root.mainloop()
