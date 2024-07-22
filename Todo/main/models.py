from django.db import models

# Create your models here.
class Todo(models.Model):
    task=models.CharField(max_length=255)#add cheytha task store cheyan venditte olla field
    completed=models.BooleanField(default=False)#completed ayitta olla tasksum allathathum separate akkan venditte olla boolean field 

    #date in which the task is created
    created_date=models.DateField(auto_now_add=True)
    #if we update anything in task that date
    modified_date=models.DateField(auto_now=True)

#when we add the task its created as object 'Todoobject' so to change this 
#so to represent the task variable in string form (task name)we re using here "__str__"
    def __str__(self):
        return self.task