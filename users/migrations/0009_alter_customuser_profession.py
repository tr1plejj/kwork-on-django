# Generated by Django 4.2 on 2024-04-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_exp_customuser_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profession',
            field=models.CharField(blank=True, choices=[('python', 'Python-разработчик'), ('java', 'Java-разработчик'), ('sql', 'Архитектор баз данных'), ('analytic', 'Аналитик'), ('php', 'PHP-разработчик'), ('c', 'C-разработчик')], default='', verbose_name='profession'),
        ),
    ]
