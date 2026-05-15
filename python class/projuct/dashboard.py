import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys

# Color Palette
BG_COLOR = "#1e1e2e"  # Deep dark blue/grey
ACCENT_COLOR = "#89b4fa"  # Soft blue
TEXT_COLOR = "#cdd6f4"  # Off-white
HOVER_COLOR = "#313244"  # Lighter dark for hover
BTN_BG = "#45475a"  # Button background

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Dashboard")
        self.root.geometry("600x450")
        self.root.configure(bg=BG_COLOR)
        
        # Prevent resizing to keep the layout clean
        self.root.resizable(False, False)
        
        self.create_widgets()

    def create_widgets(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg=BG_COLOR, pady=30)
        header_frame.pack(fill="x")
        
        header_label = tk.Label(
            header_frame, 
            text="PYTHON PROJECT HUB", 
            font=("Helvetica", 28, "bold"), 
            bg=BG_COLOR, 
            fg=ACCENT_COLOR
        )
        header_label.pack()
        
        subtitle_label = tk.Label(
            header_frame, 
            text="Choose an application to launch", 
            font=("Helvetica", 12), 
            bg=BG_COLOR, 
            fg=TEXT_COLOR
        )
        subtitle_label.pack(pady=5)

        # Main Buttons Frame
        btn_frame = tk.Frame(self.root, bg=BG_COLOR, pady=20)
        btn_frame.pack(expand=True)

        self.create_button(btn_frame, "🐍 Play Snake Game", self.launch_snake)
        self.create_button(btn_frame, "⏰ Digital Clock", self.launch_clock)
        self.create_button(btn_frame, "📝 Registration Form", self.launch_registration_form)
        self.create_button(btn_frame, "❌ Exit Dashboard", self.root.quit, is_exit=True)

        # Footer
        footer_label = tk.Label(
            self.root, 
            text="Developed by Indhuja", 
            font=("Helvetica", 9, "italic"), 
            bg=BG_COLOR, 
            fg="#585b70"
        )
        footer_label.pack(side="bottom", pady=10)

    def create_button(self, parent, text, command, is_exit=False):
        color = "#f38ba8" if is_exit else BTN_BG  # Red-ish for exit
        
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Helvetica", 14, "bold"),
            bg=color,
            fg=TEXT_COLOR,
            activebackground=ACCENT_COLOR,
            activeforeground=BG_COLOR,
            relief="flat",
            width=25,
            pady=12,
            cursor="hand2"
        )
        btn.pack(pady=10)
        
        # Hover effects
        btn.bind("<Enter>", lambda e: btn.config(bg=ACCENT_COLOR if not is_exit else "#eba0ac", fg=BG_COLOR))
        btn.bind("<Leave>", lambda e: btn.config(bg=color, fg=TEXT_COLOR))

    def launch_snake(self):
        try:
            # Using absolute path logic to ensure it finds the file
            script_path = os.path.join(os.path.dirname(__file__), "projuct.py")
            subprocess.Popen([sys.executable, script_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch Snake Game: {e}")

    def launch_clock(self):
        try:
            script_path = os.path.join(os.path.dirname(__file__), "main_gui.py")
            subprocess.Popen([sys.executable, script_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch Digital Clock: {e}")

    def launch_registration_form(self):
        try:
            script_path = os.path.join(os.path.dirname(__file__), "registration_form.py")
            subprocess.Popen([sys.executable, script_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch Registration Form: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
