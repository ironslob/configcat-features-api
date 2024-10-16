# configcat-features-api

A trivial API to return ConfigCat feature flag results

# Run it

`CONFIGCAT_SDK_KEY="configcat-sdk-1/..." poetry run fastapi dev`

# Query a feature flag

```
➜  configcat-features-api git:(main) ✗ curl "http://localhost:8000/?feature_flag=testing&default=false" 2> /dev/null | jq 

{
  "testing": false
}
➜  configcat-features-api git:(main) ✗ curl "http://localhost:8000/?feature_flag=testing&default=false&user_identifier=1&user_email=example@example.com" 2> /dev/null | jq

{
  "testing": true
}
➜  configcat-features-api git:(main) ✗

```
