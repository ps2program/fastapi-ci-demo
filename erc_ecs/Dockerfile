

# Dockerfile
# Use the official lightweight Nginx image to serve static content
FROM nginx:stable-alpine


# Remove the default nginx index page
RUN rm -f /usr/share/nginx/html/*


# Copy our single-file site to the nginx html folder
COPY index.html /usr/share/nginx/html/index.html


# Expose port 80 and run nginx in the foreground
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]