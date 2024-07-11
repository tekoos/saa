import tkinter as tk
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import subprocess

def authenticate(username, password):
    return username == "" and password == ""  # Replace with actual authentication logic

def login_clicked():
    username = username_entry.get()
    password = password_entry.get()
    if authenticate(username, password):
        login_status_label.configure(text="Login successful", text_color="green")
        open_main_window()
    else:
        login_status_label.configure(text="Invalid username or password", text_color="red")

def open_main_window():
    global main_window, side_img_data, img_Navigation, img_AI_Chatbot, img_Hospital_System, img_talksys
    app.withdraw()

    main_window = tk.Toplevel(app)
    main_window.title("Main Window")
    main_window.geometry("1024x600")
    main_window.resizable(0, 0)
    main_window.protocol("WM_DELETE_WINDOW", terminate_app)

    side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(500, 600))
    CTkLabel(master=main_window, text="", image=side_img).pack(side="left", padx=(20, 0))

    button_frame = CTkFrame(master=main_window, width=600, height=600)
    button_frame.pack_propagate(0)
    button_frame.pack(expand=True, side="right")

    CTkLabel(master=button_frame, text="Welcome to the Main Window!", text_color="#601E88", anchor="center", justify="center", font=("Arial Bold", 16)).grid(row=0, columnspan=2, pady=(20, 50))

    img_nav = Image.open("Navigation.png").resize((150, 100), Image.LANCZOS)
    img_off = Image.open("AI.png").resize((150, 100), Image.LANCZOS)
    img_hos = Image.open("Hospital.png").resize((150, 100), Image.LANCZOS)
    img_talk = Image.open("talk.png").resize((150, 100), Image.LANCZOS)

    img_Navigation = ImageTk.PhotoImage(img_nav)
    img_AI_Chatbot = ImageTk.PhotoImage(img_off)
    img_Hospital_System = ImageTk.PhotoImage(img_hos)
    img_talksys = ImageTk.PhotoImage(img_talk)

    # Navigation button
    btn_frame1 = tk.Frame(button_frame, width=150, height=120)
    btn_frame1.grid_propagate(0)
    btn_frame1.grid(row=1, column=0, padx=10, pady=5)
    tk.Label(btn_frame1, text="Navigation", font=("Arial", 12)).pack()
    btn_Navigation = tk.Button(btn_frame1, image=img_Navigation, command=option1_clicked)
    btn_Navigation.image = img_Navigation
    btn_Navigation.pack()

    # AI Chatbot button
    btn_frame2 = tk.Frame(button_frame, width=150, height=120)
    btn_frame2.grid_propagate(0)
    btn_frame2.grid(row=1, column=1, padx=10, pady=5)
    tk.Label(btn_frame2, text="AI Chatbot", font=("Arial", 12)).pack()
    btn_AI = tk.Button(btn_frame2, image=img_AI_Chatbot, command=option2_clicked)
    btn_AI.image = img_AI_Chatbot
    btn_AI.pack()

    # Clinic button
    btn_frame3 = tk.Frame(button_frame, width=150, height=120)
    btn_frame3.grid_propagate(0)
    btn_frame3.grid(row=2, column=0, padx=10, pady=5)
    tk.Label(btn_frame3, text="Clinic", font=("Arial", 12)).pack()
    btn_Hospital = tk.Button(btn_frame3, image=img_Hospital_System, command=option3_clicked)
    btn_Hospital.image = img_Hospital_System
    btn_Hospital.pack()

    # Talk With ME button
    btn_frame4 = tk.Frame(button_frame, width=150, height=120)
    btn_frame4.grid_propagate(0)
    btn_frame4.grid(row=2, column=1, padx=10, pady=5)
    tk.Label(btn_frame4, text="Talk With ME", font=("Arial", 12)).pack()
    btn_Talk = tk.Button(btn_frame4, image=img_talksys, command=option4_clicked)
    btn_Talk.image = img_talksys
    btn_Talk.pack()

def option1_clicked():
    main_window.withdraw()
    script_path = ""  # Provide the actual path to the script
    python_executable = sys.executable
    subprocess.Popen([python_executable, script_path])

def start_chatbot(language):
    main_window.withdraw()
    script_path = "/home/marwan/GUI/GeminiArabic.py" if language == "Arabic" else "/home/marwan/GUI/GeminiEnglish.py"
    python_executable = sys.executable
    subprocess.Popen([python_executable, script_path])

