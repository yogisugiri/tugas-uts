from django.db import models

# Create your models here.
from django.db import models

class Film(models.Model):
    id_film = models.AutoField(primary_key=True)
    judul_film = models.CharField(max_length=100)
    durasi = models.PositiveIntegerField(help_text="Durasi film dalam menit")
    genre = models.CharField(max_length=50)
    klasifikasi_umur = models.CharField(max_length=10)

    def __str__(self):
        return self.judul_film


class Jadwal(models.Model):
    id_jadwal = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='jadwal')
    tanggal = models.DateField()
    jam_tayang = models.TimeField()
    studio = models.CharField(max_length=20)
    harga_tiket = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return f"{self.film.judul_film} - {self.tanggal} {self.jam_tayang}"
