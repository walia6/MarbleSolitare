import grid
from numpy import ndarray
from functools import partial
from Tkinter import *
import ttk

buttons_functions = ndarray((9, 9), object)
buttons = ndarray((9, 9), object)
queue = {}

main = grid.GridSystem()
root = Tk()

main.print_grid()

images = {
    "None": PhotoImage(file="~/github/MarbleSolitare/None.gif"),
    "ball": PhotoImage(file="~/github/MarbleSolitare/ball.gif"),
    "border": PhotoImage(file="~/github/MarbleSolitare/border.gif")
}


def update(event, pos):
    print("got event", event)
    titles = {
        "1": "Ready to select ball",
        "0": "Ball selected"
    }
    root.winfo_toplevel().title(titles[str(len(queue))])
    del titles
    if pos == "init":
        for a in range(9):
            for b in range(9):
                buttons[a][b]["image"] = images[str(main.grid[b][a].item_type)]
                #
        return
    if len(queue) == 1:
        queue[1] = pos
        print("running move command x1: " + str(queue[0][0]) + "  y1: "
              + str(queue[0][1]) + "  x2: " + str(queue[1][0]) + "  y2: "
              + str(queue[1][1]))
        print(main.mv((queue[0][1], queue[0][0]), (queue[1][1], queue[1][0])))
        main.print_grid()
        del queue[0], queue[1]

        for a in range(9):
            for b in range(9):
                buttons[a][b]["image"] = images[str(main.grid[b][a].item_type)]
    else:
        queue[0] = pos
    print("updated!")


for a in range(9):
    for b in range(9):
        buttons[a][b] = Label(root, text="", width=45, height=45)
        buttons[a][b].grid(row=a + 1, column=b + 1)
        buttons[a][b].bind("<Button-1>", partial(update, pos=(a, b)))

update("", "init")

root.mainloop()
