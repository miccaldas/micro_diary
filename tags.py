import urwid


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


class Tags(urwid.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            return super(Tags, self).keypress(size, key)
        texto = u"%s.\n\nPress Q to exit." % edit.edit_text
        self.original_widget = urwid.Text(texto, align='center')


edit = urwid.Edit(u"Tags:\n", align='center')
fill = Tags(edit)
loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()

f = open('tags.txt', 'w')
f.write(edit.get_edit_text())
f.close()
