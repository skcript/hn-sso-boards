import jwt

# https://<YOUR-DOMAIN>.hellonext.co/admin/settings/advanced
# Copy the token from the SSO section
SSO_KEY = "GENERATED_SSO_KEY";

def generate_sso_token(user):
  user_data = {
    'email': user.email,
    'name': user.name,
  }
  
  return jwt.encode(user_data, SSO_KEY, algorithm='HS256')
