## Common Shell Commands


### Django Shell
'''bash
python manage.py shell

'''

### Django Settings


_Accessing global variables/config in 'settings.py'_
'''python

from django.conf import settings

MY_VAR = getatrr(settings,'MY_VAR','default')

_Debug_
'''python
'''

__BASE_DIR__
'''python
'''

### Import of a model

'from <appname>.models import <KlassNAme>'

'''python
 from mita.models import EmailEntry

'''

'''

### Get a singke stored item
'''it only for single stored'''

'''python
EmailEntry.objects.get(id=1)
# EmailEntry.objects.get(email="abc@gmail.com")
'''

### List all stored item of a model
'''python

 EmailEntry.objects.all()
'''

### Filter all stored item of a model
'''python
EmailEntry.objects.filter(email="yaduvanshiamit009@gmail.com")


'''

### Create a new stored item (instance ) of a model
'''python

EmailEntry.objects.create(
    email='hello@abc.com'
)
or 

obj = EmailEntry()
obj.email = 'hello@abc.com'
obj.save()

'''
### Update a new stored item (instance) of a model

'''python
obj = EmailEntry.objects.get(id=1)
obj.name = 'Bhapa'
obj.save()

'''

### Delete a new stored item (instance) of a Model

'''python
obj = EmailEntry.objects.get(id=2)
obj.delete()


'''

