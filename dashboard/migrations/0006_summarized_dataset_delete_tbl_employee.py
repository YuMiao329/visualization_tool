# Generated by Django 4.0.4 on 2022-06-06 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_exprience_tbl_employee_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summarized_Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_female', models.IntegerField()),
                ('number_male', models.IntegerField()),
                ('number_total', models.IntegerField()),
                ('name_dataset', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='tbl_Employee',
        ),
    ]
