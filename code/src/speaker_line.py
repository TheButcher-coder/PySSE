from . import Line


class speaker_line(Line.Line):
    """
    Class for a speaker line, which is a line with a source at one end.
    It inherits from the Line class and adds a source point.
    """

    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.amp = 1000  # Amplitude of the source

    def get_p(self, t):
        """
        Returns the value of the source at time t.
        The source is a delta function.
        """
        return self.amp if t == 0 else 0

    def get_source(self):
        return self.source_x, self.source_y

    def set_source(self, source_x, source_y):
        self.source_x = source_x
        self.source_y = source_y