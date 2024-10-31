from django import forms


class PrimForm(forms.Form):
    num1 = forms.IntegerField(
        label="Enter The Number to get primes before it", min_value=2, max_value=int(1e6)
    )


