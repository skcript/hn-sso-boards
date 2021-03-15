require 'jwt'

# https://wantable.hellonext.co/admin/settings/advanced
# Copy the token from the SSO section
SSO_KEY = 'YOUR SSO TOKEN'

def generate_sso_token(email, name)
  user_data = {
    email: email,
    name: name
  }

  JWT.encode(user_data, SSO_KEY, 'HS256')
end