def option2_clicked():
    main_window.withdraw()
    side_img_data = Image.open("side-img.png")
    side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(500, 600))
    language_window = tk.Toplevel(main_window)
    language_window.title("Language Model")
    language_window.geometry("1024x600")
    language_window.protocol("WM_DELETE_WINDOW", lambda: return_to_main_window(language_window))

    CTkLabel(master=language_window, text="", image=side_img).pack(side="left", fill="y")

    button_frame = CTkFrame(master=language_window, width=512, height=600)
    button_frame.pack_propagate(0)
    button_frame.pack(expand=True, side="right")

    tk.Label(button_frame, text="Please select a language").pack(pady=10)

    button_width = 20
    button_height = 2

    tk.Button(button_frame, text="Arabic", command=lambda: start_chatbot("Arabic"), width=button_width, height=button_height).pack(pady=10)
    tk.Button(button_frame, text="English", command=lambda: start_chatbot("English"), width=button_width, height=button_height).pack(pady=10)
    tk.Button(button_frame, text="Return", command=lambda: return_to_main_window(language_window), width=button_width, height=button_height).pack(pady=10)

def option3_clicked():
    main_window.withdraw()
    side_img_data = Image.open("side-img.png")
    side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(500, 600))
    clinic_window = tk.Toplevel(main_window)
    clinic_window.title("Clinic")
    clinic_window.geometry("1024x600")

    CTkLabel(master=clinic_window, text="", image=side_img).pack(side="left", fill="y")

    button_frame = CTkFrame(master=clinic_window, width=512, height=600)
    button_frame.pack_propagate(0)
    button_frame.pack(expand=True, side="right")

    tk.Label(button_frame, text="Welcome to our clinics system").pack(pady=10)

    button_width = 20
    button_height = 2

    tk.Button(button_frame, text="Available Clinic", command=run_importtime_script, width=button_width, height=button_height).pack(pady=10)
    tk.Button(button_frame, text="Scheduling", command=run_scheduling_script, width=button_width, height=button_height).pack(pady=10)
    tk.Button(button_frame, text="Return", command=lambda: return_to_main_window(clinic_window), width=button_width, height=button_height).pack(pady=10)

def create_TALK_WITH_ME_window(main_window):
    side_img_data = Image.open("side-img.png")
    side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(500, 600))
    talk_window = tk.Toplevel(main_window)
    talk_window.title("Talk With Me")
    talk_window.geometry("1024x600")

    CTkLabel(master=talk_window, text="", image=side_img).pack(side="left", fill="y")

    button_frame = CTkFrame(master=talk_window, width=512, height=600)
    button_frame.pack_propagate(0)
    button_frame.pack(expand=True, side="right")

    tk.Label(button_frame, text="Please select an option").pack(pady=10)

    button_width = 20
    button_height = 2

    tk.Button(button_frame, text="Text", command=lambda: start_chatbot("Text"), width=button_width, height=button_height).pack(pady=10)
    tk.Button(button_frame, text="Speech", command=lambda: start_chatbot("Speech"), width=button_width, height=button_height).pack(pady=10)
    tk.Button(button_frame, text="Return", command=lambda: return_to_main_window(talk_window), width=button_width, height=button_height).pack(pady=10)

def option4_clicked():
    global main_window
    main_window.withdraw()
    create_TALK_WITH_ME_window(main_window)

def run_importtime_script():
    python_executable = sys.executable
    script_path = "/home/marwan/GUI/importtime.py"
    subprocess.Popen([python_executable, script_path])

def run_scheduling_script():
    python_executable = sys.executable
    script_path = "/path/to/scheduling_script.py"  # Replace with the actual path to your scheduling script
    subprocess.Popen([python_executable, script_path])

def return_to_main_window(window):
    window.destroy()
    main_window.deiconify()

def terminate_app():
    app.quit()
    app.destroy()
    sys.exit()

app = CTk()
app.title("AASTMT")
app.geometry("1024x600")
app.resizable(0, 0)
app.protocol("WM_DELETE_WINDOW", terminate_app)

# Load images
side_img_data = Image.open("side-img.png")
email_icon_data = Image.open("email-icon.png")
password_icon_data = Image.open("password-icon.png")
google_icon_data = Image.open("google-icon.png")

# Create CTkImage instances
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(600, 600))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(25, 25))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(22, 22))
google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(22, 22))

# Create widgets for the login screen
CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left", padx=(0, 0))

frame = CTkFrame(master=app, width=350, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 28)).pack(anchor="w", pady=(50, 10), padx=(5, 0))
CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", padx=(5, 0))

CTkLabel(master=frame, text="  Username:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 16), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
username_entry = CTkEntry(master=frame, width=275, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
username_entry.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 16), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
password_entry = CTkEntry(master=frame, width=275, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
password_entry.pack(anchor="w", padx=(25, 0))

# Login button
login_button = CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 14), text_color="#ffffff", width=275, command=login_clicked)
login_button.pack(anchor="w", pady=(40, 0), padx=(25, 0))

# Continue With Google button (with icon only)
google_button = CTkButton(master=frame, fg_color="#EEEEEE", hover_color="#EEEEEE", width=275, image=google_icon)
google_button.pack(anchor="w", pady=(20, 0), padx=(25, 0))

# Login status label
login_status_label = CTkLabel(master=frame, text="", text_color="green")
login_status_label.pack()

app.mainloop()
