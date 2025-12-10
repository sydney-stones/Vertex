# 🚀 Deploy to Your Hugging Face Space

## Your Space: `sydstones02/vertex`

Quick deployment to your already-created Hugging Face Space!

---

## Step 1: Clone Your Space (30 seconds)

```bash
# Clone your space
git clone https://huggingface.co/spaces/sydstones02/vertex
cd vertex
```

When prompted for password, use an access token:
- Go to: https://huggingface.co/settings/tokens
- Click "New token"
- Name: `vertex-deploy`
- Type: `Write`
- Copy the token and paste as password

---

## Step 2: Copy Files (30 seconds)

```bash
# Copy the needed files from your project
cp ../app_deploy.py app.py
cp ../virtual_tryon.py .
cp ../config.py .
cp ../requirements.txt .
cp ../README.md .
```

---

## Step 3: Add Credentials to Secrets (1 minute)

**Get credentials first:**

```bash
cd ..

# Create service account key
gcloud iam service-accounts create virtual-tryon-sa --project=renderedfitsnew

gcloud projects add-iam-policy-binding renderedfitsnew \
  --member="serviceAccount:virtual-tryon-sa@renderedfitsnew.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

gcloud iam service-accounts keys create credentials.json \
  --iam-account=virtual-tryon-sa@renderedfitsnew.iam.gserviceaccount.com

# Display the credentials (copy this output)
cat credentials.json
```

**Add to Hugging Face:**

1. Go to: https://huggingface.co/spaces/sydstones02/vertex/settings
2. Click "Repository secrets"
3. Add these secrets:

**Secret #1:**
- Name: `GOOGLE_CLOUD_PROJECT`
- Value: `renderedfitsnew`
- Click "Add"

**Secret #2:**
- Name: `GOOGLE_APPLICATION_CREDENTIALS_JSON`
- Value: (paste entire output from `cat credentials.json`)
- Click "Add"

---

## Step 4: Push to Deploy (1 minute)

```bash
cd vertex

# Add all files
git add app.py virtual_tryon.py config.py requirements.txt README.md

# Commit
git commit -m "Add Virtual Try-On application"

# Push (will ask for token again)
git push
```

---

## Step 5: Wait for Build (2-3 minutes)

Watch the build at:
https://huggingface.co/spaces/sydstones02/vertex

Once it says "Running", your app is live! 🎉

---

## ✅ Your App is Live!

**URL:** https://huggingface.co/spaces/sydstones02/vertex

Share this with anyone!

---

## 🔒 Security: Delete Local Credentials

```bash
cd ..
rm credentials.json
```

The credentials are now safely stored in Hugging Face Secrets.

---

## 🆘 Troubleshooting

### "Build failed"
Check the logs at your Space URL. Common issues:
- Missing files (check all 4 files were added)
- Syntax errors (check app.py is valid)

### "Authentication error"
- Make sure both secrets were added correctly
- Verify `GOOGLE_APPLICATION_CREDENTIALS_JSON` has the complete JSON

### "API not enabled"
```bash
gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew
```

---

## 🔄 Update Your App

Made changes? Just push again:

```bash
cd vertex
# Make your changes to files
git add .
git commit -m "Update app"
git push
```

Hugging Face will automatically rebuild!

---

## ✨ Summary

```bash
# 1. Clone
git clone https://huggingface.co/spaces/sydstones02/vertex
cd vertex

# 2. Copy files
cp ../app_deploy.py app.py
cp ../virtual_tryon.py .
cp ../config.py .
cp ../requirements.txt .

# 3. Get credentials
gcloud iam service-accounts keys create credentials.json \
  --iam-account=virtual-tryon-sa@renderedfitsnew.iam.gserviceaccount.com

# 4. Add secrets at: https://huggingface.co/spaces/sydstones02/vertex/settings

# 5. Push
git add .
git commit -m "Add Virtual Try-On application"
git push
```

**Result:** Your app is live at https://huggingface.co/spaces/sydstones02/vertex

---

Ready? Start with Step 1! 🚀
