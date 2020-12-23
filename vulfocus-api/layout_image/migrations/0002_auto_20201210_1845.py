# Generated by Django 2.2.10 on 2020-12-10 18:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('layout_image', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layoutservice',
            name='exposed_port',
        ),
        migrations.AddField(
            model_name='layout',
            name='layout_desc',
            field=models.TextField(null=True, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='layout',
            name='raw_content',
            field=models.TextField(default='', verbose_name='原json内容'),
        ),
        migrations.AddField(
            model_name='layoutdata',
            name='file_path',
            field=models.TextField(default='', verbose_name='启动目录'),
        ),
        migrations.AddField(
            model_name='layoutservice',
            name='service_name',
            field=models.TextField(default='', verbose_name='服务环境名称'),
        ),
        migrations.AlterField(
            model_name='layout',
            name='layout_id',
            field=models.UUIDField(default=uuid.UUID('e92ded99-d4ae-47f1-9dce-02bed6064a55'), editable=False, primary_key=True, serialize=False, verbose_name='编排UUID'),
        ),
        migrations.AlterField(
            model_name='layoutdata',
            name='layout_user_id',
            field=models.UUIDField(default=uuid.UUID('57a01a3d-a7e6-49c8-881a-c92a1dbfd7af'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservice',
            name='image_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dockerapi.ImageInfo', verbose_name='镜像ID'),
        ),
        migrations.AlterField(
            model_name='layoutservice',
            name='service_id',
            field=models.UUIDField(default=uuid.UUID('7d1ccae2-3b00-465f-bdc6-e6a323e70efa'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicecontainer',
            name='service_container_id',
            field=models.UUIDField(default=uuid.UUID('1df7e992-665e-401e-a9dd-ab9241c97666'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicenetwork',
            name='layout_service_network_id',
            field=models.UUIDField(default=uuid.UUID('647cab36-7179-4268-856c-37350f7f0899'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
