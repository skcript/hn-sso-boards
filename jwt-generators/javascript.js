// make sure you install,
// npm install --save jsonwebtoken

// https://<YOUR-DOMAIN>.hellonext.co/admin/settings/advanced
// Copy the token from the SSO section

var jwt = require("jsonwebtoken");

const SSO_KEY = "GENERATED_SSO_KEY";

function generateJWTToken(user) {
  var userData = {
    email: user.email,
    name: user.name,
  };
  return jwt.sign(userData, SSO_KEY, { algorithm: "HS256" });
}
