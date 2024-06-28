# ====================
# Datos estaticos
# ====================

DEV_AWS_REGION = us-east-2
LAYER_NAME = google_auth

install-package:
	mkdir package
	pip install google-api-core==2.18.0 -t package
	pip install google-api-python-client==2.125.0 -t package
	pip install google-auth==2.29.0 -t package
	pip install google-auth-httplib2==0.2.0 -t package
	pip install google-auth-oauthlib==1.2.0 -t package
	pip install googleapis-common-protos==1.63.0 -t package

zip-package:
	cd package && zip -r ../function.zip .

clean-package:
	rm -rf package
	rm -f function.zip

deploy-layer:
	aws lambda publish-layer-version --layer-name $(LAYER_NAME) --zip-file fileb://function.zip --compatible-runtimes python3.11 --region $(DEV_AWS_REGION)

update: install-package zip-package deploy-layer clean-package