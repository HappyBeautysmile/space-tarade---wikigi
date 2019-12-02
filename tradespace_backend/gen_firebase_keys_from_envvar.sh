env_vars="type project_id private_key_id private_key client_email client_id auth_uri token_uri auth_provider_x509_cert_url client_x509_cert_url"

echo "{"
for env_var in $env_vars
do
    chosen_value=${!env_var}
    echo "\"$env_var\": \"${chosen_value}\","
done
echo "}"