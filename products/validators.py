from django.core.exceptions import ValidationError


class MinimumValidator:
    def __init__(self, min_value):
        self.min_value = min_value

    def __call__(self, value):
        if value < self.min_value:
            raise ValidationError(
                f'Value must be greater than or equal to {self.min_value}'
            )


class MaximumValidator:
    def __init__(self, max_value):
        self.max_value = max_value

    def __call__(self, value):
        if value > self.max_value:
            raise ValidationError(
                f"Value must be less than or equal to {self.max_value}"
            )
