from rest_framework.viewsets import ModelViewSet
from ..models import Task, TaskStatus, TaskStatusImage
from ..serializers import TaskSerializer, TaskStatusSerializer, TaskStatusImageSerializer
from rest_framework.permissions import IsAuthenticated

class TaskView(ModelViewSet):
    #select * from Task;
    queryset = Task.objects.all() #qual a tabela e a query
    serializer_class = TaskSerializer #qual o serializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        #select * from Task WHERE creator_FK = user.id
        if user.is_authenticated:
            return Task.objects.filter(creator_FK=user.id)
        return Task.objects.none()
    

class TaskStatusView(ModelViewSet):
    queryset = TaskStatus.objects.all() #qual a tabela e a query
    serializer_class = TaskStatusSerializer #qual o serializer

class TaskStatusImageView(ModelViewSet):
    queryset = TaskStatusImage.objects.all() #qual a tabela e a query
    serializer_class = TaskStatusImageSerializer #qual o serializer