from django.contrib import admin

from ExpedienteCO.models import Padre,Paciente,Aplicacionprocedimiento

class PadreNombreFilter(admin.SimpleListFilter):

    def lookups(self, request, model_admin):
        # Seleccionamos las categorías que son principales ordenadas por nombre ascendente
        all_padres = Padre.objects.filter(id_padre=True).order_by("nombre1").all()

        response = list()

        for padre_entity in all_padres:
            response.append((padre_entity.nombre1, padre_entity.apellido1))

        return response

    title = u'Categoría Principal'

    parameter_name = 'main_category'

    def queryset(self, request, queryset):

        if self.value():
            category_id = self.value()
            return queryset.filter(nombre1=str(category_id))

        return queryset


