def kaggle_data_importer(challenge_name, kaggle_json_path):

  # install kaggle
  !pip install -q kaggle

  #create a kaggle folder
  !mkdir ~/.kaggle

  # copy the kaggle.json to folder
  !cp kaggle_json_path ~/.kaggle/

  # Permission for the json to act
  !chmod 600 ~/.kaggle/kaggle.json

  # Kaggle competition data download link
  !kaggle competitions download -c challenge_name
