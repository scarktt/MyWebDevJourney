# Generated by Django 4.1 on 2022-08-24 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0003_remove_animelist_anime_id_remove_animelist_list_id_and_more'),
        ('lists', '0002_list_anime_delete_userlist'),
        ('users', '0004_alter_user_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('watching', 'Watching'), ('paused', 'Paused'), ('finished', 'Finished')], max_length=8)),
                ('score', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('anime_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.anime')),
            ],
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.list')),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['user_id', 'created_at'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='user',
            name='anime',
            field=models.ManyToManyField(related_name='user_id', through='users.UserAnime', to='animes.anime'),
        ),
        migrations.AddField(
            model_name='user',
            name='lists',
            field=models.ManyToManyField(related_name='user_id', through='users.UserList', to='lists.list'),
        ),
        migrations.AddField(
            model_name='userlist',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='useranime',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
