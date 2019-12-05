env_vars="TWILIO_AUTH_TOKEN TWILIO_SID TWILIO_NUMBER"

for env_var in $env_vars
do
    chosen_value=${!env_var}
    echo "$env_var=\"${chosen_value}\""
done