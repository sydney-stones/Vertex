# Your Custom Setup Guide - renderedfitsnew

## ✅ What's Already Done

- ✅ Project ID configured: `renderedfitsnew`
- ✅ Python virtual environment created
- ✅ Dependencies installed
- ✅ Your images found:
  - Person: `input_images/person/model.png` (1.4 MB)
  - Outfit: `input_images/clothing/outfit.png` (564 KB)
- ✅ Custom script created: [run_my_tryon.py](run_my_tryon.py)

## 🚀 Quick Start - 3 Steps

### Step 1: Install Google Cloud CLI

Since gcloud CLI is not installed, you need to install it first:

**macOS (using Homebrew):**
```bash
brew install google-cloud-sdk
```

**macOS (manual install):**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

**Or download from:**
https://cloud.google.com/sdk/docs/install

### Step 2: Authenticate & Enable API

After installing gcloud CLI:

```bash
# 1. Login to your Google Cloud account
gcloud auth login

# 2. Set up application default credentials (required for API)
gcloud auth application-default login

# 3. Set your project
gcloud config set project renderedfitsnew

# 4. Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew
```

### Step 3: Run Your Virtual Try-On!

```bash
# Activate the virtual environment
source venv/bin/activate

# Run the custom script
python run_my_tryon.py
```

## 📋 Alternative: Use Google Cloud Console

If you prefer to use the web interface:

### Enable Vertex AI API via Console:
1. Go to: https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=renderedfitsnew
2. Click "Enable"

### Set up Authentication:
You still need gcloud CLI for authentication:
```bash
gcloud auth application-default login
```

## 🎯 What the Script Does

The [run_my_tryon.py](run_my_tryon.py) script will:

1. Load your person image (`model.png`)
2. Load your outfit image (`outfit.png`)
3. Send them to Google's Virtual Try-On API
4. Generate a new image showing the model wearing the outfit
5. Save the result to `output_images/` with a timestamp

## 💰 Important: Billing

⚠️ **Make sure billing is enabled on your project!**

Check here:
https://console.cloud.google.com/billing/projects

Virtual Try-On is a paid API. Typical cost is a few cents per image generated.

## 🔧 Troubleshooting

### "Authentication failed"
```bash
gcloud auth application-default login
```

### "API not enabled"
```bash
gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew
```

### "Permission denied"
- Make sure you're the owner or have Editor role on the project
- Check: https://console.cloud.google.com/iam-admin/iam?project=renderedfitsnew

### "Quota exceeded"
- Check quotas: https://console.cloud.google.com/iam-admin/quotas?project=renderedfitsnew
- You may need to request a quota increase

## 📱 Your Project Info

- **Project ID:** renderedfitsnew
- **Project Number:** 966434497382
- **Region:** us-central1
- **Console:** https://console.cloud.google.com/home/dashboard?project=renderedfitsnew

## 🎨 Your Images

Located at:
- **Person:** [input_images/person/model.png](input_images/person/model.png)
- **Outfit:** [input_images/clothing/outfit.png](input_images/clothing/outfit.png)

## 🚦 Status Checklist

Complete these in order:

- [ ] Install gcloud CLI
- [ ] Run `gcloud auth login`
- [ ] Run `gcloud auth application-default login`
- [ ] Run `gcloud services enable aiplatform.googleapis.com --project=renderedfitsnew`
- [ ] Verify billing is enabled
- [ ] Run `source venv/bin/activate`
- [ ] Run `python run_my_tryon.py`
- [ ] Check `output_images/` for your result!

## 🎬 Expected Output

When successful, you'll see:

```
======================================================================
Virtual Try-On Demo - renderedfitsnew
======================================================================

Initializing Virtual Try-On client...
Project: renderedfitsnew
Location: us-central1
Client initialized successfully!

✅ Found person image: input_images/person/model.png
✅ Found clothing image: input_images/clothing/outfit.png

======================================================================
Starting Virtual Try-On...
======================================================================

Processing try-on:
  Person: input_images/person/model.png
  Clothing: input_images/clothing/outfit.png
  Saved: output_images/tryon_20251210_HHMMSS_0.jpeg

======================================================================
✅ SUCCESS! Virtual Try-On Complete!
======================================================================

Generated image saved to:
  output_images/tryon_20251210_HHMMSS_0.jpeg

You can view the image in the output_images/ folder!
```

## 📞 Next Steps

Once you've completed the authentication:

1. Run the script: `python run_my_tryon.py`
2. Check the output image
3. Try generating multiple variations
4. Experiment with different clothing items

## 🔗 Useful Links

- **Project Dashboard:** https://console.cloud.google.com/home/dashboard?project=renderedfitsnew
- **Vertex AI:** https://console.cloud.google.com/vertex-ai?project=renderedfitsnew
- **Billing:** https://console.cloud.google.com/billing
- **API Library:** https://console.cloud.google.com/apis/library?project=renderedfitsnew
- **gcloud Install:** https://cloud.google.com/sdk/docs/install

---

**Ready?** Just install gcloud CLI, authenticate, and run `python run_my_tryon.py`! 🚀
