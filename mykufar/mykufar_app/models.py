from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#


# #
# # class Basket(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #
# # class BasketProduct(models.Model):
# #     basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     quantity = models.PositiveIntegerField(default=1)
# #
# # class UserProduct(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #
# #     def __str__(self):
# #         return f"{self.user.username} - {self.product.name}"
#
# # class Order(models.Model):
# #     email = models.EmailField()
#
# # class Contact(models.Model):
# #     name = models.CharField(max_length=30)
# #     email = models.EmailField(max_length=50)
# #
# #     def __str__(self):
# #         return self.name
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
#     photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
#     info = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.user.username
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)  # Создаем профиль пользователя при создании нового пользователя
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()