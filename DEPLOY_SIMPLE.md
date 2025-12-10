# 🚀 Deploy to Web in 5 Steps

## Deploy your Virtual Try-On app to Hugging Face (FREE!)

---

## Step 1: Get Credentials (1 minute)

Run this command:
```bash
gcloud iam service-accounts create virtual-tryon-sa --project=renderedfitsnew

gcloud projects add-iam-policy-binding renderedfitsnew \
  --member="serviceAccount:virtual-tryon-sa@renderedfitsnew.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

gcloud iam service-accounts keys create credentials.json \
  --iam-account=virtual-tryon-sa@renderedfitsnew.iam.gserviceaccount.com
```

This creates `credentials.json` in your current folder.

---

## Step 2: Create Hugging Face Account (1 minute)

Go to: https://huggingface.co/join

Sign up (free) and verify your email.

---

## Step 3: Create Space (1 minute)

Go to: https://huggingface.co/new-space

Settings:
- **Name:** `virtual-tryon`
- **SDK:** Gradio
- **Hardware:** CPU basic (free)

Click **Create Space**

---

## Step 4: Upload Files (1 minute)

Click **Files** → **Add file** → **Upload files**

Upload these 4 files:
1. `app_deploy.py` (**IMPORTANT: Rename to `app.py`**)
2. `virtual_tryon.py`
3. `config.py`
4. `requirements.txt`

---

## Step 5: Add Secrets (1 minute)

Go to **Settings** → **Repository secrets**

**Add Secret #1:**
- Name: `GOOGLE_CLOUD_PROJECT`
- Value: `renderedfitsnew`
- Click **Add**

**Add Secret #2:**
- Name: `GOOGLE_APPLICATION_CREDENTIALS_JSON`
- Value: Open `credentials.json`, copy ALL text, paste here
- Click **Add**

---

## ✅ Done!

Your app will build automatically (takes 2-3 minutes).

Visit: `https://huggingface.co/spaces/YOUR_USERNAME/virtual-tryon`

Share this URL with anyone!

---

## 🔒 Security

Delete `credentials.json` from your computer after deployment:
```bash
rm credentials.json
```

It's now safely stored in Hugging Face Secrets.

---

## 💰 Cost

- **Hugging Face:** FREE
- **Google Vertex AI:** ~$0.02 per generation

---

## 🎉 That's It!

Your Virtual Try-On is now live on the web!

**Before deploying, your local URL was:**
http://127.0.0.1:7860

**After deploying, anyone can access:**
https://huggingface.co/spaces/YOUR_USERNAME/virtual-tryon

No installation needed! Share the link! 🚀
