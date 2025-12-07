
class Calculator:
    # Class attribute referenced by the class method.
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # Static method: Takes regular arguments, no access to cls or self.
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Class method: Takes cls as first argument to access class attributes.
        print(f"Calculation type: {cls.calculation_type}")
        return a * b