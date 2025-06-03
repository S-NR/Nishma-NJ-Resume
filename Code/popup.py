# installs 
# pip install pyinstaller
# pip install pillow
# pip install pywebview 

# c:\python39\python.exe -m PyInstaller popup.py --onefile --hidden-import=PIL --hidden-import=PIL.ImageTk
# python -m PyInstaller --onefile --windowed popup.py
# "C:\Users\Nishma Nj\AppData\Local\Programs\Python\Python311\python.exe" -m PyInstaller popup.py --onefile --hidden-import=PIL --hidden-import=PIL.ImageTk

import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkfont
import webbrowser
import webview
from tkinter import messagebox

import smtplib
from email.mime.text import MIMEText

# ---------- Constants ----------
FONT_NORMAL = ("Arial", 10)
FONT_BOLD = ("Arial", 10, "bold")
FONT_HEADER = ("Arial", 18)
FONT_EMOJI = ("Segoe UI Emoji", 12, "bold")  # Optional

# ---------- Setup Root ----------
root = tk.Tk()
root.title("MY BIO")
root.geometry("600x500")
root.resizable(False, False)

# ---------- Fonts ----------
normal_font = tkfont.Font(family="Arial", size=10)
bold_font = tkfont.Font(family="Arial", size=10, weight="bold")

# ---------- Load Image ----------
# image = Image.open("nishma.png").resize((100, 100))
image = Image.open("nishma.png")
image = image.resize((100,100), Image.Resampling.LANCZOS)  # Use this instead of ANTIALIAS
photo = ImageTk.PhotoImage(image)

# ---------- Widgets ----------
label = tk.Label(root, text="MY BIO\n\nNishma Rakshak", font=FONT_HEADER)
label.pack(pady=20)

image_label = tk.Label(root, image=photo)
image_label.image = photo
image_label.pack(pady=10)

descrip = tk.Text(root, wrap="word", font=normal_font, width=100, height=15, bg=root["bg"], bd=0)
descrip.tag_configure("bold", font=bold_font)

table_frame = tk.Frame(root)

# ---------- Buttons ----------
button1 = tk.Button(root, text="Click Me")
button2 = tk.Button(root)
button3 = tk.Button(root)
button4 = tk.Button(root)
button5 = tk.Button(root)
button6 = tk.Button(root)

# Global or class-level dictionary to hold image references
icon_images = {}

# def load_icon(filename, size=(20, 20)):
#     img = Image.open(filename).resize(size, Image.ANTIALIAS)
#     return ImageTk.PhotoImage(img)

def load_icon(filename, size=(10, 10)):
    try:
        image = Image.open(filename)
        image = image.resize(size, Image.Resampling.LANCZOS)  # Use this instead of ANTIALIAS
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image {filename}: {e}")
        return None

# def load_icon(filename):
#     try:
#         image = Image.open(filename)
#         return ImageTk.PhotoImage(image)
#     except Exception as e:
#         print(f"Error loading image {filename}: {e}")
#         return None

# ---------- Helper Functions ----------
def reset_ui():    
    image_label.config(image='')
    descrip.pack_forget()
    table_frame.pack_forget()
    for btn in (button1, button2, button3, button4, button5, button6):
        btn.pack_forget()

def show_buttons(buttons):
    for btn in buttons:
        btn.pack(side="left", padx=10, pady=10)

