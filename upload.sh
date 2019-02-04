if [[ -z "$AWS_S3_BUCKET" ]]
  then
  python trello_upload.py "$@"
else
    python s3_upload.py "$@"
fi
