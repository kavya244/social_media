User opens the Streamlit app on Render.

User enters topic + platform + tone and clicks Generate.

App sends prompt to OpenAI (model: gpt-4o-mini) and receives post text.

App displays generated text. User may click Save.

If Save clicked, app writes the post to Firebase Realtime DB using service-account credentials (provided via environment variable).

All code, assets and deployment config live in the GitHub repo; Render automatically deploys when changes are pushed to the tracked branch.