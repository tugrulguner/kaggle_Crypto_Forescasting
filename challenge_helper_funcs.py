def kaggle_data_importer(challenge_link, kaggle_json_path)

  # install kaggle
  !pip install -q kaggle

  #create a kaggle folder
  !mkdir ~/.kaggle

  # copy the kaggle.json to folder
  !cp kaggle.json ~/.kaggle/

  # Permission for the json to act
  !chmod 600 ~/.kaggle/kaggle.json

  # Kaggle competition data download link
  !kaggle competitions download -c g-research-crypto-forecasting
