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

class pillowForms(forms.Form):
    Цвет = forms.ChoiceField(required = False, choices = color)
    Размер = forms.ChoiceField(choices = size)
    Формат = forms.ChoiceField(choices = side)
    #Принт = forms.ImageField()

class answerForms (forms.Form):
    ответ = forms.CharField()