def say_hello():
    reset_ui()

    label.config(text="Hi...\nI am Nishma N J")
    label.pack(pady=10)

    image_label.config(image=photo)
    image_label.image = photo  # ensure reference is held
    image_label.pack(pady=5)

    descrip.config(state="normal")
    descrip.delete("1.0", tk.END)
    descrip.tag_configure("center", justify="center")
    descrip.insert("end", "This is not just a resume.\nIt's me\nClick below to know more about me", "center")
    descrip.config(state="disabled")
    descrip.pack(pady=5, padx=5, fill="x")

    # # Create a frame for buttons and pack it with some vertical padding
    # button_frame = tk.Frame(root)  # or use your main window variable
    button1.pack(pady=1)

    # Show buttons
    button1.config(text="CAREER", command=career)
    button2.config(text="SKILLS", command=tech_skills)
    button3.config(text="EDUCATION", command=education)
    button4.config(text="SKILLS", command=tech_skills)
    button5.config(text="LinkedIn", command=open_browser)
    button6.config(text="CONTACT", command=contact)

    show_buttons([button1, button2, button3, button4, button5, button6])
    
    # # Pack buttons inside the frame
    # for btn in [button1, button2, button3, button4]:
    #     btn.pack(in_=button_frame, side="left", padx=10)

def tech_skills():
    reset_ui()
    label.config(text="TECHNICAL SKILLS")
    descrip.config(state="normal")
    descrip.delete("1.0", tk.END)

    for widget in table_frame.winfo_children():
        widget.destroy()

    data = [
        ("Key Skills:", "Bare Metal and RTOS Firmware Design and Development."),
        ("Programming:", "C programming on ARM cortex M, Familiar with Python."),
        ("Frameworks and Tools:", "Free RTOS, easyGUI, Touch GFX, Embedded Linux (basics)."),
        ("Interface and Technologies:", "I2C, SPI, UART, ADC, 1 Wire, LCD Display,"),
        ("", "Modbus, MBUS, BLE, JSON, SD Card, USB."),
        ("Tools and Process:", "Git, SonarQube, Azile CI/CD, Automating the process, Mantis."),
        ("Project Management:", "Requirements analysis, Schedule Estimation,"),
        ("", "Training Engineers, design review."),
    ]

    for i, (title, content) in enumerate(data):
        if title:
            tk.Label(table_frame, text=title, font=FONT_BOLD, anchor="w").grid(row=i, column=0, sticky="w", padx=10, pady=2)
        tk.Label(table_frame, text=content, font=FONT_NORMAL, anchor="w", wraplength=500, justify="left").grid(row=i, column=1, sticky="w", padx=10, pady=2)

    table_frame.pack(pady=20, fill="x")
    button1.config(text="BACK", command=say_hello)
    button1.pack(pady=10)

# def education():
#     reset_ui()
#     label.config(text="My educational background....")

#     for widget in table_frame.winfo_children():
#         widget.destroy()

#     data = [
#         ("🎓 BE (2010 - 2014):", "Electronics and Communication", "76%"),
#         ("🎓 M.Tech (2014 - 2016):", "VLSI and Embedded Systems", "83.38%"),
#     ]

#     for i, row in enumerate(data):
#         for j, val in enumerate(row):
#             font = FONT_BOLD if j in (0, 2) else FONT_NORMAL
#             tk.Label(table_frame, text=val, font=font, anchor="w", width=30).grid(row=i, column=j, padx=5, pady=5)

#     table_frame.pack(pady=20)
#     button1.config(text="BACK", command=say_hello)
#     button1.pack(pady=10)

def education():
    reset_ui()
    label.config(text="My educational background....", font=("Arial", 18, "bold"))

    for widget in table_frame.winfo_children():
        widget.destroy()

    data = [
        ("🎓", "BE (2010 - 2014)", "Electronics and Communication", "76%"),
        ("🎓", "M.Tech (2014 - 2016)", "VLSI and Embedded Systems", "83.38%"),
    ]

    headers = ("", "Degree", "Specialization", "Percentage")
    header_fonts = ("Arial", 13, "bold")

    for j, title in enumerate(headers):
        tk.Label(
            table_frame,
            text=title,
            font=header_fonts,
            fg="blue",
            anchor="w",
            # width=25
            justify="left",
            # sticky="w"
        ).grid(row=0, column=j, padx=10, pady=8, sticky="w")

    for i, row in enumerate(data, start=1):
        for j, val in enumerate(row):
            font = FONT_EMOJI if val == "🎓" else (FONT_BOLD if j in (1, 3) else FONT_NORMAL)
            tk.Label(
                table_frame,
                text=val,
                font=font,
                anchor="w",
                # width=25,
                justify="left",
                # sticky="w",
                padx=5
            ).grid(row=i, column=j, padx=10, pady=5, sticky="w")

    for col in range(4):
        table_frame.grid_columnconfigure(col, weight=1)

    table_frame.pack(pady=20)
    button1.config(text="BACK", command=say_hello)
    button1.pack(pady=10)

