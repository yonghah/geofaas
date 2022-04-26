# Point Label

This project creates a lambda function that generates vector tiles of 
the point features with room attributes. This vector tiles will be used
to display room labels to workaround tile boundary issues. 

The process is:

* from room polygon in RDS -> room points (gpkg, ogr2ogr)
* room points -> vector tiles (pbf, ogr2ogr)
* copy the vector tiles to S3 (aws cli or boto)

Alternatively,

* add a secondary geometry column to room polygon table in RDS
  * this will give a good report for converstion status
* convert room points -> vector tiles
* copy the vector tiles to S3


### for testing

* room polygon -> room points 
* count number of points on each polygon 


## Guide on CDK

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
