# pip freeze > requirements.txt

from tkinter import ttk
import tkinter as tk


bot_output = None
user_input = None

def print_hi(name):
    global bot_output
    global user_input

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    root = tk.Tk()
    root.geometry("500x300")
    user_input = tk.Entry(root)
    user_input.pack()

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()

    clear_button = tk.Button(root, text="Clear", command=clear_message)
    clear_button.pack()

    vbg = '#FAE5D3'
    vfg = '#000'
    bot_output = tk.Text(root)
    scr = ttk.Scrollbar(root, orient=tk.VERTICAL, command=bot_output.yview)
    bot_output.config(yscrollcommand=scr.set, font=('Arial', 8, 'bold', 'italic'), bg=vbg, fg=vfg)
    scr.pack(side=tk.RIGHT, fill=tk.Y)
    bot_output.pack()

    root.mainloop()


def send_message():
    user_message = user_input.get()
    bot_output.insert(tk.END, "Voce: " + user_message + "\n")
    bot_output.insert(tk.END, "Bot: Ola tudo bem ?\n\n")


def clear_message():
    bot_output.config(state='normal')
    bot_output.delete('1.0', tk.END)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
