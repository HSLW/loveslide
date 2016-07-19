from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class FacebookLogin(SocialLoginView):
    """
    /rest-auth/facebook/ (POST)

        access_token
        code
    """
    adapter_class = FacebookOAuth2Adapter

