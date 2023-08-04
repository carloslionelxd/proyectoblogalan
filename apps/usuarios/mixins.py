from django.contrib.auth.mixins import UserPassesTestMixin


class EsColaboradorMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.es_colaborador or user.es_miembro or user.is_superuser
    

