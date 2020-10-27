The Project is created in Python and uses behave (for BDD )and Seleneium (for driving Web browser).

Setting up Dependencies:
Both are in requirements.txt so any modern python IDE such as pycharm will ask users to install dependencies present in that file.
Another way to install dependencies is to run following commands:
open a terminal
pip install selenium
pip install behave
Another thing which is required is Chrome driver downloadable from web for the version of chrome installed.

Running project:
set the path of chrome driver exe file in features/environment.py variable chrome_driver_path
then directly run the file features_runner.py. It's alternate of runnign CLI commands of behave to run feature. This file will trigger both the feature files.
Screenshots of both feature shall be captured at captured_screenshots
