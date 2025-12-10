# 🚀 Deploy to Google Cloud Run (3 Minutes)

## Super Simple - You're Already on Google Cloud!

Since your project is already on Google Cloud (`renderedfitsnew`), deploying to Cloud Run is the easiest option.

---

## ✅ Why Cloud Run?

- **FREE tier** - Up to 2 million requests/month
- **Already authenticated** - Uses your existing project
- **Auto-scales** - Handles traffic automatically
- **Fast** - Deploys in 2-3 minutes
- **Professional** - Get a real URL

---

## 🎯 Deploy in 3 Commands

### Command 1: Prepare App (10 seconds)
```bash
# Update app_deploy.py for Cloud Run
sed -i '' 's/server_port=7860/server_port=int(os.getenv("PORT", 8080))/' app_deploy.py
```

### Command 2: Enable Cloud Run API (10 seconds)
```bash
gcloud services enable run.googleapis.com --project=renderedfitsnew
```

### Command 3: Deploy! (2-3 minutes)
```bash
gcloud run deploy virtual-tryon \
  --source . \
  --project=renderedfitsnew \
  --region=us-central1 \
  --platform=managed \
  --allow-unauthenticated \
  --port=8080 \
  --memory=2Gi \
  --timeout=300 \
  --set-env-vars="GOOGLE_CLOUD_PROJECT=renderedfitsnew,GOOGLE_CLOUD_REGION=us-central1"
```

---

## ✨ That's It!

You'll see output like:
```
Service [virtual-tryon] revision [virtual-tryon-00001] has been deployed
and is serving 100 percent of traffic.
Service URL: https://virtual-tryon-abc123-uc.a.run.app
```

**Your app is live!** Share the URL with anyone!

---

## 📝 What Just Happened?

1. Cloud Run created a container from your code
2. Deployed it to Google's infrastructure
3. Gave you a public URL
4. Set up auto-scaling
5. Used your existing Google Cloud authentication

---

## 💰 Cost

**Cloud Run Free Tier (generous!):**
- 2 million requests/month
- 360,000 GB-seconds/month
- 180,000 vCPU-seconds/month

**Your app likely stays FREE!**

Monitor: https://console.cloud.google.com/run?project=renderedfitsnew

**Vertex AI costs still apply:**
~$0.02 per image generation

---

## 🎨 Custom Domain (Optional)

Want your own domain? (e.g., `tryon.yourdomain.com`)

```bash
# Map custom domain
gcloud run services update virtual-tryon \
  --project=renderedfitsnew \
  --region=us-central1 \
  --custom-domain=tryon.yourdomain.com
```

Follow the DNS instructions shown.

---

## 🔄 Update Your App

Made changes? Redeploy:

```bash
gcloud run deploy virtual-tryon \
  --source . \
  --project=renderedfitsnew \
  --region=us-central1
```

---

## 🛑 Delete Deployment

Want to remove it?

```bash
gcloud run services delete virtual-tryon \
  --project=renderedfitsnew \
  --region=us-central1
```

---

## 🆘 Troubleshooting

### "Build failed"
Check you have all files:
- app_deploy.py
- virtual_tryon.py
- config.py
- requirements.txt
- Dockerfile

### "Authentication error"
The app automatically uses your project's authentication. No extra setup needed!

### "Memory exceeded"
Increase memory:
```bash
gcloud run services update virtual-tryon \
  --memory=4Gi \
  --project=renderedfitsnew \
  --region=us-central1
```

### "Timeout"
Increase timeout:
```bash
gcloud run services update virtual-tryon \
  --timeout=600 \
  --project=renderedfitsnew \
  --region=us-central1
```

---

## 📊 Monitor Your App

**View logs:**
```bash
gcloud run services logs read virtual-tryon \
  --project=renderedfitsnew \
  --region=us-central1
```

**View in Console:**
https://console.cloud.google.com/run/detail/us-central1/virtual-tryon?project=renderedfitsnew

---

## 🎯 Comparison: Cloud Run vs Hugging Face

| Feature | Cloud Run | Hugging Face |
|---------|-----------|--------------|
| **Setup** | 3 commands | 5 steps (web UI) |
| **Cost** | Free tier | Always free |
| **Speed** | Very fast | Fast |
| **Authentication** | Built-in | Need to add secrets |
| **Custom Domain** | Easy | Paid ($9/mo) |
| **Best For** | Production use | Quick sharing |

**Both are great!** Choose based on your needs.

---

## ✨ Summary

**Deploy to Cloud Run:**
```bash
# 1. Enable API
gcloud services enable run.googleapis.com --project=renderedfitsnew

# 2. Deploy
gcloud run deploy virtual-tryon \
  --source . \
  --project=renderedfitsnew \
  --region=us-central1 \
  --allow-unauthenticated \
  --set-env-vars="GOOGLE_CLOUD_PROJECT=renderedfitsnew"
```

**Result:**
Your app is live on the web with a professional URL! 🚀

**Cost:**
Likely FREE (generous free tier) + Vertex AI usage

**Share:**
Just send the URL to anyone!

---

Ready? Run the commands above! ⬆️
