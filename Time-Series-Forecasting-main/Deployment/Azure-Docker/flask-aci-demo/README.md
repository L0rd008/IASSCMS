# Flask Azure Container Instances (ACI) Deployment Guide

This guide walks you through deploying a Flask application to Azure Container Instances (ACI) using Docker. ACI provides a serverless container environment with per-second billing, making it ideal for applications with variable workloads.

## Prerequisites

Before starting, ensure you have:

- **Azure Account**: Active subscription with contributor permissions
- **Docker Desktop**: Latest version installed and running
- **Azure CLI**: For command-line deployment (optional, but recommended)
- **Python 3.x**: For local development and testing
- **Visual Studio Code**: With Docker extension (recommended)

## Step 1: Build Docker Image

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/flask-aci-demo.git
cd flask-aci-demo
```

### 3. Build the Docker image
```bash
docker build -t flask-aci-demo .
```

### 4. Run the Docker container locally to test
```bash
docker run -p 80:80 flask-aci-demo
```

Visit `http://localhost` to verify the application works correctly. The application should load without errors.

## Step 2: Push Docker Image to Azure Container Registry (ACR)

### 1. Create an Azure Container Registry (ACR) instance

**Using Azure CLI:**
```bash
az login
az acr create --resource-group yourResourceGroup --name yourregistry --sku Basic
```

**Using Azure Portal:**
1. Navigate to Azure Portal → Create Resource → Container Registry
2. Fill in the following details:
   - Registry name: `flaskacireg` (must be globally unique)
   - Resource group: Create new or use existing
   - Location: Choose nearest region
   - SKU: Basic
3. Click "Review + create" and then "Create"

### 2. Login to ACR

**Using Azure CLI:**
```bash
az acr login --name yourregistry
```

**Using Azure Portal:**
1. Go to your registry in the Azure portal
2. Navigate to Settings → Access keys
3. Enable Admin user
4. Note down the username and password
5. Login with Docker:
   ```bash
   docker login yourregistry.azurecr.io -u username -p password
   ```

### 3. Tag and push the Docker image to ACR

```bash
docker tag flask-aci-demo yourregistry.azurecr.io/flask-aci-demo:v1
docker push yourregistry.azurecr.io/flask-aci-demo:v1
```

Verify the image was uploaded by checking the "Repositories" section in your ACR instance on the Azure Portal.

## Step 3: Deploy to Azure Container Instances (ACI)

### 1. Create a resource group (if not already created)

**Using Azure CLI:**
```bash
az group create --name yourResourceGroup --location eastus
```

**Using Azure Portal:**
1. Go to Azure Portal → Resource Groups → Create
2. Fill in the details:
   - Resource group name: `flaskaci-rg`
   - Region: East US (or your preferred region)
3. Click "Review + create" and then "Create"

### 2. Create an ACI instance

**Using Azure CLI:**
```bash
az container create \
  --resource-group yourResourceGroup \
  --name flask-aci-demo \
  --image yourregistry.azurecr.io/flask-aci-demo:v1 \
  --registry-login-server yourregistry.azurecr.io \
  --registry-username <username> \
  --registry-password <password> \
  --cpu 1 \
  --memory 1.5 \
  --ip-address public \
  --ports 80 \
  --dns-name-label flask-api-demo
```

**Using Azure Portal:**
1. Go to Azure Portal → Search "Container Instances" → Create
2. Fill in the basics:
   - Resource group: Select your resource group
   - Container name: `flask-aci-demo`
   - Region: Same as resource group
   - Image source: Azure Container Registry
   - Registry: Select your ACR
   - Image: `flaskacireg.azurecr.io/flask-aci-demo:v1`
   - Image tag: `v1`
3. In the Networking tab:
   - Networking type: Public
   - DNS name label: `flask-api-demo` (creates a public URL)
   - Ports: 80 (Protocol: TCP)
4. In the Advanced tab:
   - Restart policy: Always
5. Click "Review + create" and then "Create"

## Step 4: Access the Application

1. After deployment (typically 2-3 minutes), access your ACI instance in the Azure Portal
2. In the Overview section, find:
   - FQDN (Fully Qualified Domain Name): `flask-api-demo.eastus.azurecontainer.io`
   - Public IP address
3. Open the FQDN or IP address in your browser to access your application

## Step 5: Monitor and Manage Your Container

### View container logs
```bash
az container logs --resource-group yourResourceGroup --name flask-aci-demo
```

### Get container events
```bash
az container attach --resource-group yourResourceGroup --name flask-aci-demo
```

### Stop the container
```bash
az container stop --resource-group yourResourceGroup --name flask-aci-demo
```

### Start the container
```bash
az container start --resource-group yourResourceGroup --name flask-aci-demo
```

## Troubleshooting

- **Image pull failed**: Ensure ACR admin user is enabled and credentials are correct
- **Container not starting**: Check container logs for application errors
- **Can't access the application**: Verify network security settings and that the container is running
- **Application errors**: Review the Flask application logs within the container

## Cost Management
ACI charges for CPU and memory usage. Remember to delete unused containers:

```bash
az container delete --resource-group yourResourceGroup --name flask-aci-demo
```

## Additional Resources

- [ACI Documentation](https://docs.microsoft.com/en-us/azure/container-instances/)
- [Azure Container Registry Documentation](https://docs.microsoft.com/en-us/azure/container-registry/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
