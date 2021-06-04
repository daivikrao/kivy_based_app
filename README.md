# kivy_based_app
## **Description**

  * The project makes use of python and a python libary called kivy.
  * Its an app which displays quotes when certain feeling is typed.
  * The user needs to signin before using the app.
  * The details of the user are stored in the json file.

    * To install kivy

    ```python
         pip install kivy
    ```
  * Once the python file is ready it has to be converted to .apk file.
  * This could be done using ubuntu operating system.
  * In the terminal run the command "bash buildozer_installer.sh" to install all the dependencies.
  * Then inorder to install the buildozer.spec file run the command "buildozer init".
  * Then run the final command "buildozer android dubug".
  * You will then get an .apk file which could be installed in the phone.
