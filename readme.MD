1. For launching the telegram bot, please create **_auth_** folder inside the **_src_** folder
2. Create the **_auth_data.py_** file inside the **_auth_** folder.
3. Paste you telegram token into the **_auth_data.py_** file
   1. Example of **_auth_data.py_** file is below.
   ```python
    token = "your_telegram_token"
    ```
4. Install all dependencies by command. 
```python
pip install -r requirements.txt
```
A requirements file is a list of all of a project’s dependencies. This includes the dependencies needed by the dependencies. It also contains the specific version of each dependency, specified with a double equals sign (==).

5. Run the code by executing **_newsBot.py_** file