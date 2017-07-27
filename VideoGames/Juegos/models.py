from django.db import models

# Create your models here.
class creator(models.Model):
	generes=(
			('F','Female'),
			('M','Male'),
		)
    name=models.CharField(max_lenght=25,help_text='Nombre del creador ')
	birthday=models.DateField(help_text='Fecha de nacimiento')
	genere=models.Charfield(max_lenght=1, help_text='Coloque el sexo del creador' choices=generes)

class company(models.Model):
	name=models.Charfield(max_lenght=30,help_text='Compañia Desarrolladora')

	
class games(models.Model):
    """
    almacena los juegos mediante el equipo de
    administracion
    """
    title=models.CharField(max_lenght=30, help_text='Titulo del videojuego ')
    creatores=models.ForeignKey(creator,help_text='Nombre del o los creadores ')
    synopsis=models.TextField(max_lenght=300, help_text='Historia del Videojuego ')
    pubdate=models.DateTimeField(help_text='Fecha y hora de la puclicacion del videojuego ')
    clasification=models.DecimalField(max_lenght=5, help_text='Clasificacion del videojuego ')
    genere=models.CharField(max_lenght=50, help_text='Genero del videojuego ')
    console=models.CharField(max_lenght=50, help_text='Plataforma de videojuego ')


class review(models.Model):
    review=models.IntegerField(max_lenght=100,help_text='Opiniones ')
	game=models.ForeignKey(games,help_text='Selecione el juego que desea hacer la sinopsis')
	