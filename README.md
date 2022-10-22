# Homework Django

![Main workflow](https://github.com/hillel-i-python-pro-i-2022-08-26/homework__vlada_kriazh__django_templates/actions/workflows/main-workflow.yml/badge.svg)

***Enter to start and migrate***
> make homework-i-run

***Enter to purge homework related data***
> make homework-i-purge

***Enter to create admin***
> init-dev-i-create-superuser

***Main routes:***
- /
- /users_generator/**num**
- /say_hello/?name=**name**
- /contacts/
- /admin

***Django commands***
- **Creating N contacts:** python manage.py generate_contacts --amount **N**
- **Creating 10 contacts:** python manage.py generate_contacts
- **Deleted 'name':** python manage.py delete_contacts --name '**name**'
- **Deleted all contacts:** python manage.py delete_contacts
