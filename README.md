# Test Automation of Python project in Dockerized Jenkins

### Ideas:

> All files hosted here: 


1.Create a Dockerized Jenkins container.

* ```JenkinsDockerfile```: Lightweight Dockerfile to Dockerize Jenkins 

2.Write sample automation tests for sample project.
* ```src/compute.py```: Contains sample compute project.
* ```tests/test_compute.py```: Contains sample automation tests.Ref: [pytest](https://docs.pytest.org/)
* ```pytest.ini```: includes a single line “junit_family=xunit1” to ignore warnings, pytest configuration file.
* ```Push project to Github.```

3.Create a Dockerized test project image from ```Dockerfile```.

4.Run test project image from Jenkins container.

* On Add build step->Execute shell in Jenkins paste:

```shell
IMAGE_NAME="python-project-compute-image"
CONTAINER_NAME="python-project-compute-image-container"
docker build -t $IMAGE_NAME .
docker run -d --name $CONTAINER_NAME $IMAGE_NAME
rm -rf reports; mkdir reports
docker cp $CONTAINER_NAME:/python-project-compute/reports/result.xml reports/
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker rmi $IMAGE_NAME
```

* JUnit plugin is required on Jenkins

5.Inspect test result:

* Test result will reside in```reports/result.xml``` file on the test container, Jenkins container will collect this test result to publish.

### Setup:

1.Build Jenkins docker image.

```shell
sudo su
docker build -t jenkins-docker-image -f JenkinsDockerfile .
```

2.Run Jenkins docker image

```shell
docker run -d -p 8080:8080 --name jenkins-docker-container -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker-image
```

* Use ```docker rm <container-id>``` to remove any existing ```similar named``` container.

3.Get Jenkins initial setup password & visit ```http://localhost:8080/``` submit Jenkins initial setup password.

```shell
docker exec -it jenkins-docker-container cat var/jenkins_home/secrets/initialAdminPassword
```

* Check ```jenkins-docker-container``` is running:```docker container ls```

4.Provide username, password, install plugins.

### How to Use:

1.Run stopped container(```jenkins-docker-container```) if not running already.Check all stopped container:```docker ps -a```

```shell
docker start <jenkins-docker-container-id>
```

2.Login here ```http://localhost:8080/``` & use Jenkins, Click **Build Now** in project menu, see console log output.

