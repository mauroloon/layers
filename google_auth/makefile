# ====================
# Datos estaticos
# ====================

DEV_AWS_REGION = us-east-2
LAYER_NAME = google_auth

install-package:
	mkdir -p layer/python
	pip install google-api-core==2.18.0 -t layer/python
	pip install google-api-python-client==2.125.0 -t layer/python
	pip install google-auth==2.29.0 -t layer/python
	pip install google-auth-httplib2==0.2.0 -t layer/python
	pip install google-auth-oauthlib==1.2.0 -t layer/python
	pip install googleapis-common-protos==1.63.0 -t layer/python

# Copia el archivo google_auth.py al directorio correcto
copy-files:
	cp google_auth.py layer/python/

zip-package:
	cd layer && zip -r ../layer.zip .

clean-package:
	rm -rf layer
	rm -f layer.zip

deploy-layer:
	aws lambda publish-layer-version --layer-name $(LAYER_NAME) --zip-file fileb://layer.zip --compatible-runtimes python3.11 --region $(DEV_AWS_REGION)

update: install-package copy-files zip-package deploy-layer clean-package
