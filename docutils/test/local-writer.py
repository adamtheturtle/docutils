# $Id$
# Author: Engelbert Gruber <grubert@users.sourceforge.net>
# Copyright: This module is put into the public domain.

"""
mini-writer to test get_writer_class with local writer
"""

from docutils import nodes, writers


class Writer(writers.Writer):

    supported = ('dummy',)
    """Formats this writer supports."""

    output = None
    """Final translated form of `document`."""

    def __init__(self) -> None:
        writers.Writer.__init__(self)
        self.translator_class = Translator

    def translate(self) -> None:
        visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.output = visitor.astext()


class Translator(nodes.NodeVisitor):
    def __init__(self, document) -> None:
        nodes.NodeVisitor.__init__(self, document)
