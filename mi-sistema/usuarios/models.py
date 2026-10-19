from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=20, unique=True)
    codigo_usuario = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Generar código automático: 1ra letra nombre + 1ra letra apellido + 3 últimos dígitos de la cédula
        if not self.codigo_usuario:
            p_nombre = self.nombre[0].upper() if self.nombre else ""
            p_apellido = self.apellido[0].upper() if self.apellido else ""
            ult_cedula = self.cedula[-3:] if len(self.cedula) >= 3 else self.cedula
            self.codigo_usuario = f"{p_nombre}{p_apellido}{ult_cedula}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.codigo_usuario})"