import jwt

# https://<YOUR-DOMAIN>.hellonext.co/admin/settings/advanced
# Copy the token from the SSO section
SSO_KEY = "GENERATED_SSO_KEY";

def generate_sso_token(user):
  user_data = {
    'email': user.email,
    'name': user.name
    # if you'd like to add the person to your team, pass this option
#     'add_to_team': True
  }
  
  return jwt.encode(user_data, SSO_KEY, algorithm='HS256')
