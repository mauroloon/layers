# ====================
# Datos estaticos
# ====================

DEV_AWS_REGION = us-east-2
LAYER_NAME = google_auth

install-package:
	mkdir package
	pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib -t package

zip-package:
	cd package && zip -r ../function.zip .

clean-package:
	rm -rf package
	rm -f function.zip

deploy-layer:
	aws lambda publish-layer-version --layer-name $(LAYER_NAME) --zip-file fileb://function.zip --compatible-runtimes python3.11 --region $(DEV_AWS_REGION)

update: install-package zip-package deploy-layer clean-package