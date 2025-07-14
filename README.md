# 🧮 Inventory Management System (Tkinter + Python)

A simple, beginner-friendly inventory management application with a graphical interface using **Python** and **Tkinter**. This tool allows users to track stock levels for different products, with intuitive increment and decrement buttons. It also gives stock advice based on the number of boxes in stock and saves inventory data between sessions using `pickle`.

---

## 📦 Features

- ✅ GUI-based inventory tracker
- 🔢 Custom counter using a linked list
- 📊 Visual stock indicators with suggestions:
  - "Top seller product"
  - "Good selling product"
  - "Regular product"
  - "Product is not selling enough"
- 💾 Data persistence via `.pickle` files
- 👕 Tracks multiple product types: Shirts, T-Shirts, Pants, Shorts, Socks, and Shoes

---

## 🖼️ Preview

> Each product opens its own window with the ability to track purchases (`Bought`) and sales (`Sold`). The app gives recommendations based on how many "boxes" (loops) have been sold.

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (built-in GUI module)
- Pickle (for saving/loading data)
- Custom Linked List (for counting logic)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/inventory-management-system.git
   cd inventory-management-system

   
inventory-management-system/
│
├── inventory.py            # Main application file
├── *.pickle                # Auto-generated files storing inventory data
└── README.md               # Project documentation
