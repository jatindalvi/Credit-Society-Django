from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name='csadmin'
urlpatterns = [
    # /status

    # nav bar urls
    path('', views.index,name="index"),
    path('members', views.members,name="members"),
    path('fixeddeposits', views.fixeddeposits,name="fixeddeposits"),
    path('loans', views.loansadmin,name="loansadmin"),
    path('change', views.change,name="change"),
    path('message', views.message,name="message"),

    # new create urls
    path('usercreate', login_required(views.UserCreate.as_view()),name='user_create'),
    path('account/create/', login_required(views.AccountCreate.as_view()), name='account_create'),

    # rateof interests url
    path('interests/', login_required(views.InterestsUpdate.as_view()), name='interest_update'),

    # delete user url
    path('<int:id>/delete/',login_required(views.AccountDelete.as_view()),name='User_Delete'),
    path('userdelete', login_required(views.UserDelete),name='user_delete'),

    # individual details update
    path('FDupdate/(?P<pk>)/', login_required(views.FDUpdate.as_view()), name='fd_update'),
    path('LongLoanupdate/(?P<pk>)/', login_required(views.LongLoanUpdate.as_view()), name='longloan_update'),
    path('EmerLoanupdate/(?P<pk>)/', login_required(views.EmerLoanUpdate.as_view()), name='emerloan_update'),
    path('Sharesupdate/(?P<pk>)/', login_required(views.SharesUpdate.as_view()), name='shares _update'),
    # path('actionUrl', views.FDUpdate.as_view(),name='fdrenew'),

    # pdf conversion
    path('tableview',login_required(views.GeneratePdf.as_view()),name="GeneratePdf"),

]
