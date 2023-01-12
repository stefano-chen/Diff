class ExamException(Exception):
    pass


class Diff:
    def __init__(self, ratio=1):
        if not isinstance(ratio, int | float):
            raise ExamException("Ratio Type Error")
        if ratio == 0:
            raise ExamException("Ratio cannot be 0")
        self.ratio = ratio
