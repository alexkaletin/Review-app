This is a simple course review app that is run serverless. 
It utilizes google datastore for the backend
and google run for managing container.
Also the container image is stored in google container
Mostly taken from labs 5.2g and 6.3g

Commands:
In cloudshell:
```
    clone git <repo-name>
    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt
    python app.py
```
Prepare container image
```
    gcloud builds submit --timeout=900 --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/<container_name>
```

Run container via google run using least IAM role
``` 
  gcloud run deploy <container-name> \
  --image gcr.io/${GOOGLE_CLOUD_PROJECT}/<container-name> \
  --service-account <service-account-name>@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com 
```

  
