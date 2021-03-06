# Generated by Django 2.0.1 on 2018-01-30 14:59

from django.db import migrations

nutrient_keys = ['kilojoules','protein','fibre','carbohydrate','fat','sugar','saturatedfat','sodium']

def copy_nutrient_data(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects.
    Ingredient = apps.get_model('ingredients', 'Ingredient')
    for ing in Ingredient.objects.filter(nutrients__isnull=False):
       if ing.nutrients:
          # Have a ing with nutrient data - copy each value and save
          for key in nutrient_keys:
            setattr(
               ing,
               key,
               getattr(ing.nutrients, key)
            ) # Allow any exceptions to fail the migration
          ing.save()

class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_squashed_0008_auto_20180130_1455'),
    ]

    operations = [
        migrations.RunPython(copy_nutrient_data),
    ]
