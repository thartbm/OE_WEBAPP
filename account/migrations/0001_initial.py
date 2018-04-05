# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import account.validator
import uuid
import account.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(max_length=150, validators=[account.validator.UnicodeUsernameValidator], unique=True, verbose_name='username', help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', error_messages={'unique': 'A user with that username already exists.'})),
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('email', models.EmailField(blank=True, unique=True, verbose_name='email address', null=True, max_length=254)),
                ('is_participant', models.BooleanField(default=False)),
                ('is_researcher', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('home_directory', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('age', models.IntegerField(blank=True, choices=[(8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99), (100, 100), (101, 101), (102, 102), (103, 103), (104, 104), (105, 105), (106, 106), (107, 107), (108, 108), (109, 109), (110, 110), (111, 111), (112, 112), (113, 113), (114, 114), (115, 115), (116, 116), (117, 117), (118, 118), (119, 119), (120, 120), (121, 121), (122, 122), (123, 123), (124, 124)], null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('education', models.CharField(blank=True, choices=[('did not complete highschool', 'Did not complete Highschool'), ('highschool/GED', 'Highschool/GED'), ('some college', 'Some College'), ("bachelor's degree", "Bachelor's Degree"), ("master's degree", "Master's Degree"), ('advanced or Ph.D', 'Advanced Graduate Work or Ph.D')], max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True)),
                ('race', models.CharField(blank=True, choices=[('aboriginal indian', 'Aboriginal Indian'), ('asian', 'Asian'), ('black or african american', 'Black or African American'), ('white/caucasian', 'White/Caucasian'), ('hispanic or latino', 'Hispanic or Latino')], max_length=25, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
