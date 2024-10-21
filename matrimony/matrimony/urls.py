"""
URL configuration for matrimony project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import BasicInforView
from contact.views import ContactView
from family.views import FamilyView
from education.views import EducationView
from django.conf import settings
from django.conf.urls.static import static
from uauthentic.views import (RegisterView,LoginView,ChangePasswordView,
    SendOTPViewEmail,VerifyOTPViewEmail,SendPhoneOTPView,VerifyPhoneOTPView,
    DeleteUserView,InstantDeleteUserView,LogoutView,RegisterDetailView,RegisterListView,PasswordResetRequestView,
    PasswordResetConfirmView)
from user.views import PartnerPreferenceDetailsAPIView,UserModelAPIView,SixPhotoAPIView,IdProofAPIView,DocumentAddressAPIView,CompatibilityMatchAPIView,ReviewSectionAPIView,ProfileCompletesAPIView,HabitsView,HobbiesView,CreateOrderAPIView,VerifyPaymentAPIView
#from userauthentication.views import RegisterView,LoginView,ProfileView,ChangePasswordView,DeleteUserView,VerifyOTPView,SendOTPView,VerifyEmailView,SendVerificationEmailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('basicinfo/',BasicInforView.as_view()),
    path('basicinfo/<int:pk>/',BasicInforView.as_view()),
    path('contactus/',ContactView.as_view()),
    path('contactus/<int:pk>',ContactView.as_view()),
    path('family/',FamilyView.as_view()),
    path('family/<int:pk>',FamilyView.as_view()),
    path('education/',EducationView.as_view()),
    path('education/<int:pk>',EducationView.as_view()),
    path('partner-preferences/', PartnerPreferenceDetailsAPIView.as_view(), name='partner-preferences-list'),
    path('partner-preferences/<int:pk>/', PartnerPreferenceDetailsAPIView.as_view(), name='partner-preferences-detail'),
    path('user-models/', UserModelAPIView.as_view(), name='user-model-list'),
    path('user-models/<int:pk>/', UserModelAPIView.as_view(), name='user-model-detail'),
    path('six-photos/', SixPhotoAPIView.as_view(), name='six-photo-list'),
    path('six-photos/<int:pk>/', SixPhotoAPIView.as_view(), name='six-photo-detail'),
    path('id-proofs/', IdProofAPIView.as_view(), name='id-proof-list'),
    path('id-proofs/<int:pk>/', IdProofAPIView.as_view(), name='id-proof-detail'),
    path('document-addresses/', DocumentAddressAPIView.as_view(), name='document-address-list'),
    path('document-addresses/<int:pk>/', DocumentAddressAPIView.as_view(), name='document-address-detail'),
    path('compatibility-matches/', CompatibilityMatchAPIView.as_view(), name='compatibility-match-list'),
    path('compatibility-matches/<int:pk>/', CompatibilityMatchAPIView.as_view(), name='compatibility-match-detail'),
    path('reviews/', ReviewSectionAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewSectionAPIView.as_view(), name='review-detail'),
    path('profile-completes/', ProfileCompletesAPIView.as_view(), name='profile-completes-list-create'),
    path('profile-completes/<int:pk>/', ProfileCompletesAPIView.as_view(), name='profile-completes-detail'),
    path('habits/', HabitsView.as_view(), name='habits-list'),      
    path('habits/<int:pk>/', HabitsView.as_view(), name='habits-detail'),
    path('hobbies/', HobbiesView.as_view(), name='hobbies-list'),
    path('hobbies/<int:pk>/', HobbiesView.as_view(), name='hobbies-detail'),
    path('payment/',CreateOrderAPIView.as_view(),name='payment'),
    path('verify/',VerifyPaymentAPIView.as_view(),name='verify'),
    path('rigister/',RegisterView.as_view(),name='rigister'),
    path('login/', LoginView.as_view(), name='login'),
    path('changepassword/', ChangePasswordView.as_view(), name='change_password'),
    path('email-send-otp/', SendOTPViewEmail.as_view(), name='send_otp'),
    path('email-verify-otp/', VerifyOTPViewEmail.as_view(), name='verify_otp'),
    path('send-phone-otp/', SendPhoneOTPView.as_view(), name='send_phone_otp'), 
    path('verify-phone-otp/', VerifyPhoneOTPView.as_view(), name='verify_phone_otp'),
    path('delete-user/', DeleteUserView.as_view(), name='delete_user'),
    path('instant-delete-user/', InstantDeleteUserView.as_view(), name='instant_delete_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', RegisterListView.as_view(), name='register-list'),
    path('profile/<int:pk>/', RegisterDetailView.as_view(), name='register-detail'),
    path('passwordreset/',PasswordResetRequestView.as_view(),name="reset password"),
    path('passwordconfirm/',PasswordResetConfirmView.as_view(),name='reset_password_confirmation')
    
]   
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 


