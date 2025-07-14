import tkinter as tk
import pickle


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 1  # fix: initialize total to 1 instead of 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

class Counter:
    def __init__(self):
        self.linked_list = LinkedList()
        self.linked_list.append(0)
        self.num_loops = 15
        self.value = 0

    def increment(self):
        cur_node = self.linked_list.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        if cur_node.data == 9:
            self.linked_list.append(0)
            self.num_loops += 1
            self.value = 0
        else:
            cur_node.data += 1
            self.value += 1

    def decrement(self):
        if self.linked_list.length() == 1 and self.linked_list.head.data == 0:
            self.value = 0
            return
        cur_node = self.linked_list.head
        prev_node = None
        while cur_node.next is not None:
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node.data == 0:
            if self.num_loops == 0:
                self.value = 0
            else:
                prev_node.next = None
                if self.linked_list.length() > 1:
                    self.num_loops -= 1
                self.value = 9
        else:
            cur_node.data -= 1
            self.value -= 1

                                                        
class Main_Window:
    def __init__(self):
        self.window1 = tk.Tk()
        self.window1.title("Inventory Management System")
        self.window1.geometry("400x450")
        self.window1.config(bg='#90C2E7')
                
        self.label = tk.Label(self.window1, text="Choose Product: ", bg="#454545", fg="white", font=("Arial", 24))
        self.label.pack()
        
        self.button1 = tk.Button(self.window1, text="Shirts", command=lambda: self.new_window("Shirts"), bg="#454545", fg="white", padx=12, pady=8, font=("Arial", 24))
        self.button1.pack()
        
        self.button2 = tk.Button(self.window1, text="T-Shirts", command=lambda: self.new_window("T-Shirts"), bg="#454545", fg="white", padx=12, pady=8, font=("Arial", 24))
        self.button2.pack()
        
        self.button3 = tk.Button(self.window1, text="Pants", command=lambda: self.new_window("Pants"), bg="#454545", fg="white", padx=12, pady=8, font=("Arial", 24))
        self.button3.pack()
        
        self.button4 = tk.Button(self.window1, text="Shorts", command=lambda: self.new_window("Shorts"), bg="#454545", fg="white", padx=12, pady=8, font=("Arial", 24))
        self.button4.pack()
        
        self.button5 = tk.Button(self.window1, text="Socks", command=lambda: self.new_window("Socks"), bg="#454545", fg="white", padx=12, pady=8, font=("Arial", 24))
        self.button5.pack()
        
        self.button6 = tk.Button(self.window1, text="Shoes", command=lambda: self.new_window("Shoes"), bg="#454545", fg="white", padx=12, pady=8, font=("Arial", 24))
        self.button6.pack()
        
        self.close_button = tk.Button(self.window1, text="Close", command=self.window1.quit, bg="#454545", fg="white", padx=12, pady=8, font=("Arial", 24))
        self.close_button.pack()
        
               
    def new_window(self, title):
        CounterGUI(title)


class CounterGUI:
    def __init__(self, title):
        self.counter = Counter()
        self.title = title
        
        
        
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry("300x300")
        
        self.label = tk.Label(self.window, text=title + "'s inventory")
        self.label.pack()

        self.counter_label = tk.Label(self.window, text="0", font=("Arial", 24))
        self.counter_label.pack()

        self.increment_button = tk.Button(self.window, text="Bought", command=self.increment)
        self.increment_button.pack()

        self.decrement_button = tk.Button(self.window, text="Sold", command=self.decrement)
        self.decrement_button.pack()
        
        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset)
        self.reset_button.pack()
        
        self.loops_label = tk.Label(self.window, text="Boxes: ", font=("Arial", 12))
        self.loops_label.pack()
        
        self.closebutton = tk.Button(self.window, text="Close", command=self.window.quit)
        self.closebutton.pack()
        
        self.save_button = tk.Button(self.window, text="Save", command=self.save_counter)
        self.save_button.pack()
        
        self.message_label = tk.Label(self.window, text="")
        self.message_label.pack()
        
        self.load_counter()
        
        self.update_labels()

        self.window.mainloop()
        
    def save_counter(self):
        with open(f"{self.title}_counter.pickle", "wb") as f:
            data = {
                "value": self.counter.value,
                "num_loops": self.counter.num_loops,
                "linked_list": self.counter.linked_list
            }
            pickle.dump(data, f)
            
    def load_counter(self):
        try:
            with open(f"{self.title}_counter.pickle", "rb") as f:
                data = pickle.load(f)
                self.counter.value = data["value"]
                self.counter.num_loops = data["num_loops"]
                self.counter.linked_list = data["linked_list"]
        except FileNotFoundError:
            pass
                     
       
    def increment(self):
        self.counter.increment()
        self.update_labels()

    def decrement(self):
        self.counter.decrement()
        self.update_labels()
        
    def reset(self):
        self.counter = Counter()
        self.counter.num_loops = 0
        self.update_labels()

    def update_labels(self):
        self.counter_label.config(text=str(self.counter.value))
        self.loops_label.config(text=f"Boxes: {self.counter.num_loops}")
        
        if self.counter.num_loops > 0 and self.counter.num_loops <= 3:
            message = "Order much more boxes. \nTop seller product."
        elif self.counter.num_loops > 3 and self.counter.num_loops <= 7:
            message = "Order more boxes. \nGood selling product."
        elif self.counter.num_loops > 7 and self.counter.num_loops <= 11:
            message = "Order some boxes. \nRegular product."
        else:
            message = "Don't order any more boxes. \nProduct is not selling enough."

        self.message_label.config(text=f"Boxes: {self.counter.num_loops} - " + message, bg="#FF0800", fg="white")

my_window = Main_Window()
my_window.window1.mainloop()
