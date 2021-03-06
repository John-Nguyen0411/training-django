# Generated by Django 3.2 on 2022-03-22 08:55

import cart.enums
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0004_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.CharField(choices=[(cart.enums.CsvLogType['INSERT'], 'Insert Only'), (cart.enums.CsvLogType['UPSERT'], 'Insert and Update'), (cart.enums.CsvLogType['EXPORT'], 'Export')], max_length=100)),
                ('file_path', models.CharField(max_length=1000)),
                ('file_size', models.FloatField(null=True)),
                ('total_records', models.IntegerField(null=True)),
                ('success', models.IntegerField(null=True)),
                ('fails', models.IntegerField(null=True)),
                ('errors', models.JSONField(blank=True, null=True)),
                ('status', models.CharField(choices=[(cart.enums.CsvLogStatus['NEW'], 'New'), (cart.enums.CsvLogStatus['IN_PROGRESS'], 'In-progress'), (cart.enums.CsvLogStatus['DONE'], 'Done')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
