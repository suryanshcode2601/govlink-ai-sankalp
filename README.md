<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# Run and deploy your AI Studio app

This contains everything you need to run your app locally.

View your app in AI Studio: https://ai.studio/apps/de66c3f4-3fcb-4616-8f36-7b5d752169e5

## Run Locally

**Prerequisites:**  Node.js


1. Install dependencies:
   `npm install`
2. Set the `GEMINI_API_KEY` in [.env.local](.env.local) to your Gemini API key
3. Run the app:
   `npm run dev`


By the get we are sending information only through url
through get we are sending the information through url only 
Now by using post we get the output in base model


Summary of the Flow-Setting.tsx
User opens page: Data is fetched from useApp.

User edits text: formData is updated locally.

User clicks "Save": A spinner appears, a delay occurs, and then updateUserSettings saves the data globally.