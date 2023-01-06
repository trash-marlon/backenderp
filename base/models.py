from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class ClassModel(models.Model):
    state = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)


    """
    @classmethod
    def get_default_uc(cls):
        return User.objects.get(username='admin')
    
    @classmethod
    def get_default_um(cls):
        return User.objects.get(username='admin').id
    
    uc = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_uc )
    um = models.IntegerField(blank=True, null=True, default=1)
    """

    uc = models.ForeignKey(User, on_delete=models.CASCADE )
    um = models.IntegerField(blank=True, null=True)
    

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.uc = self.get_default_uc()
    #         self.um = self.get_default_um()
    #     return super(ClassModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

