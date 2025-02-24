from tkinter import *
import functions as fn

# Starting
root = Tk()
root.title('Image Transfer')
root.geometry("300x250")
root.resizable(False, False)

# UI Elements
Label(root, text="Image Transfer", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

Label(root, text="From:").grid(row=1, column=0, sticky=W, padx=10, pady=5)
Label(root, text="To:").grid(row=2, column=0, sticky=W, padx=10, pady=5)

# Labels
src_label = Label(root, text="No folder selected", fg="gray", width=20, anchor=W, wraplength=150)
dest_label = Label(root, text="No folder selected", fg="gray", width=20, anchor=W, wraplength=150)
status_label = Label(root, text="Status: Waiting...", font=("Arial", 10, "italic"), fg="blue", width=30, anchor=CENTER, wraplength=250)

src_label.grid(row=1, column=1, sticky=W, padx=10)
dest_label.grid(row=2, column=1, sticky=W, padx=10)
status_label.grid(row=4, column=0, columnspan=3, pady=10)

# Buttons
Button(root, text="Browse", command=lambda: [fn.browseFolder1(src_label), fn.srcLabel(src_label)]).grid(row=1, column=2, padx=10)
Button(root, text="Browse", command=lambda: [fn.browseFolder2(dest_label), fn.destLabel(dest_label)]).grid(row=2, column=2, padx=10)
Button(root, text="Start Transfer", font=("Arial", 10, "bold"), bg="green", fg="white", command=lambda: fn.execute(status_label)).grid(row=3, column=0, columnspan=3, pady=15)

root.mainloop()
