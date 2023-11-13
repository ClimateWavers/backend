from django.http import JsonResponse
from .models import CustomToken, User
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated


class TokenVerificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the request path
        path = request.path

        # List of endpoints where the middleware should be applied
        unprotected_endpoints = ['/api/v1/backend/register', '/api/v1/backend/login']

        # Check if the request path matches any protected endpoint
        if path not in unprotected_endpoints and 'confirm' not in path and 'verify' not in path:
            # Get access and refresh tokens from the request headers or cookies
            try:
                access_token = request.headers.get('Authorization').split(" ")[1]
                refresh_token = request.COOKIES.get('refresh_token')
            except Exception:
                return JsonResponse({'detail': 'Tokens are missing'})
            # Verify tokens and authenticate the user
            if access_token or refresh_token:
                # Verify tokens
                try:
                    if refresh_token:
                        token = CustomToken.objects.get(refresh_token=refresh_token)
                    #if access token is not provided but refresh token is available
                except Exception as e:
                    token = access_token
                    if verify_access_token(access_token) is None and refresh_token == token.refresh_token:
                        try:
                            decoded_refresh_token = RefreshToken(token.refresh_token)
                            # Verify refresh token
                            decoded_refresh_token.verify()
                            new_access_token = decoded_refresh_token.access_token
                            # Save access token to request to send back to client
                            request.access_token = str(new_access_token)
                            access_token = str(new_access_token)
                        except Exception:
                            # If user token can't be verified because user is logged in with oauth
                            # Provide new access token for user access to this microservice
                            user = User.objects.get(id=token.user_id)
                            new_refresh_token = RefreshToken.for_user(user)
                            token.refresh_token = str(new_refresh_token)
                            new_access_token = new_refresh_token.access_token
                            # Save access token to request to send back to client
                            request.access_token = str(new_access_token)
                            access_token = str(new_access_token)

                    # Verify access token, if available
                    elif verify_access_token(access_token) is None:
                        return JsonResponse({'detail': 'Invalid tokens'}, status=401)
                    # If refresh and access token has been refreshed, verify and store refresh token
                    elif refresh_token and (token != "") and (refresh_token != token.refresh_token):
                        decoded_refresh_token = RefreshToken(refresh_token)
                        # Verify refresh token
                        decoded_refresh_token.verify()
                        token.refresh_token = refresh_token
                        token.save()
                    #Decode access token
                    decoded_acc_token = verify_access_token(access_token)
                    # Get user
                    user_id = decoded_acc_token.payload["user_id"]
                    request.user = User.objects.get(id=user_id)
                    request.user.is_authenticated = True
                    request.user.permissions = [IsAuthenticated]  # Attach IsAuthenticated permission
                    if (not hasattr(request, 'access_token')) or request.access_token is None:
                        request.access_token = access_token

                except Exception as e:
                    print(e)
                    return JsonResponse({'detail': 'Invalid tokens'}, status=401)
            else:
                return JsonResponse({'detail': 'Tokens are missing'}, status=401)
        response = self.get_response(request)
        return response

def verify_access_token(access_token):
    try:
        # Decode the access token and verify its authenticity
        decoded_token = AccessToken(access_token)
        # If the token is valid, it will be decoded without raising an exception
        return decoded_token
    except Exception as e:
        # Handle invalid or expired tokens here
        print("Token verification failed:", e)
        return None
