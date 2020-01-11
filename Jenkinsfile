
def labels = ['master','slave'] 
def builders = [:]
for (x in labels) {
    def label = x // Need to bind the label variable before the closure 

    // Create a map to pass in to the 'parallel' step so we can fire all the builds at once
    builders[label] = {
		timestamps {
			node () {
				
				def PROJECT="/home/ubuntu/Dev/booking"
				def PYTHON_P="$PROJECT/bin/python3.6"
				def GET_SECRET="/var/lib/jenkins/run_vars_booking.py"
				
				
				stage ('Checkout') {
					// checkout scm
					sh """ 
					sudo service apache2 stop
					cd $PROJECT
					sudo git fetch --all
					sudo git reset --hard origin/master
					"""
				}

				stage ('Build') {
					
					sh """ 

					cd $PROJECT
					sudo virtualenv -p python3 .
					sudo chmod -R 770 $PROJECT
					sudo chown -R www-data:www-data $PROJECT
					. bin/activate
					echo 'which python are you running?'
					which python
					cd src

					sudo $PYTHON_P -m pip install --upgrade pip # Upgrade pip
					echo 'pip upgrade done'
					sudo $PYTHON_P -m pip install -r REQUIREMENTS.txt # Install or upgrade dependencies
					echo 'pip install done'
					sudo $PYTHON_P $GET_SECRET
					echo 'var import done'

					# sudo $PYTHON_P manage.py createcachetable cache_table

					# sudo $PYTHON_P manage.py makemigrations                  

					# sudo $PYTHON_P manage.py migrate                  
					echo 'manage.py migrate done'

					# sudo /usr/local/bin/compile_messages

					sudo $PYTHON_P manage.py collectstatic --noinput  # Collect static files
					echo 'manage.py collectstatic done'

					deactivate # quit the virtual environment

					sudo service apache2 start

					""" 
				}
			}
		}
    }
}

throttle(['loadbalancer']) {
  parallel builders
}




