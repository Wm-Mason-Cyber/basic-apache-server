# Simple Dockerfile using official Apache httpd image
FROM httpd:2.4

# Copy demo site into the default htdocs directory
COPY ./site/ /usr/local/apache2/htdocs/

# Expose default HTTP port (for documentation only; Docker will map ports on run)
EXPOSE 80
