class texteditor:
    def __init__(self):
        self.document = " "
        self.undo_stack = []
        self.redo_stack = []

    def make_changes(self, change):
        self.undo_stack.append(self.document)
        self.document += change
        self.redo_stack.clear()
        print("\nchanges made ")
        self.display_state()

change = input("enter the txt")
t =texteditor()
t.make_changes(change)

