import tkinter as tk
import time

def update_time():
    """Update the time label every second."""
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    # Check current date as well
    current_date = time.strftime("%A, %B %d, %Y")
    date_label.config(text=current_date)
    root.after(1000, update_time)

def toggle_theme():
    """Switch between Light and Dark mode."""
    if root.cget("bg") == "white":
        # Switch to Dark Mode
        root.config(bg="#2c3e50")
        time_label.config(bg="#2c3e50", fg="#ecf0f1")
        date_label.config(bg="#2c3e50", fg="#bdc3c7")
        theme_btn.config(text="Switch to Light Mode", bg="#ecf0f1", fg="#2c3e50")
    else:
        # Switch to Light Mode
        root.config(bg="white")
        time_label.config(bg="white", fg="#2c3e50")
        date_label.config(bg="white", fg="#7f8c8d")
        theme_btn.config(text="Switch to Dark Mode", bg="#2c3e50", fg="white")

# Start updating the clock
def run_clock():
    global root, time_label, date_label, theme_btn
    
    # 1. Main Window Setup
    root = tk.Tk()
    root.title("Digital Clock")
    root.geometry("450x250")
    root.config(bg="#2c3e50")  # Start in dark mode

    # 2. Time Label
    time_label = tk.Label(
        root, 
        text="00:00:00", 
        font=("Arial", 60, "bold"), 
        bg="#2c3e50", 
        fg="#ecf0f1"
    )
    time_label.pack(expand=True)

    # 3. Date Label
    date_label = tk.Label(
        root, 
        text="", 
        font=("Arial", 14), 
        bg="#2c3e50", 
        fg="#bdc3c7"
    )
    date_label.pack(pady=(0, 20))

    # 4. Theme Toggle Button
    theme_btn = tk.Button(
        root, 
        text="Switch to Light Mode", 
        command=toggle_theme,
        font=("Arial", 10),
        bg="#ecf0f1",
        fg="#2c3e50",
        relief="flat",
        padx=10,
        pady=5
    )
    theme_btn.pack(pady=10)

    update_time()
    root.mainloop()

if __name__ == "__main__":
    run_clock()

