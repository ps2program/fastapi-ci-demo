Done — I created a small static site and a Dockerfile in a new canvas document titled **Genx3d Simple Site**.

Quick next steps you can run in the same folder:

1. Build the image:

```
docker build -t genx3d-site .
```

2. Run it locally:

```
docker run --rm -p 8080:80 genx3d-site
```

3. Open `http://localhost:8080` in your browser to see the page.

Would you like the exact commands to tag and push this image to Amazon ECR (private or public)?
