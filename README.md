# drf_ecommerce

Учебный проект (DRF by Илья Перминов)

### Ход работы:
1. Добавили приложения accounts, profiles, sellers, shop, common
2. Переопределили get_queryset, добавили get_or_none и создали абстрактную модель BaseModel
3. Переопределили delete для поддержки мягкого и жесткого удаления и создали абстрактную модель IsDeletedModel
4. Создадим модель юзера на основе абстрактной модели AbstractBaseUser и IsDeletedModel
