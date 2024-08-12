# About Convex

Convex is a serverless reactive backend-as-a-service that simplifies state management and syncing across users with automatic real-time updates, caching, and scaling, all through JavaScript or TypeScript functions.

# About this Repo

 This repository demonstrates a basic installation and usage of Convex with Python scripts, providing straightforward examples to help you get started. Since Convex can be challenging for developers transitioning from other tech stacks, this repository aims to facilitate a smooth introduction to using Convex with Python.

## Installation

1. Clone this repository.
2. Run ```npm init -y``` to create a package.json file.
3. Run ```npm install convex``` to install the Convex SDK.
4. Run ```npx convex dev``` to start the Convex development server.
5. Open a new terminal and run ```npx convex deploy``` to deploy the Convex app.
6. Change the URL in the .env file to the URL of the deployed Convex app.
7. Run ```python app.py``` to start the Python script.
8. Open a browser and navigate to ```http://localhost:5000``` to see the app in action.

You may check the results in the Convex Dashboard to see the state changes in real-time.

- Credits

This repository is inspired by this convex [repo](https://github.com/get-convex/convex-demos/tree/main) made by the official [Convex team](https://github.com/get-convex).