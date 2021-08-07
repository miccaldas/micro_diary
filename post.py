"""No comments on a subject that was new"""
import urwid


def exit_on_q(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()


class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != "enter":
            return super(QuestionBox, self).keypress(size, key)
        texto = u"%s.\n\nPress Q to exit." % edit.edit_text
        self.original_widget = urwid.Text(texto, align="center")


palette = [
    ("banner", "white", "#ff6f69"),
    ("streak", "white", "light red"),
    ("bg", "white", "#ff6f69"),
]

edit = urwid.Edit(("banner", u"   DEITA CÀ PRA FORA!  \n"), align="center")
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(fill, "bg")
loop.run()

f = open("post.txt", "w")
f.write(edit.get_edit_text())
f.close()
