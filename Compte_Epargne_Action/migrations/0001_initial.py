# Generated by Django 2.2.3 on 2019-07-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_quantity', models.IntegerField()),
                ('title_value', models.FloatField()),
                ('aquisition_date', models.DateField()),
                ('time_stamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioTitle',
            fields=[
                ('portolio_id', models.AutoField(default=None, primary_key=True, serialize=False, unique=True)),
                ('portfolio_label', models.CharField(choices=[('p1', 'A'), ('p2', 'B'), ('p3', 'C'), ('p4', 'D'), ('p5', 'E')], default=None, max_length=2)),
            ],
        ),
    ]