def career():
    reset_ui()
    label.config(text="My career....")
    button1.config(text="BACK", command=say_hello)
    button1.pack(pady=10)

def open_linkedin():
    webbrowser.open("https://www.linkedin.com/in/nishma-nj/")

    # Add to say_hello
    button4.config(text="LinkedIn", command=open_linkedin)
    button4.pack(side="left", padx=10)

def open_browser():
    webview.create_window('Browser', 'https://www.linkedin.com/posts/nishma-n-j-108b52186_firmware-debugging-embeddedsystems-activity-7215904948088098818-0SBe')
    webview.start()

# def contact():
#     reset_ui()
#     label.config(text="Contact me by....")
    
#     descrip.config(state="normal")
#     descrip.delete("1.0", tk.END)

#     for widget in table_frame.winfo_children():
#         widget.destroy()

#     # Load icons once
#     icon_images["phone"] = load_icon("phone.png")
#     icon_images["email"] = load_icon("email.png")
#     icon_images["location"] = load_icon("location.png")

#     data = [
#         ("Phone:", "9035505792", icon_images["phone"]),
#         ("Email:", "njnishma@gmail.com", icon_images["email"]),
#         ("Location:", "Bangalore, India", icon_images["location"]),
#     ]

#     for i, (title, content, icon) in enumerate(data):
#         if title:
#             tk.Label(table_frame, image=icon).grid(row=i, column=0, padx=5, pady=2)
#             tk.Label(table_frame, text=title, font=FONT_BOLD, anchor="w").grid(row=i, column=1, sticky="w", padx=5)
#         tk.Label(table_frame, text=content, font=FONT_NORMAL, anchor="w", wraplength=500, justify="left").grid(row=i, column=2, sticky="w", padx=5)

#     table_frame.pack(pady=20, fill="x")
#     button1.config(text="BACK", command=say_hello)
#     button1.pack(pady=10)

# def open_email(event):
#     webbrowser.open("mailto:njnishma@gmail.com")

# email_label = tk.Label(table_frame, text="njnishma@gmail.com", font=FONT_NORMAL, anchor="w", fg="blue", cursor="hand2")
# email_label.grid(row=1, column=1, sticky="w", padx=10, pady=2)
# email_label.bind("<Button-1>", open_email)


# #sending emeil in browser
# def contact():
#     reset_ui()
#     label.config(text="Contact me by....")
    
#     descrip.config(state="normal")
#     descrip.delete("1.0", tk.END)

#     for widget in table_frame.winfo_children():
#         widget.destroy()

#     # Load icons once
#     icon_images["phone"] = load_icon("phone.png")
#     icon_images["email"] = load_icon("email.png")
#     icon_images["location"] = load_icon("location.png")

#     data = [
#         ("Phone:", "9035505792", icon_images["phone"]),
#         ("Email:", "njnishma@gmail.com", icon_images["email"]),
#         ("Location:", "Bangalore, India", icon_images["location"]),
#     ]

#     for i, (title, content, icon) in enumerate(data):
#         if title:
#             tk.Label(table_frame, image=icon).grid(row=i, column=0, padx=5, pady=2)
#             tk.Label(table_frame, text=title, font=FONT_BOLD, anchor="w").grid(row=i, column=1, sticky="w", padx=5)
        
