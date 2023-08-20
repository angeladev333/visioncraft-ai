# A Comprehensive Guide on VisionCraft [![VisionCraft](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/angeladev333/hack-the-6ix)

> VisionCraft is a new way to capture and analyze your hardware setup, unlocking a wealth of possibilities

## Project Statistics

<p align="center">
    <a href="https://github.com/simple-icons/simple-icons/actions?query=workflow%3AVerify+branch%3Adevelop">
        <img src="https://img.shields.io/github/actions/workflow/status/simple-icons/simple-icons/verify.yml?branch=develop&logo=github&label=tests" alt="Build status"/>
    </a>
    <a href="https://hits.dwyl.com/angeladev333/hack-the-6ix">
        <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fhits.dwyl.com%2Fangeladev333%2Fhack-the-6ix.json%3Fcolor%3Dpink" alt="HitCount"/>
    </a>
</p>

<p align="center">
    <a href="https://www.npmjs.com/package/simple-icons"><img src="https://img.shields.io/npm/v/simple-icons.svg?logo=npm" alt="NPM version"/></a>
    <a href="https://github.com/{owner}/{repo}/pulls">
    <img src="https://img.shields.io/badge/pull%20requests%20merged-4-blue" alt="Pull Requests Merged">
    </a>
    <a href="https://github.com/{owner}/{repo}/commits">
    <img src="https://img.shields.io/badge/commits-100+-blue" alt="GitHub Commits"> <br/><br/>
    <img src="https://raw.githubusercontent.com/BraveUX/for-the-badge/master/src/images/badges/0-percent-optimized.svg" />
                <img src="https://raw.githubusercontent.com/BraveUX/for-the-badge/master/src/images/badges/60-percent-of-the-time-works-every-time.svg" />
</a>

</p>

## Deployment

Since VisionCraft is a non-static full-stack application, we used [Vercel](https://vercel.com/) to ship the deployment. Github Actions was used in the process.

[View](https://hack-the-6ix-git-master-angeladev333.vercel.app/) deployment at https://hack-the-6ix-git-master-angeladev333.vercel.app/.

## Usage

When an 'upload_image' api request is initiated, the image gets uploaded to the Roboflow API for YOLO Object detection. Then, the user-inputted form data consolidated with the object detection data is forwarded to a sequence of ChatGPT and DALL-E image prompts. The content generated from these processes is then combined to produce a comprehensive guide in PDF format. (edited)

## Tech stack and program architecture

<img src="client/public/VisionCraft_techstack_flow.png" alt="VisionCraft techstack flow">

## Installation (for developers)

### Front-end 

```shell
cd client
```

Install all dependencies, and next

```shell
npm i next
npm install -a
```

Run web app!

```shell
npm run dev
```

### Backend Setup and Deployment

Follow these steps to set up the backend environment and deploy your app. These instructions will guide you through creating a virtual environment, installing dependencies, and deploying to Google App Engine.

#### Step 1: Virtual Environment and Dependencies

1. Create a virtual environment and activate it:
   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required dependencies from `requirements.txt`:
   ```shell
   pip install -r requirements.txt
   ```

#### Step 2: Starting the Server Locally

Start the server using the following command:
   ```shell
   python server/main.py
   ```

#### Step 3: Deployment to Google App Engine

Before deploying to Google App Engine, ensure you have the [gCloud CLI](https://cloud.google.com/sdk/gcloud) installed and authenticated with your Google account.

1. Install the gCloud CLI if you haven't already.

2. Authenticate with Google:
   ```shell
   gcloud auth login
   ```

3. Deploy your app to Google App Engine using:
   ```shell
   gcloud app deploy
   gcloud app browse
   ```

That's it! Your app is now deployed and accessible via the provided URL using Google App Engine.

## Third-Party Extensions

| Extension                                                                        |                                                                                      |
| :------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| [Python package](https://github.com/sachinraja/simple-icons-py)                  | <img src="https://simpleicons.org/icons/python.svg" alt="Python" width=24 height=24> |
| [React package](https://github.com/icons-pack/react-simple-icons)                | <img src="https://simpleicons.org/icons/react.svg" alt="React" width=24 height=24>   |
| [NextUI for React](https://github.com/nextui-org/react)                          |                                                                                      |
| [React Simple Typewriter](https://www.npmjs.com/package/react-simple-typewriter) |                                                                                      |
| [YOLO 3V](https://pjreddie.com/darknet/yolo/)                                    |                                                                                      |
| [IPFS](https://ipfs.io/)                                                         | <img src="https://simpleicons.org/icons/ipfs.svg" alt="IPFS" width=24 height=24>     |
