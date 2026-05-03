import tkinter as tk
from tkinter import messagebox

# IMPORT YOUR MODULES
from src.user import User
from src.schedule import Schedule
from src.booking import Booking
from src.payment import Payment
from src.notification import Notification
from src.search import Search


# ========================
# APP CLASS
# ========================
class PRASAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PRASA Smart Passenger System")
        self.root.geometry("600x500")

        self.user = User("admin", "1234")
        self.schedule = Schedule()
        self.search = Search()
        self.notification = Notification()

        self.create_login_screen()

    # ========================
    # LOGIN SCREEN
    # ========================
    def create_login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="PRASA Login", font=("Arial", 16)).pack(pady=20)

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, "admin")

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, "1234")

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.user.login(username, password)

        if result == "Login successful":
            messagebox.showinfo("Success", result)
            self.create_main_menu()
        else:
            messagebox.showerror("Error", result)

    # ========================
    # MAIN MENU
    # ========================
    def create_main_menu(self):
        self.clear_screen()

        tk.Label(self.root, text="PRASA Dashboard", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="View Schedule", command=self.show_schedule).pack(pady=10)
        tk.Button(self.root, text="Search Train", command=self.search_train).pack(pady=10)
        tk.Button(self.root, text="Book Train", command=self.book_train).pack(pady=10)
        tk.Button(self.root, text="View Notifications", command=self.show_notifications).pack(pady=10)

    # ========================
    # VIEW SCHEDULE
    # ========================
    def show_schedule(self):
        self.clear_screen()

        tk.Label(self.root, text="Train Schedule", font=("Arial", 14)).pack(pady=10)

        schedules = self.schedule.display()

        for s in schedules:
            text = f"{s['train']} | {s['route']} | {s['departure']} - {s['arrival']} | Platform {s['platform']} | {s['status']}"
            tk.Label(self.root, text=text).pack()

        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=20)

    # ========================
    # SEARCH TRAIN
    # ========================
    def search_train(self):
        self.clear_screen()

        tk.Label(self.root, text="Search Train by Route").pack(pady=10)

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack(pady=5)

        tk.Button(self.root, text="Search", command=self.perform_search).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=10)

    def perform_search(self):
        route = self.search_entry.get()
        results = self.search.search_train(self.schedule.display(), route)

        if results:
            result_text = "\n".join([str(r) for r in results])
            messagebox.showinfo("Results", result_text)
        else:
            messagebox.showinfo("Results", "No trains found")

    # ========================
    # BOOK TRAIN
    # ========================
    def book_train(self):
        self.clear_screen()

        tk.Label(self.root, text="Enter Train ID to Book").pack(pady=10)

        self.train_entry = tk.Entry(self.root)
        self.train_entry.pack(pady=5)

        tk.Button(self.root, text="Confirm Booking", command=self.confirm_booking).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=10)

    def confirm_booking(self):
        train_id = self.train_entry.get()

        booking = Booking("admin", train_id)
        booking_msg = booking.create_booking()

        payment = Payment(150)
        payment_msg = payment.process_payment()

        messagebox.showinfo("Booking", f"{booking_msg}\n{payment_msg}")

    # ========================
    # NOTIFICATIONS
    # ========================
    def show_notifications(self):
        self.clear_screen()

        tk.Label(self.root, text="Notifications", font=("Arial", 14)).pack(pady=10)

        updates = self.schedule.get_updates()

        if updates:
            for u in updates:
                msg = self.notification.send(u)
                tk.Label(self.root, text=msg).pack()
        else:
            tk.Label(self.root, text="No new notifications").pack()

        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=20)

    # ========================
    # CLEAR SCREEN
    # ========================
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ========================
# RUN APP
# ========================
if __name__ == "__main__":
    root = tk.Tk()
    app = PRASAApp(root)
    root.mainloop()