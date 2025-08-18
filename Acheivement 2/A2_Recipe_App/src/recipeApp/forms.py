from django import forms

# comment out for now until I know I want to use this
# CHART_CHOICES = (
#   ('#1', 'Bar Chart'),
#   ('#2', 'Pie Chart'),
#   ('#3', 'Line Chart')
# )

# class created for form to be used


class IngredientSearchForm(forms.Form):
    # may need to be redifined later, correctly for recipe_ingredients
    recipe_title = forms.CharField(max_length=120, label="Recipe Lookup")
    # only use this if I want them to appear on the same page - comment out for now
    # chart_type = forms.ChoiceField(choices=CHART_CHOICES)
