from numpy import ndarray


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class GridSystem:

    class NewItem:

        def __init__(self, parent, y, x, item_type="ball"):
            parent.grid[y][x] = self
            self.x, self.y, self.item_type = x, y, item_type

        def jump(self, parent, other):  # somehow works
            if self.item_type == "ball" and other.item_type == "ball" and\
             (abs(self.x - other.x) == 1) ^ (abs(self.y - other.y) == 1):
                if abs(self.x - other.x) == 1:
                    if parent.grid[parent.grid[
                            self.x - 2 * (self.x - other.x)]
                            [self.y].x][parent.grid[self.x -
                                        2 * (self.x - other.x)]
                                        [self.y].y].item_type is None:
                        self.item_type, other.item_type = None, None
                        parent.grid[parent.grid[
                            self.x - 2 * (self.x - other.x)]
                            [self.y].x][parent.grid[self.x -
                                        2 * (self.x - other.x)]
                                        [self.y].y].item_type = "ball"
                        return True
                elif abs(self.y - other.y) == 1:
                    if parent.grid[parent.grid[
                            self.x][self.y - 2 * (self.y - other.y)].x][
                            parent.grid[self.x][self.y - 2 * (self.y -
                                                other.y)].y].item_type is None:
                        self.item_type, other.item_type = None, None
                        parent.grid[parent.grid[
                            self.x][self.y - 2 * (self.y - other.y)].x][
                            parent.grid[self.x][self.y - 2 * (self.y -
                                                other.y)].y].item_type = "ball"
                        return True
            return False

    def __init__(self, args={}, y=9, x=9):
        self.args = args
        self.args['y'], self.args['x'] = y, x
        self.grid = ndarray((self.args['x'], self.args['y']), object)

        # ----------default grid configuration----------

        self.default = [
            ["border", "border", "border", "border", "border", "border",
                "border", "border", "border"],
            ["border", "border", "border",  "ball", "ball", "ball",
                "border", "border", "border"],
            ["border", "border", "ball", "ball", "ball", "ball",
                "ball", "border", "border"],
            ["border", "ball", "ball", "ball", "ball", "ball",
                "ball", "ball", "border"],
            ["border",  "ball", "ball", "ball", None, "ball",
                "ball", "ball", "border"],
            ["border", "ball", "ball", "ball", "ball", "ball",
                "ball", "ball", "border"],
            ["border", "border",  "ball", "ball", "ball", "ball",
                "ball", "border", "border"],
            ["border", "border", "border", "ball", "ball", "ball",
                "border", "border", "border"],
            ["border", "border", "border", "border", "border", "border",
                "border", "border", "border"]
        ]

        # ----------marble solitare iniation below----------

        for a in range(9):
            for b in range(9):
                self.NewItem(self, a, b, self.default[b][a])

    def mv(self, _from, over):  # more userfriendly jump function
        return self.grid[_from[0]][_from[1]].jump(self,
                                                  self.grid[over[0]][over[1]])

    def print_grid(self, fill="type", padding=1):
        colors = {
            "border": bcolors.BOLD,
            "ball": bcolors.OKGREEN,
            "None": bcolors.FAIL
        }
        if fill == "type":
            _to_return = ndarray((len(self.grid[0]), len(self.grid)), object)
            for a in range(len(self.grid)):
                for b in range(len(self.grid[0])):
                    if self.grid[a][b]:
                        _to_return[b][a] = self.grid[a][b].item_type
                    else:
                        _to_return[b][a] = "None"
            for a in range(len(_to_return)):
                temp = ""
                for b in range(len(_to_return[0])):
                    temp += colors[str(_to_return[a][b])] +\
                        str(_to_return[a][b]).ljust(10) + bcolors.ENDC
                print(temp)
                for _ in range(padding):
                    print("")
                del temp
        del _to_return
