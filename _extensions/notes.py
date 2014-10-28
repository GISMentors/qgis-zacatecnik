# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils.parsers.rst import directives

class NoteCmd(directives.admonitions.BaseAdmonition):
    required_arguments = 1
    node_class = nodes.admonition

    def run(self):
        self.options['classes'] = ['notecmd']
        self.arguments[0] = u'Příklad ' + self.arguments[0] + u' z příkazové řádky'
        return super(NoteCmd, self).run()

class NoteGRASS6(directives.admonitions.BaseAdmonition):
    required_arguments = 0
    node_class = nodes.admonition

    def run(self):
        self.options['classes'] = ['notegrass6']
        self.arguments.append(u'Poznámka pro GRASS GIS verze 6')
        return super(NoteGRASS6, self).run()

def setup(builder):
    directives.register_directive('notecmd', NoteCmd)
    directives.register_directive('notegrass6', NoteGRASS6)
