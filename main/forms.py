from django import forms

color = (
    ("1", "Белый"),
    ("2", "Бежевый"),
    ("3", "Имитация льна"),
    ("4", "Шампань"),
    ("5", "Фисташковый"),
)

size = (
    ("1", "35x35"),
    ("2", "40x40"),
)

side = (
    ("1", "односторонняя печать"),
    ("2", "двухсторонняя печать"),
)



class answerForms(forms.Form):
    люблю = forms.CharField()

class orderForms(forms.Form):
    Id =forms.CharField()
    Имя = forms.CharField()
    Email = forms.EmailField()
    телефон = forms.CharField()
    принт = forms.ImageField()
