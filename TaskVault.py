import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from tkcalendar import DateEntry

# --- Theme Configuration ---
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")

DATA_FILE = "users_data.json"


# --- Data Management Helpers ---
def load_data():
    """Loads JSON data from file or returns an empty dict if not existing."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return {}


def save_data(data):
    """Saves the main data dictionary into a local JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# --- Application Class ---
class TaskVaultApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("TaskVault: Academic Deadline & Project Manager")
        self.geometry("850x600")
        self.resizable(False, False)

        self.current_user = None
        self.data = load_data()

        # Main Container
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.show_login_screen()

    def clear_container(self):
        """Clears all widgets from the main container frame."""
        for widget in self.container.winfo_children():
            widget.destroy()

    # 1. LOGIN & REGISTRATION SCREENS
    def show_login_screen(self):
        self.clear_container()

        frame = ctk.CTkFrame(self.container, width=350, height=400, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        title = ctk.CTkLabel(
            frame,
            text="TaskVault Login",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        title.pack(pady=(30, 20))

        self.username_entry = ctk.CTkEntry(
            frame, placeholder_text="Username", width=250
        )
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            frame, placeholder_text="Password", show="*", width=250
        )
        self.password_entry.pack(pady=10)

        login_btn = ctk.CTkButton(
            frame, text="Sign In", width=250, command=self.handle_login
        )
        login_btn.pack(pady=(20, 10))

        signup_btn = ctk.CTkButton(
            frame,
            text="Create an Account",
            width=250,
            fg_color="transparent",
            border_width=1,
            command=self.show_register_screen,
        )
        signup_btn.pack(pady=5)

    def show_register_screen(self):
        self.clear_container()

        frame = ctk.CTkFrame(self.container, width=350, height=400, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        title = ctk.CTkLabel(
            frame,
            text="TaskVault Sign Up",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        title.pack(pady=(30, 20))

        self.reg_username_entry = ctk.CTkEntry(
            frame, placeholder_text="Choose Username", width=250
        )
        self.reg_username_entry.pack(pady=10)

        self.reg_password_entry = ctk.CTkEntry(
            frame, placeholder_text="Choose Password", show="*", width=250
        )
        self.reg_password_entry.pack(pady=10)

        register_btn = ctk.CTkButton(
            frame, text="Register", width=250, command=self.handle_register
        )
        register_btn.pack(pady=(20, 10))

        back_btn = ctk.CTkButton(
            frame,
            text="Back to Login",
            width=250,
            fg_color="transparent",
            border_width=1,
            command=self.show_login_screen,
        )
        back_btn.pack(pady=5)

    def handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        if username in self.data and self.data[username]["password"] == password:
            self.current_user = username
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def handle_register(self):
        username = self.reg_username_entry.get().strip()
        password = self.reg_password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        if username in self.data:
            messagebox.showerror("Error", "Username already exists!")
            return

        self.data[username] = {"password": password, "tasks": []}
        save_data(self.data)
        messagebox.showinfo("Success", "Account created successfully! Please log in.")
        self.show_login_screen()


    # 2. MAIN DASHBOARD SCREEN
    def show_dashboard(self):
        self.clear_container()

        # Sidebar navigation / Top bar
        top_bar = ctk.CTkFrame(self.container, height=60, corner_radius=0)
        top_bar.pack(fill="x", side="top")

        welcome_label = ctk.CTkLabel(
            top_bar,
            text=f"Welcome, {self.current_user}!",
            font=ctk.CTkFont(size=18, weight="bold"),
        )
        welcome_label.pack(side="left", padx=20, pady=15)

        logout_btn = ctk.CTkButton(
            top_bar,
            text="Logout",
            width=80,
            fg_color="#D32F2F",
            hover_color="#9A0007",
            command=self.show_login_screen,
        )
        logout_btn.pack(side="right", padx=20)

        # Content Layout
        content_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Left Column: Add Task Form
        form_frame = ctk.CTkFrame(content_frame, width=300, corner_radius=10)
        form_frame.pack(side="left", fill="y", padx=(0, 10))

        form_title = ctk.CTkLabel(
            form_frame, text="Add New Task", font=ctk.CTkFont(size=16, weight="bold")
        )
        form_title.pack(pady=(15, 10))

        self.task_name_entry = ctk.CTkEntry(
            form_frame, placeholder_text="Task Name (e.g., Quiz 1)", width=240
        )
        self.task_name_entry.pack(pady=8)

        self.course_entry = ctk.CTkEntry(
            form_frame, placeholder_text="Course (e.g., APPDAET)", width=240
        )
        self.course_entry.pack(pady=8)

        self.task_type_combo = ctk.CTkComboBox(
            form_frame,
            values=["Assignment", "Quiz", "Examination", "Project"],
            width=240,
        )
        self.task_type_combo.pack(pady=8)

        # TkCalendar Date Picker Integration
        date_label = ctk.CTkLabel(
            form_frame, text="Select Deadline:", font=ctk.CTkFont(size=12)
        )
        date_label.pack(pady=(10, 2))

        self.date_picker = DateEntry(
            form_frame,
            width=18,
            background="darkblue",
            foreground="white",
            border_width=2,
            date_pattern="yyyy-mm-dd",
        )
        self.date_picker.pack(pady=(0, 15))

        add_task_btn = ctk.CTkButton(
            form_frame, text="Add Task", width=240, command=self.add_task
        )
        add_task_btn.pack(pady=10)

        # Right Column: Task Display Area
        list_frame = ctk.CTkFrame(content_frame)
        list_frame.pack(side="right", fill="both", expand=True)

        list_title = ctk.CTkLabel(
            list_frame, text="Your Academic Tasks", font=ctk.CTkFont(size=16, weight="bold")
        )
        list_title.pack(pady=10)

        self.task_scrollable = ctk.CTkScrollableFrame(list_frame)
        self.task_scrollable.pack(fill="both", expand=True, padx=10, pady=10)

        self.refresh_task_list()


    # 3. TASK OPERATIONS & VALIDATION
    def add_task(self):
        name = self.task_name_entry.get().strip()
        course = self.course_entry.get().strip()
        task_type = self.task_type_combo.get()
        deadline_str = self.date_picker.get()

        # Validation: Non-empty inputs
        if not name or not course:
            messagebox.showerror("Validation Error", "All fields are required!")
            return

        # Check for duplicate task names
        user_tasks = self.data[self.current_user]["tasks"]
        for task in user_tasks:
            if task["name"].lower() == name.lower():
                messagebox.showerror(
                    "Validation Error", "A task with this name already exists!"
                )
                return

        # Create task structure
        new_task = {
            "name": name,
            "course": course,
            "type": task_type,
            "deadline": deadline_str,
            "completed": False,
        }

        user_tasks.append(new_task)
        save_data(self.data)

        # Reset Form
        self.task_name_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)

        self.refresh_task_list()
        messagebox.showinfo("Success", "Task added successfully!")

    def refresh_task_list(self):
        """Renders all tasks with Overdue / Completed / Pending detection."""
        for widget in self.task_scrollable.winfo_children():
            widget.destroy()

        user_tasks = self.data[self.current_user]["tasks"]

        if not user_tasks:
            no_task_lbl = ctk.CTkLabel(
                self.task_scrollable,
                text="No tasks added yet.",
                font=ctk.CTkFont(size=14),
            )
            no_task_lbl.pack(pady=20)
            return

        today = datetime.now().date()

        for idx, task in enumerate(user_tasks):
            card = ctk.CTkFrame(self.task_scrollable, corner_radius=8)
            card.pack(fill="x", padx=5, pady=5)

            task_date = datetime.strptime(task["deadline"], "%Y-%m-%d").date()

            # Determine Status Badge
            if task["completed"]:
                status_str = "COMPLETED"
                status_color = "#2E7D32"  # Green
            elif task_date < today:
                status_str = "OVERDUE"
                status_color = "#C62828"  # Red
            else:
                status_str = "PENDING"
                status_color = "#E65100"  # Orange

            info_text = (
                f"[{task['course']}] {task['name']} ({task['type']})\n"
                f"Deadline: {task['deadline']}"
            )

            task_lbl = ctk.CTkLabel(
                card, text=info_text, justify="left", font=ctk.CTkFont(size=13)
            )
            task_lbl.pack(side="left", padx=10, pady=10)

            status_badge = ctk.CTkLabel(
                card,
                text=status_str,
                text_color=status_color,
                font=ctk.CTkFont(size=11, weight="bold"),
            )
            status_badge.pack(side="left", padx=10)

            # Action Buttons
            del_btn = ctk.CTkButton(
                card,
                text="Delete",
                width=60,
                fg_color="#D32F2F",
                hover_color="#9A0007",
                command=lambda i=idx: self.delete_task(i),
            )
            del_btn.pack(side="right", padx=5, pady=10)

            toggle_text = "Mark Pending" if task["completed"] else "Mark Done"
            toggle_btn = ctk.CTkButton(
                card,
                text=toggle_text,
                width=90,
                command=lambda i=idx: self.toggle_task(i),
            )
            toggle_btn.pack(side="right", padx=5, pady=10)

    def toggle_task(self, index):
        user_tasks = self.data[self.current_user]["tasks"]
        user_tasks[index]["completed"] = not user_tasks[index]["completed"]
        save_data(self.data)
        self.refresh_task_list()

    def delete_task(self, index):
        user_tasks = self.data[self.current_user]["tasks"]
        del user_tasks[index]
        save_data(self.data)
        self.refresh_task_list()


# Execution Entry Point
if __name__ == "__main__":
    app = TaskVaultApp()
    app.mainloop()