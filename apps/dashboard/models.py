from django.contrib.gis.db import models


class Region(models.Model):
    name = models.CharField(max_length=50)
    cad_prefix = models.IntegerField()
    geometry = models.GeometryField(srid=4326)

    class Meta:
        db_table = "regions"
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return "%s - %d" % (self.name, self.cad_prefix)


class District(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey("dashboard.Region", on_delete=models.CASCADE)
    cad_prefix = models.IntegerField()
    geometry = models.GeometryField(srid=4326)

    class Meta:
        db_table = "districts"
        verbose_name = "District"
        verbose_name_plural = "Districts"

    def __str__(self):
        return "%s - %s" % (self.name, self.region)
