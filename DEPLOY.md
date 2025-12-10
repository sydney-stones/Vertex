# 🚀 Deploy Virtual Try-On to the Web

## Super Simple Deployment (5 Minutes)

Deploy your Virtual Try-On app to Hugging Face Spaces for FREE!

---

## 🎯 Quick Setup

### 1. Create Hugging Face Account (30 seconds)
Go to: https://huggingface.co/join
- Sign up (free)
- Verify email

### 2. Create New Space (1 minute)
Go to: https://huggingface.co/new-space

Fill in:
- **Space name:** `virtual-tryon` (or anything you want)
- **License:** `mit`
- **SDK:** `Gradio`
- **Space hardware:** `CPU basic` (free)

Click **Create Space**

### 3. Get Google Cloud Credentials (2 minutes)

#### Option A: Service Account (Recommended)
```bash
# Create service account
gcloud iam service-accounts create virtual-tryon-sa \
  --project=renderedfitsnew

# Grant Vertex AI User role
gcloud projects add-iam-policy-binding renderedfitsnew \
  --member="serviceAccount:virtual-tryon-sa@renderedfitsnew.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

# Create key
gcloud iam service-accounts keys create credentials.json \
  --iam-account=virtual-tryon-sa@renderedfitsnew.iam.gserviceaccount.com
```

This creates `credentials.json` file.

### 4. Upload Files to Hugging Face (2 minutes)

In your new Space, click **Files** → **Add file** → **Upload files**

Upload these files:
- `app_deploy.py` → Rename to `app.py`
- `virtual_tryon.py`
- `config.py`
- `requirements.txt`

### 5. Add Secrets (1 minute)

In your Space, go to **Settings** → **Repository secrets**

Add these secrets:

**Secret 1:**
- Name: `GOOGLE_CLOUD_PROJECT`
- Value: `renderedfitsnew`

**Secret 2:**
- Name: `GOOGLE_APPLICATION_CREDENTIALS_JSON`
- Value: Paste entire contents of `credentials.json` file

### 6. Done! ✨

Your app will build automatically. Visit:
```
https://huggingface.co/spaces/YOUR_USERNAME/virtual-tryon
```

---

## 📋 File Checklist

Files to upload:
- [ ] `app_deploy.py` (rename to `app.py`)
- [ ] `virtual_tryon.py`
- [ ] `config.py`
- [ ] `requirements.txt`

Secrets to add:
- [ ] `GOOGLE_CLOUD_PROJECT`
- [ ] `GOOGLE_APPLICATION_CREDENTIALS_JSON`

---

## 🎨 Customization

### Change App Name
Edit `app_deploy.py`, line 1:
```python
title="Your Custom Title"
```

### Change Theme
Edit `app_deploy.py`, line ~160:
```python
theme=gr.themes.Soft()  # or Base(), Glass(), Monochrome()
```

### Make Public
In Space settings:
- Set visibility to **Public**

### Add Custom Domain
Hugging Face Pro feature ($9/month)

---

## 💰 Cost

**Hugging Face Spaces:** FREE
- CPU basic tier
- Unlimited usage

**Google Vertex AI:** Pay per use
- ~$0.02 per image generation
- Monitor at: https://console.cloud.google.com/billing

---

## 🔒 Security Notes

### Service Account Key
- Keep `credentials.json` PRIVATE
- Never commit to Git
- Only paste into Hugging Face Secrets
- Delete local copy after upload

### Space Visibility
- Set to **Private** if you want to control access
- Set to **Public** to share with anyone

---

## 🆘 Troubleshooting

### "Build Failed"
Check you uploaded all files:
- app.py (renamed from app_deploy.py)
- virtual_tryon.py
- config.py
- requirements.txt

### "Authentication Error"
Check secrets are correct:
- GOOGLE_CLOUD_PROJECT = `renderedfitsnew`
- GOOGLE_APPLICATION_CREDENTIALS_JSON = entire JSON content

### "API Not Enabled"
```bash
gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew
```

### Slow Generation
Normal! AI takes 15-30 seconds per image.

---

## 📱 Share Your App

Once deployed, share the link:
```
https://huggingface.co/spaces/YOUR_USERNAME/virtual-tryon
```

Anyone can use it! No installation needed!

---

## 🎯 Alternative: Google Cloud Run (Advanced)

For more control, deploy to Cloud Run:

```bash
# Build container
gcloud run deploy virtual-tryon \
  --source . \
  --project=renderedfitsnew \
  --region=us-central1 \
  --allow-unauthenticated
```

Cost: ~$0 (generous free tier)

---

## ✨ Summary

**5-Minute Deployment:**
1. Create Hugging Face account
2. Create new Space
3. Get Google Cloud credentials
4. Upload 4 files
5. Add 2 secrets
6. Done!

**Result:**
Your Virtual Try-On app is live on the web!

**Share with anyone:**
Just send them the URL!

---

## 🔗 Useful Links

- **Hugging Face Spaces:** https://huggingface.co/spaces
- **Gradio Docs:** https://gradio.app/docs
- **Google Cloud Console:** https://console.cloud.google.com/home/dashboard?project=renderedfitsnew

---

Ready to deploy? Follow the steps above! 🚀
