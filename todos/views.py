from django.http import HttpResponse, JsonResponse

from .models import Todo
from .serializers import TodoSerializer


def index(request):
    """
    List all todos, or create a new todo.
    """
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)
