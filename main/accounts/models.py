from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser): #МОДЕЛЬ ПОЛЬЗОВАТЕОЯ
    """
  
    """

    def __str__(self) -> str:
        return self.username