# Generated by Django 4.2.1 on 2023-07-11 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_comentarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentasAptos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('imagen', models.CharField(max_length=500)),
                ('imagend', models.CharField(max_length=500)),
                ('imagent', models.CharField(max_length=500)),
                ('precio', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='visita',
            name='casa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.ventasaptos'),
        ),
        migrations.DeleteModel(
            name='VentasAp',
        ),
    ]
