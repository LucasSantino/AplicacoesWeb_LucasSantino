from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'/api/directors',DirectorView)
router.register(r'/api/movies',MovieView)
router.register(r'/api/plans',PlanView)
router.register(r'/api/user-plans',UserPlanView)
router.register(r'/api/favorites',FavoriteMovieView)

urlpatterns = router.urls