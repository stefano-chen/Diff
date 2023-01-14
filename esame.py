class ExamException(Exception):
    pass


class Diff:
    def __init__(self, ratio=1):
        if not isinstance(ratio, int | float):
            raise ExamException("Ratio Type Error")
        if ratio == 0:
            raise ExamException("Ratio cannot be 0")
        self.ratio = ratio

    def compute(self, data):
        if not isinstance(data, list):
            raise ExamException("data must be a list")
        if not all(isinstance(item, int | float) for item in data):
            raise ExamException("Not numeric values in data")
        if len(data) < 2:
            raise ExamException("Insufficient number of data")

        result = []
        for i, item in enumerate(data[0:-1]):
            result.append((data[i + 1] - item)/self.ratio)
        return result

