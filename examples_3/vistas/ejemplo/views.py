from typing import Any
from django.http import HttpResponse

from django.views.generic import TemplateView

def ejemplo(request):
    print(request.GET)
    return HttpResponse(
        f"""
            <html>
                <body>
                    <b>hola!</b>
                    <p>mi primer parrafo</p>
                    <a href="google.com">Google</a>
                    <p>{request.GET.get('nombre')}</p>
                </body>
            </html>
        """)


class Vista(TemplateView):
    template_name = 'vista.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get('nombre')
        return context
