class Division:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator
    @staticmethod
    def null(div, den):
        try:
            return (div / den)
        except:
            return (f"В нашей вселенной делить на 0 могут только Господь Бог и Вы")
div = Division(123, 32)
print(Division.null(1123, 56))
print(Division.null(132, 0.654))
print(div.null(235, 0))