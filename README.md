# ZEUS - Remote Administration Tool

ZEUS is a powerful remote administration tool built with Python, designed to provide seamless control over a target system remotely. With ZEUS, you can perform a range of actions on the target system, making it a versatile tool for various tasks.

## Features

1. **Upload-Download Files to and from Firebase**: ZEUS allows you to effortlessly upload and download files between the target system and Firebase, enabling seamless data exchange.

2. **Capture Webcam**: This feature enables you to remotely access the target system's webcam and capture images.

3. **Execute CMD Commands**: ZEUS empowers you to execute command-line (CMD) commands on the target system remotely.

4. **Capture Screenshots**: Remotely capture screenshots of the target system's display to monitor activities.

5. **Text-To-Speech**: ZEUS offers a text-to-speech functionality, enabling you to convert text to speech on the target system.



## Getting Started

To run the ZEUS project, follow these steps:

1. **Clone or Download**: Clone the ZEUS repository using Git or download the zip file from [https://github.com/Ashenoy64/ZEUS](https://github.com/Ashenoy64/ZEUS).

   ```bash
   # Clone the repository
   git clone https://github.com/Ashenoy64/ZEUS.git
   ```

   If you choose to download the zip file, extract it to your desired location.

2. **Install Requirements**: Install the necessary dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure .env File**: Create a `.env` file in the root directory and add the following parameters with their respective values:

   ```
   IP=127.0.0.1
   PORT=9999
   SERVICE_KEY_PATH=<path to service_key.json>
   API_KEY=<your-firebase-api-key>
   AUTH_DOMAIN=<your-firebase-auth-domain>
   DATABASE_URL=<your-firebase-database-url>
   PROJECT_ID=<your-firebase-project-id>
   STORAGE_BUCKET=<your-firebase-storage-bucket>
   ```

   Replace `<path to service_key.json>` with the path to your Firebase service key file, and `<your-firebase-parameters>` with the corresponding values from your Firebase project.

4. **Run the Server**: Navigate to the `server` directory and run the main.py file:

   ```bash
   cd server
   python main.py
   ```

5. **Run the Client**: In a new terminal, navigate to the `client` directory and run the main.py file:

   ```bash
   cd client
   python main.py
   ```

   The client will now connect to the ZEUS server, allowing you to remotely control the target system using the available features.

# SCREENSHOT
![image](https://user-images.githubusercontent.com/85382114/178546746-c0968e39-f111-41b7-983a-6025b564cb78.png)


## Commands Available

Once a connection is established, you can run the following commands on the ZEUS server to execute specific operations:

1. `display`: Displays all the available commands, providing a list of supported actions.

2. `run <terminal command>`: Executes the provided terminal command on the target system remotely. For example, `run ls` will list the contents of the target system's directory.

3. `capture`: Captures a picture through the target system's webcam and allows you to view it remotely.

4. `screen capture`: Takes a screenshot of the target system's display, providing a real-time view of the screen.

5. `upload <filename>`: Uploads the specified file to Firebase, allowing seamless data transfer between the target system and the cloud.

6. `download <filename>`: Downloads a file from Firebase to the target system, enabling easy retrieval of files from the cloud.

7. `say <text>`: Utilizes text-to-speech functionality to speak out the provided text on the target system.

8. `b*tch`: ???

Please ensure that you use these commands responsibly and with appropriate authorization. ZEUS is intended for legitimate purposes and should not be used for unauthorized or malicious activities.


## License

The ZEUS project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

This tool is intended for educational and authorized testing purposes only. Unauthorized access to systems without proper consent is illegal. The authors of ZEUS are not responsible for any misuse or damage caused by the usage of this tool.

## Thank You for Exploring ZEUS!

We sincerely thank you for taking the time to explore the ZEUS project. We hope that you find its remote administration capabilities intriguing and useful for your intended purposes.

If you have any feedback, suggestions, or encounter any issues, please feel free to open an issue or submit a pull request on [GitHub](https://github.com/Ashenoy64/ZEUS).

Happy coding and remote administering with ZEUS!

---
