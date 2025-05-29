# Remove PHP-specific configurations and replace them with Python equivalents

deffile=01rbczpremiumapi.yaml

rm -rf rbczpremiumapi docs test README.md

# First time installation: npm install @openapitools/openapi-generator-cli -g

npx openapi-generator-cli generate -i ${deffile} -g python --git-user-id VitexSoftware --git-repo-id python-vitexsoftware-rbczpremiumapi -c .openapi-generator/config.yaml

# Remove unnecessary PHP-specific modifications
sed -i 's/$xIBMClientId,//' rbczpremiumapi/PremiumAPI/*
sed -i '/@param  string $xIBMClientId/d' rbczpremiumapi/PremiumAPI/*

sed -i 's/$pSUIPAddress = None,//' rbczpremiumapi/PremiumAPI/*
sed -i 's/ $pSUIPAddress,//' rbczpremiumapi/PremiumAPI/*

sed -i '/@param  string $pSUIPAddress IP address/d' rbczpremiumapi/PremiumAPI/*

sed -i '/xIBMClientId_example/d' docs/* README.md
sed -i '/pSUIPAddress_example/d' docs/* README.md

sed -i 's/$xIBMClientId,//' docs/* README.md
sed -i 's/$pSUIPAddress,//' docs/* README.md

sed -i '/IBMClientId/d' docs/*
sed -i '/SUIPAddress/d' docs/*

