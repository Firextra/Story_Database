# Generated by Django 5.1.6 on 2025-02-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Story_Database', '0007_alter_profile_image_alter_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterdatabase',
            name='Tags',
            field=models.ManyToManyField(blank=True, to='Story_Database.characterdatabase'),
        ),
        migrations.AddField(
            model_name='universedatabase',
            name='UniverseAuthor',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
