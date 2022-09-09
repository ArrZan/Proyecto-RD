from datetime import datetime

from django import forms

from .models import Reserva, ReservaTipoDet


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

        widgets = {
            'horaIngreso': forms.TimeInput(format=('%H:%M:%S'),
                                           attrs={'class': 'form-control', 'placeholder': 'Seleccione una hora',
                                                  'type': 'time'}),
            'diaIngreso': forms.DateInput(format=('%d/%m/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha',
                                                 'type': 'date'})
        }

# class ReservaTipoDetForm(forms.ModelForm):
#     class Meta:
#         model = ReservaTipoDet
#         fields = '__all__'

