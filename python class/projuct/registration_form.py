import tkinter as tk
from tkinter import messagebox

# Color Palette
BG_COLOR = "#1e1e2e"
CARD_BG = "#24273a"
ACCENT_COLOR = "#89b4fa"
TEXT_COLOR = "#cdd6f4"
ENTRY_BG = "#313244"
BTN_BG = "#45475a"
SUCCESS_COLOR = "#a6e3a1"

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")
        self.root.geometry("400x550")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)
        
        # Center the window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (550 // 2)
        self.root.geometry(f"400x550+{x}+{y}")

        self.create_widgets()

    def create_widgets(self):
        # Main Card Frame
        main_frame = tk.Frame(self.root, bg=CARD_BG, padx=40, pady=40)
        main_frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=500)

        # Title
        title_label = tk.Label(
            main_frame, 
            text="Registration", 
            font=("Helvetica", 24, "bold"), 
            bg=CARD_BG, 
            fg=ACCENT_COLOR
        )
        title_label.pack(pady=(0, 10))

        subtitle_label = tk.Label(
            main_frame, 
            text="Fill in your details below", 
            font=("Helvetica", 10), 
            bg=CARD_BG, 
            fg="#9399b2"
        )
        subtitle_label.pack(pady=(0, 30))

        # Input Fields
        self.name_entry = self.create_input(main_frame, "Full Name")
        self.email_entry = self.create_input(main_frame, "Email Address")
        self.password_entry = self.create_input(main_frame, "Password", show="*")
        
        # Register Button
        self.register_btn = tk.Button(
            main_frame,
            text="REGISTER NOW",
            command=self.handle_registration,
            font=("Helvetica", 12, "bold"),
            bg=ACCENT_COLOR,
            fg=BG_COLOR,
            activebackground="#b4befe",
            activeforeground=BG_COLOR,
            relief="flat",
            cursor="hand2",
            pady=10
        )
        self.register_btn.pack(fill="x", pady=(20, 0))

        # Footer
        footer_frame = tk.Frame(main_frame, bg=CARD_BG)
        footer_frame.pack(pady=(20, 0))
        
        tk.Label(footer_frame, text="Already have an account?", bg=CARD_BG, fg=TEXT_COLOR, font=("Helvetica", 9)).pack(side="left")
        login_lbl = tk.Label(footer_frame, text=" Login", bg=CARD_BG, fg=ACCENT_COLOR, font=("Helvetica", 9, "bold"), cursor="hand2")
        login_lbl.pack(side="left")

    def create_input(self, parent, label_text, show=None):
        frame = tk.Frame(parent, bg=CARD_BG)
        frame.pack(fill="x", pady=10)

        label = tk.Label(frame, text=label_text, bg=CARD_BG, fg=TEXT_COLOR, font=("Helvetica", 10, "bold"))
        label.pack(anchor="w", pady=(0, 5))

        entry = tk.Entry(
            frame,
            font=("Helvetica", 11),
            bg=ENTRY_BG,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief="flat",
            borderwidth=0,
            highlightthickness=1,
            highlightbackground=BTN_BG,
            highlightcolor=ACCENT_COLOR,
            show=show
        )
        entry.pack(fill="x", ipady=8, padx=1)
        return entry

    def handle_registration(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not name or not email or not password:
            messagebox.showwarning("Incomplete Form", "Please fill in all fields.")
            return

        # Simple success message
        messagebox.showinfo("Success", f"Welcome, {name}!\nYour account has been created.")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()
