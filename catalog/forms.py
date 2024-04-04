from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    unacceptable_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                          'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        if cleaned_name.lower() in self.unacceptable_words:
            raise forms.ValidationError('ОШИБКА! Использовано недопустимое слово в названии!\n'
                                        'Измените название, оно не должно содержать следующие слова:\n'
                                        f'{', '.join(self.unacceptable_words)}')
        return cleaned_name

    def clean_description(self):

        cleaned_data = self.cleaned_data['description']
        if cleaned_data.lower() in self.unacceptable_words:
            raise forms.ValidationError('ОШИБКА! Использовано недопустимое слово в описании!\n'
                                        'Измените описание, оно не должно содержать следующие слова:\n'
                                        f'{', '.join(self.unacceptable_words)}')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
