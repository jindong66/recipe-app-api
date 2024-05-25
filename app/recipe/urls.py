"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter() # 创建一个默认的路由器实例
router.register('recipes', views.RecipeViewSet) # 注册 'recipes' 路由，并将其映射到 RecipeViewSet 视图集

app_name = 'recipe' # 设置应用命名空间为 'recipe'

# 定义 URL 模式
urlpatterns = [
    path('', include(router.urls)), # 包含 router.urls 中定义的所有路由
]
