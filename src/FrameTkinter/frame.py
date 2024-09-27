# from tkinter import *
# from tkinter import ctk
from customtkinter import *

from app import App


def run():
    """Initializes the AppFrame object.
    :param _app: The App object to use"""
    # Create the main window
    root = CTk()
    set_appearance_mode("dark")
    root.geometry("800x600")
    root.title("Stundenplan App")

    # Font
    _font = "Liberation Sans"

    # Create a frame
    mainFrame = CTkFrame(root, width=800, height=400)
    mainFrame.pack()

    a = App()

    # Create a label
    CTkLabel(mainFrame, text="H-BRS Kalendergenerator",
             justify="center", font=(_font, 22)).pack(pady=15/2)

    label1 = CTkLabel(mainFrame, text="Bitte wähle deinen Studiengang aus",
                      justify="center", font=(_font, 18))
    label1.pack(pady=15/2)

    allCheckboxes: tuple[CTkCheckBox, dict] = []

    # Create a checkbutton for selecting all
    # erstmal checkbox hidden lassen
    alleBox = CTkCheckBox(mainFrame, text="Alle auswählen", variable=IntVar(
    ), command=lambda: [checkbox.toggle() for checkbox, _ in allCheckboxes])
    alleBox.pack(pady=15/2, anchor="center")

    # Create new checkbuttons
    def _print(*args):
        # Clear previous alle checkbutton
        alleBox.configure(variable=IntVar())
        # Clear previous checkbuttons
        for checkbox, _ in allCheckboxes:
            checkbox.destroy()
        allCheckboxes.clear()

        # Change label text
        if args:
            label1.configure(text="Bitte wähle deine Veranstaltungen aus")

        # Create new checkbuttons
        for i, value in enumerate(a.getVeranstaltungen(args[0])):
            info = value["title"] + " in Raum: " + \
                value["room"] + " bei: " + value["lecturer"]
            checkbox = CTkCheckBox(veranst_frame, text=info, variable=IntVar())
            checkbox.grid(row=i, column=0, columnspan=2, sticky="w")
            allCheckboxes.append((checkbox, value))

        # reset scrollbar to top
        canvas.yview_moveto(0)

    # selected item
    stringvar = StringVar(mainFrame)

    # Create a combobox
    arr = a.getStudiengaenge()
    CTkOptionMenu(mainFrame, variable=stringvar, values=arr,
                  command=_print).pack(pady=15/2, anchor="center")

    # Create a scrollbar
    scrollbar = CTkScrollbar(mainFrame)
    scrollbar.pack(side="right", fill="y")

    # Create a canvas
    canvas = CTkCanvas(
        mainFrame, yscrollcommand=scrollbar.set, width=800, height=380)
    canvas.configure(bg=root.cget("bg"), highlightthickness=0,
                     bd=0, relief="ridge")
    canvas.pack(side="left", fill="both", expand=True)

    # Configure the scrollbar to work with the canvas
    scrollbar.configure(command=canvas.yview)

    # Create a frame inside the canvas to hold the checkbuttons
    veranst_frame = CTkFrame(canvas)
    veranst_frame.configure(bg_color=canvas.cget(
        "bg"), width=canvas.cget("width"), height=canvas.cget("height"))
    veranst_frame.pack(fill="both", expand=True)
    # Add the frame to the canvas
    canvas.create_window((0, 0), window=veranst_frame, anchor="nw")
    # Configure the canvas to scroll with the scrollbar
    canvas.configure(scrollregion=canvas.bbox("all"), bg=canvas.cget(
        "bg"), width=canvas.cget("width"), height=canvas.cget("height"))
    # Bind the update_scroll_region function to the frame resize event
    veranst_frame.bind("<Configure>", lambda event: canvas.configure(
        scrollregion=canvas.bbox("all")))
    veranst_frame.bind(
        "<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))
    veranst_frame.bind(
        "<Button-5>", lambda event: canvas.yview_scroll(1, "units"))

    CTkButton(root, text="Erstelle Ical", command=lambda: a.ical(
        [d for checkbox, d in allCheckboxes if checkbox.get() == 1])).pack(pady=15/2, side="bottom", anchor="center")

    # Run the main loop
    root.mainloop()


if __name__ == "__main__":
    run()
