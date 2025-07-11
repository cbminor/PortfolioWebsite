# Generated by Django 5.2.1 on 2025-07-03 20:40

import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.forms.models
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('about_text', wagtail.fields.StreamField([('text', 0), ('image', 1), ('image_left', 2), ('image_right', 3)], block_lookup={0: ('wagtail.blocks.RichTextBlock', (), {'features': ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'blockquote']}), 1: ('wagtail.images.blocks.ImageBlock', [], {}), 2: ('wagtail.blocks.StructBlock', [[('image_left', 1), ('text_right', 0)]], {}), 3: ('wagtail.blocks.StructBlock', [[('text_left', 0), ('image_right', 1)]], {})})),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.CharField(blank=True, help_text='A short paragraph introducing the portfolio', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_subtitle',
            field=models.CharField(blank=True, help_text='Add a subtitle to the front page', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_title',
            field=models.CharField(blank=True, help_text='Add a title to the front page', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Introduction Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=models.CharField(blank=True, help_text='Add an intro to the website', max_length=450),
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address')),
                ('from_address', models.EmailField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
                ('thank_you_text', wagtail.fields.RichTextField(blank=True)),
                ('contact_image', models.ForeignKey(blank=True, help_text='Image for contact page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.forms.models.FormMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.TextField(blank=True, help_text='Default value. Comma or new line separated values supported for checkboxes.', verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('display', models.CharField(choices=[('Inline', 'Inline'), ('Block', 'Block')], default='Block', max_length=10)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.contactpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(blank=True, help_text='The display title for the project', max_length=255)),
                ('project_summary', models.CharField(blank=True, help_text='A short summary of the project (About 100 characters)', max_length=255)),
                ('project_link', models.URLField(blank=True)),
                ('project_link_type', models.CharField(blank=True, choices=[('GitHub', 'GitHub'), ('Kaggle', 'Kaggle'), ('Tableau', 'Tableau')], max_length=10)),
                ('blog_link', models.ForeignKey(blank=True, help_text='Choose the related blog page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('project_image', models.ForeignKey(blank=True, help_text='Project Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_list', to='home.portfolio')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.projectcard')),
            ],
            options={
                'verbose_name': 'project_list',
                'verbose_name_plural': 'project_lists',
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
