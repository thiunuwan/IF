## GITHUB ISSUE FETCHER

A web tool for fetching GitHub issue details in JSON format. Users can retrieve details for individual issues or schedule bulk retrieval for multiple repositories and issue IDs.

### Docker Setup

This project can be easily run using Docker. Follow the steps below to build and run the application inside a Docker container.

### Build Docker Image
1.Navigate to the project directory where the Dockerfile is located.

2.Run the following command to build the Docker image:

```
docker build -t github-issue-fetcher .
```
This command will create a Docker image named github-issue-fetcher based on the Dockerfile in the current directory.

### Build Docker Image

Once the image is built, you can run the application in a Docker container using the following command:

```
docker run -d -p 5000:5000 --name github-issue-fetcher github-issue-fetcher
```

This command will start a Docker container with the following settings:

- Port mapping: Maps port 5000 on your local machine to port 5000 in the container.
- Container name: Names the container github-issue-fetcher.
- Image: Runs the application using the github-issue-fetcher Docker image.

#### Verify the Application
Once the container is running, you can verify that the application is working by visiting `http://localhost:5000/hello` in your web browser.