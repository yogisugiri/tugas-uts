from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Film, Jadwal

# Konfigurasi admin untuk model Film
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('judul_film', 'durasi', 'genre', 'klasifikasi_umur')
    search_fields = ('judul_film', 'genre')

# Konfigurasi admin untuk model Jadwal
@admin.register(Jadwal)
class JadwalAdmin(admin.ModelAdmin):
    list_display = ('film', 'tanggal', 'jam_tayang', 'studio', 'harga_tiket')
    list_filter = ('tanggal', 'studio')
    search_fields = ('film__judul_film', 'studio')

