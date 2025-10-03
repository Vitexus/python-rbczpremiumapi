# Generate Python RBC Premium API client library

deffile=01rbczpremiumapi.yaml

echo "🧹 Cleaning previous generation..."
rm -rf rbczpremiumapi docs test README.md

echo "🏗️  Generating Python library from OpenAPI spec..."
# First time installation: npm install @openapitools/openapi-generator-cli -g
npx openapi-generator-cli generate -i ${deffile} -g python --git-user-id Vitexus --git-repo-id python-rbczpremiumapi -c .openapi-generator/config.yaml

echo "✅ Library generation completed!"

# Note: Removed PHP-specific sed commands that were corrupting Python code
# The templates now handle proper Python imports and structure

