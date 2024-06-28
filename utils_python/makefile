# ====================
# Datos estaticos
# ====================

DEV_AWS_REGION = us-east-2
LAYER_NAME = utils_python

install-package:
	mkdir -p layer_utils_python/python
	pip install beautifulsoup4==4.12.2 -t layer_utils_python/python
	pip install python-dotenv==1.0.1 -t layer_utils_python/python
	pip install cachetools==5.3.3 -t layer_utils_python/python
	pip install httplib2==0.19.1 -t layer_utils_python/python
	pip install uritemplate==4.1.1 -t layer_utils_python/python
	pip install urllib3==1.26.7 -t layer_utils_python/python
	pip install pyasn1==0.6.0 -t layer_utils_python/python
	pip install pyasn1_modules==0.4.0 -t layer_utils_python/python
	pip install pyparsing==3.1.2 -t layer_utils_python/python
	pip install requests==2.32.3 -t layer_utils_python/python
	pip install requests-oauthlib==2.0.0 -t layer_utils_python/python

zip-package:
	cd layer_utils_python && zip -r ../layer_utils_python.zip .

clean-package:
	rm -rf layer_utils_python
	rm -f layer_utils_python.zip

deploy-layer:
	aws lambda publish-layer-version --layer-name $(LAYER_NAME) --zip-file fileb://layer_utils_python.zip --compatible-runtimes python3.11 --region $(DEV_AWS_REGION)

update: install-package zip-package deploy-layer clean-package