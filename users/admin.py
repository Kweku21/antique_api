from django.contrib import admin
from .models import UserBidConfig, UserAutoBidProduct

admin.site.register([UserAutoBidProduct, UserBidConfig])