#         if title.startswith("Email"):
#             # Make email clickable
#             email_label = tk.Label(table_frame, text=content, font=FONT_NORMAL, anchor="w", fg="blue", cursor="hand2")
#             email_label.grid(row=i, column=2, sticky="w", padx=5)
#             email_label.bind("<Button-1>", lambda e: webbrowser.open(f"mailto:{content}"))
#         else:
#             tk.Label(table_frame, text=content, font=FONT_NORMAL, anchor="w", wraplength=500, justify="left").grid(row=i, column=2, sticky="w", padx=5)

#     table_frame.pack(pady=20, fill="x")
#     button1.config(text="BACK", command=say_hello)
#     button1.pack(pady=10)



def open_email_popup(email):
    popup = tk.Toplevel()
    popup.title("Send Email")
    popup.geometry("400x350")  # Increased height

    tk.Label(popup, text="To:", font=FONT_BOLD).pack(anchor="w", padx=10, pady=5)
    tk.Label(popup, text=email, font=FONT_NORMAL).pack(anchor="w", padx=10)

    tk.Label(popup, text="Subject:", font=FONT_BOLD).pack(anchor="w", padx=10, pady=5)
    subject_entry = tk.Entry(popup, width=50)
    subject_entry.pack(padx=10)

    tk.Label(popup, text="Message:", font=FONT_BOLD).pack(anchor="w", padx=10, pady=5)
    message_text = tk.Text(popup, height=10, width=50)
    message_text.pack(padx=10)

    # send_button = tk.Button(popup, text="Send", command=lambda: send_email_stub(email, subject_entry.get(), message_text.get("1.0", tk.END)))
    
    send_button = tk.Button(popup, text="Send", command=lambda: send_email_real(email, subject_entry.get(), message_text.get("1.0", tk.END)))
    send_button.pack(pady=10)

# def send_email_stub(to, subject, message):
#     # This is just a stub function.
#     # In a real app, you'd hook this to an SMTP or API call.
#     print("Sending email...")
#     print("To:", to)
#     print("Subject:", subject)
#     print("Message:", message.strip())
#     messagebox.showinfo("Email", f"Email to {to} simulated.\n\nSubject: {subject}")

def send_email_real(to, subject, message_body):
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"  # Use Gmail App Password

    msg = MIMEText(message_body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        messagebox.showinfo("Email", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email:\n{e}")

def contact():
    reset_ui()
    label.config(text="Contact me by....")
    
    descrip.config(state="normal")
    descrip.delete("1.0", tk.END)

    for widget in table_frame.winfo_children():
        widget.destroy()

    # Load icons once
    icon_images["phone"] = load_icon("phone.png")
    icon_images["email"] = load_icon("email.png")
    icon_images["location"] = load_icon("location.png")

    data = [
        ("Phone:", "9035505792", icon_images["phone"]),
        ("Email:", "njnishma@gmail.com", icon_images["email"]),
        ("Location:", "Bangalore, India", icon_images["location"]),
    ]

    for i, (title, content, icon) in enumerate(data):
        if title:
            tk.Label(table_frame, image=icon).grid(row=i, column=0, padx=5, pady=2)
            tk.Label(table_frame, text=title, font=FONT_BOLD, anchor="w").grid(row=i, column=1, sticky="w", padx=5)
        
        if title.startswith("Email"):
            email_label = tk.Label(table_frame, text=content, font=FONT_NORMAL, anchor="w", fg="blue", cursor="hand2")
            email_label.grid(row=i, column=2, sticky="w", padx=5)
            email_label.bind("<Button-1>", lambda e, email=content: open_email_popup(email))
        else:
            tk.Label(table_frame, text=content, font=FONT_NORMAL, anchor="w", wraplength=500, justify="left").grid(row=i, column=2, sticky="w", padx=5)

    table_frame.pack(pady=20, fill="x")
    button1.config(text="BACK", command=say_hello)
    button1.pack(pady=10)


# ---------- Start ----------
say_hello()
root.mainloop()
