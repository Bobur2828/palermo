# Generated by Django 5.1.2 on 2025-03-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blog_alter_blogpgheader_options_blogelements_cart_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePGClientsTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=23)),
                ('text_ru', models.CharField(blank=True, max_length=122, null=True)),
                ('text_en', models.CharField(blank=True, max_length=122, null=True)),
            ],
            options={
                'verbose_name': 'ServicePG ClientsTitle',
                'verbose_name_plural': 'ServicePG ClientsTitles',
            },
        ),
    ]
