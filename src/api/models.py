# pyright: reportMissingTypeArgument=none, reportUnknownMemberType=none, reportUnknownVariableType=none, reportMissingTypeStubs=none

from django.db import models
from pgvector.django import VectorField


class Theme(models.Model):
    id: models.SmallIntegerField = models.SmallIntegerField(primary_key=True)

    name: models.CharField = models.CharField(max_length=100)


class Status(models.Model):
    id: models.SmallIntegerField = models.SmallIntegerField(primary_key=True)

    name: models.CharField = models.CharField(max_length=256)


class Law(models.Model):
    publish_date: models.DateField = models.DateField()

    name: models.CharField = models.CharField(max_length=256)

    number: models.IntegerField = models.IntegerField()

    id_status: models.ForeignKey = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name='law'
    )


class Article(models.Model):
    article: models.TextField = models.TextField()

    chunk: VectorField = VectorField(dimensions=3000)

    last_change: models.DateField = models.DateField()

    id_law: models.ForeignKey = models.ForeignKey(
        Law, on_delete=models.CASCADE, related_name='article'
    )

    id_theme: models.ForeignKey = models.ForeignKey(
        Theme, on_delete=models.CASCADE, related_name='article'
    )
    id_status: models.ForeignKey = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name='article'
    )


class Paragraph(models.Model):
    article: models.TextField = models.TextField()

    chunk: VectorField = VectorField(dimensions=3000)

    paragraph_number: models.IntegerField = models.IntegerField()

    id_article: models.ForeignKey = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='paragraph', primary_key=True
    )
