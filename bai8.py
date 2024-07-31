import tkinter as tk
from tkinter import filedialog, messagebox, font, colorchooser

# Hàm để mở tệp
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

# Hàm để lưu tệp
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

# Hàm để thoát khỏi ứng dụng
def exit_app():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.quit()

# Hàm để cắt văn bản
def cut_text():
    text_area.event_generate("<<Cut>>")

# Hàm để sao chép văn bản
def copy_text():
    text_area.event_generate("<<Copy>>")

# Hàm để dán văn bản
def paste_text():
    text_area.event_generate("<<Paste>>")

# Hàm để hoàn tác văn bản
def undo_text():
    text_area.event_generate("<<Undo>>")

# Hàm để làm lại văn bản
def redo_text():
    text_area.event_generate("<<Redo>>")

# Hàm để chọn tất cả văn bản
def select_all():
    text_area.tag_add("sel", "1.0", "end")

# Hàm để thay đổi phông chữ
def change_font():
    font_choice = font.askfont(root)
    if font_choice:
        text_area.config(font=(font_choice["family"], font_choice["size"], font_choice["weight"]))

# Hàm để thay đổi màu chữ
def change_font_color():
    color = colorchooser.askcolor(title="Choose text color")
    if color:
        text_area.config(fg=color[1])

# Hàm để hiển thị thông tin về ứng dụng
def about_app():
    messagebox.showinfo("About Simple Notepad", "This is a simple Notepad application built with Tkinter.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Simple Notepad")

# Tạo vùng văn bản
text_area = tk.Text(root, wrap='word', undo=True)
text_area.pack(expand='yes', fill='both')

# Tạo thanh menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Tạo menu Tệp
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Tạo menu Chỉnh sửa
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo_text)
edit_menu.add_command(label="Redo", command=redo_text)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)

# Tạo menu Định dạng
format_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Font", command=change_font)
format_menu.add_command(label="Font Color", command=change_font_color)

# Tạo menu Trợ giúp
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_app)

# Chạy ứng dụng
root.mainloop()
