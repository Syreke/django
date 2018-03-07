from django.db import models
# Create your models here.
class Teacher(models.Model):
	first_name = models.CharField(max_length=200, help_text = "Есімін енгізініз")
	last_name = models.CharField(max_length=200, help_text = "Тегін енгізініз")
	email = models.CharField(max_length=200, help_text = "Почта енгізініз")
	kafedra = models.CharField(max_length=200, help_text = "Кафедра енгізініз")
	date_of_birth = models.DateField(null=True, blank=True)
	
	class Meta:
		ordering = ["last_name", "first_name"]
	
	def get_absolute_url(self):
		return reverse('teacher-detail', args=[str(self.id)])
	
	
	def __str__(self):
		return '{0},{1}'.format(self.last_name,self.first_name)
		
	
class Student(models.Model):
	first_name = models.CharField(max_length=200, help_text = "Есімін енгізініз")
	last_name = models.CharField(max_length=200, help_text = "Тегін енгізініз")
	email = models.CharField(max_length=200, help_text = "Почта енгізініз")
	kafedra = models.CharField(max_length=200, help_text = "Кафедра енгізініз")
	date_of_birth = models.DateField(null=True, blank=True)
	
	class Meta:
		ordering = ["last_name", "first_name"]
	
	def get_absolute_url(self):
		return reverse('student-detail', args=[str(self.id)])
	
	
	def __str__(self):
		return '{0},{1}'.format(self.last_name,self.first_name)
		
	
	