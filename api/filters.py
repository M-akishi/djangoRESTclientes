import django_filters
from .models import Cliente

class ClienteFilter(django_filters.FilterSet):
    edad_min = django_filters.NumberFilter(field_name='Edad', lookup_expr='gte')
    edad_max = django_filters.NumberFilter(field_name='Edad', lookup_expr='lte') 
    satisfaccion = django_filters.ChoiceFilter(field_name='Nivel_de_Satisfaccion', choices=Cliente.NIVEL_SATISFACCION_CHOICES)
    genero = django_filters.ChoiceFilter(choices=Cliente.GENERO_CHOICES, label='Genero')
    activo = django_filters.ChoiceFilter(choices=Cliente.ESTADO_CHOICES, label='Activo')

    class Meta:
        model = Cliente
        fields = ['Edad', 'Nivel_de_Satisfaccion','Genero','Activo']
