install-package:
	mkdir package
	pip install boto3==1.34.120 -t package
	pip install botocore==1.34.120 -t package
	pip install jmespath==1.0.1 -t package
	pip install python-dateutil==2.9.0.post0 -t package
	pip install s3transfer==0.10.1 -t package
	pip install six==1.16.0 -t package
	pip install urllib3==2.2.1 -t package

update-package:
	pip install -r requirements.txt -t package --upgrade

zip-package:
	cd package && zip -r ../function.zip .

clean-package:
	rm -rf package
	rm -f function.zip