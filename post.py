import urwid


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            return super(QuestionBox, self).keypress(size, key)
        texto = u"%s.\n\nPress Q to exit." % edit.edit_text
        self.original_widget = urwid.Text(texto, align='center')


edit = urwid.Edit(u"Say what you come to say\n", align='center')
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()

f = open('post.txt', 'w')
f.write(edit.get_edit_text())
f.close()
