## Run the docker image locally

### ✅ 1. Build the Docker Image

In the root of your project (where `Dockerfile` is located):

```bash
docker build -t model .
```

### ✅ 2. Run the Docker Container

```bash
docker run -p 8000:8000 model
```

This makes the app available at `http://localhost:8000`

If you're using Django, and `CMD` runs `python manage.py runserver 0.0.0.0:8000`, then you’re good to go!

---

### ✅ 3. Access `/predict/` Endpoint

You can now send a POST request to:
```
http://localhost:8000/predict/
```

Using **Postman** or **curl**.

---

### 🧪 Example: Using Postman

- **Method**: POST  
- **URL**: `http://localhost:8000/predict/`  
- **Headers**:
  - `Content-Type: application/json`
- **Body** → raw → JSON:

```json
{
  "data": [30, 53172, 588, 3, 42]
}
```

---

### 🧪 Example: Using `curl` (terminal)

```bash
curl -X POST http://localhost:8000/predict/ \
     -H "Content-Type: application/json" \
     -d '{"data": [30, 53172, 588, 3, 42]}'
```

You’ll get a response like:

```json
{
  "prediction": 0.989999
}
```

## Deploy model in Docker Hub

#### 1. **Log in to Docker Hub**
```bash
docker login
```

#### 2. **Tag your image**
If Docker Hub username is `induwara3`, tag it like:

```bash
docker tag loan-model induwara3/loan-model:latest
```

> Replace `loan-model` with your local image name 

#### 3. **Push it to Docker Hub**
```bash
docker push induwara3/loan-model:latest
```

Now it's publicly available at:  
👉 `https://hub.docker.com/r/induwara3/loan-model`

---

### ✅ Run the Image From Anywhere

On any machine with Docker installed:

```bash
docker pull induwara3/loan-model:latest
docker run -p 8000:8000 induwara3/loan-model:latest
```

Now your API is live at `http://localhost:8000/predict/` 🔥

---

### Using Docker Compose with Hub Image

In your `docker-compose.yml`, use:

```yaml
version: '3.8'

services:
  model:
    image: induwara3/loan-model:latest
    ports:
      - "8000:8000"
```

Then run:

```bash
docker-compose up
```
